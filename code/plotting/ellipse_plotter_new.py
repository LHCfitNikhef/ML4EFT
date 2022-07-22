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
        pass

    @staticmethod
    def confidence_ellipse(x, y, ax, n_std=3.0, facecolor="none", **kwargs):
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
        pearson = cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1])
        # Using a special case to obtain the eigenvalues of this
        # two-dimensionl dataset.
        ell_radius_x = np.sqrt(1 + pearson)
        ell_radius_y = np.sqrt(1 - pearson)
        ellipse = Ellipse(
            (0, 0),
            width=ell_radius_x * 2,
            height=ell_radius_y * 2,
            facecolor=facecolor,
            **kwargs,
        )

        # Calculating the stdandard deviation of x from
        # the squareroot of the variance and multiplying
        # with the given number of standard deviations.
        scale_x = np.sqrt(cov[0, 0]) * n_std
        mean_x = np.mean(x)

        # calculating the stdandard deviation of y ...
        scale_y = np.sqrt(cov[1, 1]) * n_std
        mean_y = np.mean(y)

        transf = (
            transforms.Affine2D()
                .rotate_deg(45)
                .scale(scale_x, scale_y)
                .translate(mean_x, mean_y)
        )

        ellipse.set_transform(transf + ax.transData)
        return ax.add_patch(ellipse)

    def get_coeffiecients_values(self, coeff, fit):
        """
        Get the coefficient posterior or look for
        propagated params.
        Parameters
        ----------
            coeff: str
               coefficient name
            fit: str
                fit name
        Returns
        -------
            coeff_values: numplt.ndarray
                posterior distribution
        """
        # TODO: maybe you can look for something in coefficints
        # utils, to avoid repetition

        if coeff in self.full_labels[fit]:
            # look for posteriors else for propagated params
            if "SNS" in fit:
                coeff_values = np.array(self.coeff_vals[fit][coeff])
            else:
                idx = np.where(np.array(self.full_labels[fit]) == coeff)[0][0]
                coeff_values = np.array(self.coeff_vals[fit][coeff]).T[idx]
        else:
            coeff_values = None
        return coeff_values

    def plot(self, ax, dfs, ax_labels, coeff1, coeff2, samples=None):
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

        lbls = []
        hndls = []
        p1 = []
        p2 = []

        colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

        for i, df in enumerate(dfs):

            coeff1_values = df[coeff1].values
            coeff2_values = df[coeff2].values

            if coeff1_values is not None and coeff2_values is not None:
                if samples is not None:
                    if samples[i]:
                        sns.kdeplot(x=coeff1_values, y=coeff2_values, levels=[0.32, 1.0], bw_adjust=1.2, ax=ax, fill=True, alpha=0.3, color=colors[i])
                        sns.kdeplot(x=coeff1_values, y=coeff2_values, levels=[0.32], bw_adjust=1.2, ax=ax,
                                    alpha=1, color=colors[i])
                        hndls.append(mpatches.Patch(ec=colors[i], fc=colors[i], fill=True, alpha=0.3))

                        ax.scatter(coeff1_values, coeff2_values, s=2, alpha=0.2, color=colors[i])

                else:

                    p2 = self.confidence_ellipse(
                        coeff1_values,
                        coeff2_values,
                        ax,
                        n_std=2,
                        alpha=0.3,
                        facecolor=colors[i],
                        edgecolor=None,
                    )
                    p1 = self.confidence_ellipse(
                        coeff1_values,
                        coeff2_values,
                        ax,
                        n_std=2,
                        alpha=1,
                        edgecolor=colors[i],
                    )


                    p3 = self.confidence_ellipse(
                        coeff1_values,
                        coeff2_values,
                        ax,
                        n_std=1,
                        alpha=1,
                        edgecolor=colors[i],
                        linestyle='dotted'
                    )



                    hndls.append((p1, p2))

                ax.scatter(
                    np.mean(coeff1_values, axis=0),
                    np.mean(coeff2_values, axis=0),
                    c=colors[i],
                    s=3,
                )





            plt.xlabel(ax_labels[0], fontsize=33)
            plt.ylabel(ax_labels[1], fontsize=33)
            plt.tick_params(which="both", direction="in", labelsize=22)



        #plt.xlim(-0.06, 0.06)
        #plt.ylim((-0.5, 0.5))

        ax.scatter(0, 0, c="k", marker="s", s=10, zorder=10)
        # ax.legend(
        #     loc="upper left", handles=hndls, labels=labels, frameon=False, prop={"size": 15}
        # )
        #plt.title(r"${\rm 68\%\ Confidence\ Level\ Bounds}$", fontsize=15)


        return ax, hndls
        #plt.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/15_07/ellipse_zh_llbb_68.pdf')
