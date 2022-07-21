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

    def plot(self, ax, dfs, ax_labels, labels, coeff1, coeff2):
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
                # if i==0:
                #     sns.kdeplot(x=coeff1_values, y=coeff2_values, levels=[0.32, 1.0], bw_adjust=1.2, ax=ax, fill=True, alpha=0.3, color=colors[i])
                #     sns.kdeplot(x=coeff1_values, y=coeff2_values, levels=[0.32], bw_adjust=1.2, ax=ax,
                #                 alpha=1, color=colors[i])
                #     hndls.append(mpatches.Patch(ec=colors[i], fc=colors[i], fill=True, label=labels[i], alpha=0.3))
                #     xmin, xmax = plt.xlim()
                #     ymin, ymax = plt.ylim()
                #     ax.scatter(coeff1_values, coeff2_values, s=2, alpha=0.2, color=colors[i])

                #else:



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


                p3 = confidence_ellipse(
                    coeff1_values,
                    coeff2_values,
                    ax,
                    n_std=1,
                    alpha=1,
                    edgecolor=colors[i],
                    linestyle='dotted'
                )
                ax.scatter(
                    np.mean(coeff1_values, axis=0),
                    np.mean(coeff2_values, axis=0),
                    c=colors[i],
                    s=3,
                )

                if i == 0:
                    xmin, xmax = plt.xlim()
                    ymin, ymax = plt.ylim()
                lbls.append(labels[i])

                hndls.append((p1, p2))



            plt.xlabel(ax_labels[0], fontsize=33)
            plt.ylabel(ax_labels[1], fontsize=33)
            plt.tick_params(which="both", direction="in", labelsize=22)


        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        #plt.xlim(-0.06, 0.06)
        #plt.ylim((-0.5, 0.5))

        ax.scatter(0, 0, c="k", marker="s", s=10, zorder=10)
        # ax.legend(
        #     loc="upper left", handles=hndls, labels=labels, frameon=False, prop={"size": 15}
        # )
        #plt.title(r"${\rm 68\%\ Confidence\ Level\ Bounds}$", fontsize=15)


        return ax, hndls
        #plt.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/15_07/ellipse_zh_llbb_68.pdf')

def sample_loader(path):
    with open(path) as json_data:
        samples = json.load(json_data)
    df = pd.DataFrame(samples)
    return df

# path_to_nn = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/nn/mtt_y_high/posterior.json'
# #path_to_nn_3_feat = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/nn/3_feat/posterior.json'
# path_to_truth = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/truth/mtt_y/posterior.json'
# path_to_truth_3_feat = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/truth/3_feat/posterior.json'
# path_to_binned_fine = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/binned/fb/posterior.json'
# path_to_binned_coarse = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/tt/binned/mzh_y/posterior.json'

#df_nn = sample_loader(path_to_nn)
#df_nn_3_feat = sample_loader(path_to_nn_3_feat)
#df_truth = sample_loader(path_to_truth)
#df_truth_3_feat = sample_loader(path_to_truth_3_feat)
#df_binned_fine = sample_loader(path_to_binned_fine)
#df_binned_coarse = sample_loader(path_to_binned_coarse)

# tt parton level
#labels = [r'$\mathrm{Re}\:C_{tG}$', r'$C_{tu}^{(1)}$']

# zh_llbb
#
# path_to_nn = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/zh_llbb/nn_3/posterior.json'
# path_to_stxs = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/zh_llbb/binned/posterior.json'
# path_to_1bin = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/zh_llbb/binned/1/posterior.json'
# path_to_nn_pt = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/contours/zh_llbb/nn/pt/posterior.json'
# #
# ax_labels = [r'$C_{HW}$', r'$C_{bH}$']
# #ax_labels = [r'$\mathrm{Re}\:C_{tG}$', r'$C_{tu}^{(1)}$']
# #
# df_nn = sample_loader(path_to_nn)
# df_nn_pt = sample_loader(path_to_nn_pt)
# df_stxs = sample_loader(path_to_stxs)
# df_1bin = sample_loader(path_to_1bin)
#
# fig, ax = plt.subplots(figsize=(10,6))
# ax.hist(df_nn['cbhre'], bins=50)
# fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/15_07/test_cbhre_v2.pdf')
#
# plotter = EllipsePlotter()
# plotter.plot([df_stxs, df_1bin, df_nn_pt, df_nn], coeff1="chw", coeff2="cbhre", ax_labels=ax_labels,
#              labels=[r"$p_T^Z\in[75, 150, 250, 400, \infty)\:\mathrm{GeV}$", r"$\mathrm{Inclusive}$",
#                      r"$\mathrm{ML}\;\mathrm{model}\;(p_T^Z)$", r"$\mathrm{ML}\;\mathrm{model}\;(7\;\mathrm{features})$"])

