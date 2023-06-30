import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
from matplotlib import rc
import seaborn as sns
import matplotlib.patches as mpatches
import itertools
import os

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 26})
rc('text', usetex=True)


class EllipsePlotter:
    """
    Class to plot 2 dimensional confidence levels bounds
    Parameters
    ----------
        analyzer : Analyzer
            analysis class object
    """

    def __init__(self):

        self.replica_handle_add = False
        pass

    def confidence_contour_kde(self, x, y, ax, hndls, facecolor=None, edgecolor='k', alpha=0.3, taken_together=False):
        """Plot confidence contour using KDE estimation"""
        if not taken_together:
            sns.kdeplot(x=x, y=y, levels=[0.05, 1.0], bw_adjust=1.2, ax=ax, fill=True, alpha=alpha, color=facecolor)
            hndls.append((mpatches.Patch(ec=edgecolor, fc=facecolor, fill=True, alpha=alpha),
                        mpatches.Patch(ec=edgecolor, fc=facecolor, fill=False, alpha=1.0)))
            sns.kdeplot(x=x, y=y, levels=[0.05], bw_adjust=1.2, ax=ax, alpha=1, color=edgecolor)
        else:
            sns.kdeplot(x=x, y=y, levels=[0.05, 1.0], bw_adjust=1.2, ax=ax, fill=True, alpha=alpha, color=facecolor)
            hndls.append((mpatches.Patch(ec=edgecolor, fc=facecolor, fill=True, alpha=alpha),
                        mpatches.Patch(ec=edgecolor, fc=facecolor, fill=False, alpha=1.0)))
            sns.kdeplot(x=x, y=y, levels=[0.05], bw_adjust=1.2, ax=ax, alpha=1, color=edgecolor)

        return hndls


    @staticmethod
    def confidence_ellipse(x, y, ax, facecolor="none", **kwargs):
        """
        Create a plot of the covariance confidence ellipse of `x` and `y`
        Parameters
        ----------
        x, y : array_like, shape (n, )
            Input data.
        ax : matplotlib.axes.Axes
            The axes object to draw the ellipse into.
        n_std : float
            The number of standard deviations to determine the ellipse's radiuses.
        Returns
        -------
        matplotlib.patches.Ellipse
        Other parameters
        ----------------
        kwargs : `~matplotlib.patches.Patch` properties
        """

        if x.size != y.size:
            raise ValueError("x and y must be the same size")

        cov = np.cov(x, y)

        eig_val, eig_vec = np.linalg.eig(cov)

        eig_vec_max = eig_vec[:, np.argmax(eig_val)]

        cos_th = eig_vec[0, np.argmax(eig_val)] / np.linalg.norm(eig_vec_max)
        if eig_vec_max[1] > 0:
            inclination = np.arccos(cos_th)
        else:
            inclination = - np.arccos(cos_th)

        eigval_sort = np.sort(eig_val)

        ell_radius_x = np.sqrt(5.991 * eigval_sort[-1])
        ell_radius_y = np.sqrt(5.991 * eigval_sort[-2])

        ellipse = Ellipse(
            (0, 0),
            width=ell_radius_x * 2,
            height=ell_radius_y * 2,
            facecolor=facecolor,
            **kwargs
        )

        mean_x = np.median(x)
        mean_y = np.median(y)

        transf = (transforms.Affine2D().rotate(inclination).translate(mean_x, mean_y))

        ellipse.set_transform(transf + ax.transData)

        return ax.add_patch(ellipse), inclination

    def plot(self, ax, dfs, ax_labels, coeff1, coeff2, kde=None, labels=None, loc="best", envelope=False, colors=None, alphas=None,
             taken_together=False):
        """
        Plot the 2 standard deviation ellipse of two parameters
        (used for 2 parameter fits)
        Parameters
        ----------
            coeff1: str, optional
                first coefficient
            coeff2: str, optional
                second coefficient
        """

        hndls = []

        if colors is None:
            colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]


        if alphas is None:
            alphas = 0.3 * np.ones(len(colors))

        for i, df in enumerate(dfs):

            coeff1_values = df[coeff1].values
            coeff2_values = df[coeff2].values

            if coeff1_values is not None and coeff2_values is not None:

                if not kde:

                    p1, inc = self.confidence_ellipse(
                        coeff1_values,
                        coeff2_values,
                        ax,
                        alpha=1,
                        edgecolor=colors[i],
                    )

                    p2, _ = self.confidence_ellipse(
                        coeff1_values,
                        coeff2_values,
                        ax,
                        alpha=alphas[i],
                        facecolor=colors[i],
                        edgecolor=None,
                    )

                    ax.scatter(
                        np.mean(coeff1_values, axis=0),
                        np.mean(coeff2_values, axis=0),
                        c=colors[i],
                        s=3,
                    )

                    hndls.append((p1, p2))

                else:

                    # if i == 0:
                    #     if (coeff1 == 'cbHRe' and coeff2 == 'cHj3') or (coeff2 == 'cbHRe' and coeff1 == 'cHj3'):
                    #         ax.scatter(np.random.choice(coeff1_values, 1000, replace=False),
                    #                    np.random.choice(coeff2_values, 1000, replace=False), alpha=alphas[i], color=colors[i],
                    #                    s=5)
                    #         ax.set_xlim((-0.2, 1.0))
                    #         continue

                    if i == 0:
                        taken_together = False
                    else:
                        taken_together = True

                    if envelope and i > 0:
                        if taken_together:
                            facecolor = colors[i]
                            edgecolor = colors[i]
                            alpha = alphas[i]
                        else:
                            facecolor = None
                            edgecolor = 'k'
                            alpha = 1
                    else:
                        facecolor = colors[i]
                        edgecolor = colors[i]
                        alpha = alphas[i]



                    hndls = self.confidence_contour_kde(df[coeff1],
                                                        df[coeff2],
                                                        ax,
                                                        hndls,
                                                        facecolor=facecolor,
                                                        edgecolor=edgecolor,
                                                        alpha=alpha,
                                                        taken_together=taken_together)

                    # if i == 0:
                    #     ax.scatter(np.random.choice(coeff1_values, 1000, replace=False),
                    #                np.random.choice(coeff2_values, 1000, replace=False), alpha=0.3, color=colors[i], s=5)

                # smefit

                # p3 = self.confidence_ellipse_smefit(
                #     coeff1_values,
                #     coeff2_values,
                #     ax,
                #     n_std=1,
                #     alpha=0.3,
                #     facecolor='C1',
                #     edgecolor=None,
                # )
                # p4 = self.confidence_ellipse_smefit(
                #     coeff1_values,
                #     coeff2_values,
                #     ax,
                #     n_std=1,
                #     alpha=1,
                #     edgecolor='C1',
                # )

                # hndls.append((p3, p4))

            plt.xlabel(ax_labels[0], fontsize=35)
            plt.ylabel(ax_labels[1], fontsize=35)
            plt.tick_params(which="both", direction="in", labelsize=22)

        hndls.append(ax.scatter(0, 0, c="k", marker="+", s=50, zorder=10))

        if labels is not None:
            ax.legend(
                loc=loc, handles=hndls, labels=labels, frameon=False, prop={"size": 24}
            )
        else:
            return hndls

        # plt.title(r"${\rm 68\%\ Confidence\ Level\ Bounds}$", fontsize=20)
