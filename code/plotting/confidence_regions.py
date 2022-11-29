import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
from matplotlib import rc
import seaborn as sns


rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 26})
rc('text', usetex=True)


def confidence_region_quad(x, y, ax, facecolor=None, edgecolor='k', alpha=0.3):
    """
    Creates a 2-dim exclusion contour at 95% CL at the quadratic level
    Parameters
    ----------
    x: array_like, shape (n, )
        Posterior samples first coefficient
    y: array_like, shape (n, )
        Posterior samples second coefficient
    ax : matplotlib.axes.Axes
        The axes object to draw the ellipse into.
    facecolor: str, optional
        Color of the filled contour
    edgecolor: str, optional
        Edgecolor of the contours
    alpha: float, optional
        Transparency
    """

    sns.kdeplot(x, y, levels=[0.317, 1.0], bw_adjust=1.2, ax=ax, fill=True, alpha=alpha, color=facecolor)
    sns.kdeplot(x, y, levels=[0.317], bw_adjust=1.2, ax=ax, alpha=1, color=edgecolor)


def confidence_region_lin(x, y, ax, facecolor="none", **kwargs):
    """
    Create a 2-dim exclusion contour at 95% CL at the linear level
    Parameters
    ----------
    x: array_like, shape (n, )
        Posterior samples first coefficient
    y: array_like, shape (n, )
        Posterior samples second coefficient
    ax : matplotlib.axes.Axes
        The axes object to draw the ellipse into.
    facecolor: str, optional
        Color of the filled contour
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

    ell_radius_x = np.sqrt(5.99 * eigval_sort[-1])
    ell_radius_y = np.sqrt(5.99 * eigval_sort[-2])

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

    return ax.add_patch(ellipse)


def plot_confidence_region(ax, dfs, ax_labels, coeff1, coeff2, order, colors=None):
    """
    Plots 2-dim 95% CL contours
    Parameters
    ----------
        ax : matplotlib.axes.Axes
            Axes object to plot on
        dfs: list
            List of Pandas Dataframes of posterior samples
        ax_labels: list
            List of x and y label
        coeff1: str
            Name of coefficient on the y-axis
        coeff2: str
            Name of coefficient on the x-axis
        order: str
            Order in the EFT expansion, either `lin` or `quad`
        colors: list, optional
            List of colors that each contours must have
    """

    if colors is None:
        colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]

    for i, df in enumerate(dfs):

        coeff1_values = df[coeff1].values
        coeff2_values = df[coeff2].values

        if coeff1_values is not None and coeff2_values is not None:

            if order == 'lin':

                confidence_region_lin(
                    coeff1_values,
                    coeff2_values,
                    ax,
                    alpha=1,
                    edgecolor=colors[i],
                )

                confidence_region_lin(
                    coeff1_values,
                    coeff2_values,
                    ax,
                    alpha=0.3,
                    facecolor=colors[i],
                    edgecolor=None,
                )

                ax.scatter(
                    np.mean(coeff1_values, axis=0),
                    np.mean(coeff2_values, axis=0),
                    c=colors[i],
                    s=3,
                )

            else:

                confidence_region_quad(coeff1_values,
                                       coeff2_values,
                                       ax,
                                       facecolor='C0',
                                       edgecolor='C0')

        plt.xlabel(ax_labels[0], fontsize=35)
        plt.ylabel(ax_labels[1], fontsize=35)
        plt.tick_params(which="both", direction="in", labelsize=22)