# plotter.plot([df_nn, df_truth, df_binned_coarse], coeff1="ctgre", coeff2="cut", ax_labels=ax_labels,
#              labels=[r"$\mathrm{ML}\;\mathrm{model}\;(m_{t\bar{t}}, Y)$", r"$\mathrm{Analytical}\;(m_{t\bar{t}}, Y)$", r"$m_{t\bar{t}}\in[0.5, 1.0, \infty)\:\mathrm{TeV}$"])


#labels=[r"$\mathrm{NN}\;(9\;\mathrm{features})$", r"$\mathrm{STXS}\;\mathrm{Stage}\;1.2$", r"$1\;\mathrm{bin}$"]

#### GLOBAL #####

#df_nn_global = sample_loader('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/ns_glob/nn/posterior.json')




coeff_dict = {"cHu": r'$c_{\varphi u}$', "cHd": r'$c_{\varphi d}$', "cHj1": r'$c_{\varphi q}^{(1)}$', "cHj3": r'$c_{\varphi q}^{(3)}$',
              "cbHRe": r'$c_{b\varphi}$', "cHW": r'$c_{\varphi W}$', "cHWB": r'$c_{\varphi WB}$'}


n_cols = len(coeff_dict) - 1
n_rows = n_cols


fig = plt.figure(figsize=(n_cols * 4, n_rows * 4))

root_pt = "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/ns_pt_z/"
root_lin = "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/ns_lin"
root_quad = "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/ns_quad"
root_7 = "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/output/ns_7_feat/"


labels = [r"$p_T^Z\in[75, 150, 250, 400, \infty)\:\mathrm{GeV}:\mathrm{Quadratic}$", r"$\mathrm{ML}\;\mathrm{model}\;(p_T^Z):\mathrm{Quadratic}$"]#,
         # r"$p_T^Z\in[75, 150, 250, 400, \infty)\:\mathrm{GeV}:\mathrm{Quadratic}$", r"$\mathrm{ML}\;\mathrm{model}\;(p_T^Z):\mathrm{Quadratic}$"]
          #r"$\mathrm{ML}\;\mathrm{model}\;(7\;\mathrm{features})$", r"$\mathrm{ML}\;\mathrm{model}\;(7\;\mathrm{features}\;\mathrm{global})$"]
c1_old = "cHu"
i = n_cols * n_rows
j = 1
for (c1, c2) in itertools.combinations(coeff_dict.keys(), 2):
    if c1 != c1_old:
        i -= j
        j += 1
        c1_old = c1
    ax = plt.subplot(n_rows, n_cols, i)
    print(i, c1, c2)

    post_path_binned_lin = os.path.join(root_lin, 'binned', c1 + '_' + c2, 'posterior_{}_{}.json'.format(c1, c2))
    post_path_binned_quad = os.path.join(root_quad, 'binned', c1 + '_' + c2, 'posterior_{}_{}.json'.format(c1, c2))
    post_path_nn = os.path.join(root_pt, 'nn', c1 + '_' + c2, 'posterior_{}_{}.json'.format(c1, c2))
    post_path_nn_quad = os.path.join(root_quad, 'nn', c1 + '_' + c2, 'posterior_{}_{}.json'.format(c1, c2))

    #post_path_nn_7 = os.path.join(root_7, 'nn', c1 + '_' + c2, 'posterior_{}_{}.json'.format(c1, c2))


    #df_binned_lin = sample_loader(post_path_binned_lin)
    df_binned_quad = sample_loader(post_path_binned_quad)
    #df_nn = sample_loader(post_path_nn)
    df_nn_quad = sample_loader(post_path_nn_quad)
    #df_nn_7 = sample_loader(post_path_nn_7)
    plotter = EllipsePlotter()
    # ax, hndls = plotter.plot(ax, [df_binned, df_nn, df_nn_7, df_nn_global], coeff1=c2, coeff2=c1, labels=labels, ax_labels=[coeff_dict[c2], coeff_dict[c1]])
    # ax, hndls = plotter.plot(ax, [df_binned_lin, df_nn, df_binned_quad, df_nn_quad], coeff1=c2, coeff2=c1, labels=labels,
    #                          ax_labels=[coeff_dict[c2], coeff_dict[c1]])
    ax, hndls = plotter.plot(ax, [df_binned_quad, df_nn_quad], coeff1=c2, coeff2=c1,
                             labels=labels,
                             ax_labels=[coeff_dict[c2], coeff_dict[c1]])
    if j!=1:
        ax.set_xlabel('')
    if not (i == n_cols * n_rows + 1 - j * n_cols):
        ax.set_ylabel('')

    i -= 1

legend = fig.legend(
        labels=labels, handles=hndls,
        loc='upper center', frameon=False, fontsize=26)

bbox = legend.get_window_extent(fig.canvas.get_renderer()).transformed(fig.transFigure.inverted())

plt.tight_layout()

fig.savefig('/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/plots/2022/21_07/zh_particle_quad_only.pdf')
