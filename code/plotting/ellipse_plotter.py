import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
from matplotlib import rc

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 15})
rc('text', usetex=True)


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

    def plot(self, dfs, labels):
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

        _, ax = plt.subplots(figsize=(6, 6))
        colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

        for i, df in enumerate(dfs):


            coeff1_values = df["ctgre"].values
            coeff2_values = df["cut"].values

            if coeff1_values is not None and coeff2_values is not None:
                p2 = confidence_ellipse(
                    coeff1_values,
                    coeff2_values,
                    ax,
                    n_std=2,
                    alpha=0.3,
                    facecolor=colors[i],
                    edgecolor=None,
                )
                p1 = confidence_ellipse(
                    coeff1_values,
                    coeff2_values,
                    ax,
                    n_std=2,
                    alpha=1,
                    edgecolor=colors[i],
                )
                ax.scatter(
                    np.mean(coeff1_values, axis=0),
                    np.mean(coeff2_values, axis=0),
                    c=colors[i],
                    s=3,
                )



            plt.xlabel(r'$\mathrm{Re}\:C_{tG}$', fontsize=20)
            plt.ylabel(r'$C_{tu}^{(1)}$', fontsize=20)
            plt.tick_params(which="both", direction="in", labelsize=15)

            lbls.append(labels[i])

            hndls.append((p1, p2))

        ax.scatter(0, 0, c="k", marker="s", s=10, zorder=10)
        plt.legend(
            loc="best", handles=hndls, labels=lbls, frameon=False, prop={"size": 18}
        )
        plt.title(r"${\rm 95\%\ Confidence\ Level\ Bounds}$", fontsize=15)
        plt.tight_layout()
        plt.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/23_06/ellipse_nn_truth_2bins.pdf')

def sample_loader(path):
    with open(path) as json_data:
        samples = json.load(json_data)
    df = pd.DataFrame(samples)
    return df

path_to_nn = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/nn/mtt_y_high/posterior.json'
path_to_truth = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/truth/mtt_y/posterior.json'
#path_to_binned_fine = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/binned/fb/posterior.json'
path_to_binned_coarse = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/binned/mzh_y/posterior.json'

df_nn = sample_loader(path_to_nn)
df_truth = sample_loader(path_to_truth)
#df_binned_fine = sample_loader(path_to_binned_fine)
df_binned_coarse = sample_loader(path_to_binned_coarse)

plotter = EllipsePlotter()
plotter.plot([df_nn, df_truth, df_binned_coarse],
             labels=[r"$\mathrm{NN}\;\rm{(median)}$", r"$\mathrm{Truth}$", r"$2\;\mathrm{bins}$",
                     r"$2\;\mathrm{bins}$"])