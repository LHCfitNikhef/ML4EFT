import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import rc
import numpy as np
import torch
import sys
import copy
import matplotlib.gridspec as gridspec
from matplotlib import animation
import os

# import own pacakges
from . import quad_classifier_cluster as quad_clas
from quad_clas.core.xsec import tt_prod as axs
from quad_clas.core.xsec import vh_prod

#matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': 22})
rc('text', usetex=True)


def likelihood_ratio_truth(x, c, lin=False, quad=False):
    """
    Compute the 1D analytic likelihood ratio r(x, c)

    Parameters
    ----------
    x : numpy.ndarray, shape=(M, N)
        Kinematics feature vector with M instances of N kinematics, e.g. N =2 for
        the invariant mass and the rapidity.
    c : numpy.ndarray, shape=(M,)
        EFT point in M dimensions, e.g c = (cHW, cHq3)
    lin: bool, optional
        Set to False by default. Turn on for linear corrections.
    quad: bool, optional
        Set to False by default. Turn on for quadratic corrections.
    """

    n_kin = x.shape[1]
    cHW, cHq3 = c

    if n_kin == 1:
        dsigma_0 = [vh_prod.dsigma_dmvh(x_i, cHW, cHq3, lin=lin, quad=quad) for x_i in x]  # EFT
        dsigma_1 = [vh_prod.dsigma_dmvh(x_i, 0, 0, lin=lin, quad=quad) for x_i in x]  # SM
    elif n_kin == 2:
        dsigma_0 = [vh_prod.dsigma_dmvh_dy(y, mvh, cHW, cHq3, lin=lin, quad=quad) for (mvh, y) in x]  # EFT
        dsigma_1 = [vh_prod.dsigma_dmvh_dy(y, mvh, 0, 0, lin=lin, quad=quad) for (mvh, y) in x]  # SM
    else:
        raise NotImplementedError("No more than two features are currently supported")

    dsigma_0, dsigma_1 = np.array(dsigma_0), np.array(dsigma_1)

    ratio = np.divide(dsigma_0, dsigma_1, out=np.zeros_like(dsigma_0), where=dsigma_1 != 0)
    #ratio = dsigma_0 / dsigma_1

    return ratio.flatten()

def decision_function_truth(x, c, lin=False, quad=False):
    ratio = likelihood_ratio_truth(x, c, lin, quad)
    return 1 / (1 + ratio)

def likelihood_ratio_nn(x, c, path_to_models, architecture, mc_run, lin=False, quad=False):
    """

    Parameters
    ----------
    x : numpy.ndarray, shape=(M, N)
        Kinematics feature vector with M instances of N kinematics, e.g. N =2 for
        the invariant mass and the rapidity.
    c : numpy.ndarray, shape=(M,)
        EFT point in M dimensions, e.g c = (cHW, cHq3)
    path_to_models: dict
        Path to the nn model root directory
    mc_run: int
        Monte Carlo replica number
    lin: bool, optional
        Set to False by default. Turn on for linear corrections.
    quad: bool, optional
        Set to False by default. Turn on for quadratic corrections.

    Returns
    -------

    """
    cHW, cHq3 = c

    path_nn_lin = path_to_models['lin'] # shape = (len(c), )
    # path_nn_quad = path_to_models['quad'] # shape = (len(c), )
    # path_nn_cross = path_to_models['cross'] # TODO: shape

    with torch.no_grad():

        n_lin_1 = quad_clas.PredictorLinear(architecture)

        path_nn_lin_1 = os.path.join(path_nn_lin[0], 'mc_run_{}', 'trained_nn.pt')
        n_lin_1.load_state_dict(torch.load(path_nn_lin_1.format(mc_run)))
        mean, std = np.loadtxt(os.path.join(path_nn_lin[0], 'mc_run_{}'.format(mc_run), 'scaling.dat'))

        x_scaled = (x - mean) / std
        n_lin_1_out = n_lin_1.n_alpha(x_scaled.float())

        #######

        # n_lin_2 = quad_clas.PredictorLinear(architecture)
        #
        # path_nn_lin_2 = os.path.join(path_nn_lin[1], 'mc_run_{}', 'trained_nn.pt')
        # n_lin_2.load_state_dict(torch.load(path_nn_lin_1.format(mc_run)))
        # mean, std = np.loadtxt(os.path.join(path_nn_lin[1], 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        #
        # x_scaled = (x - mean) / std
        # n_lin_2_out = n_lin_2.n_alpha(x_scaled.float())

        ########

        # n_quad_1 = PredictorQuadratic(architecture)
        # n_quad_1.load_state_dict(torch.load(path_nn_quad_1.format(mc_run)))
        #
        # mean, std = np.loadtxt(os.path.join(path_quad_1, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        # x_scaled = (x - mean) / std
        # n_quad_1_out = n_quad_1.n_beta(x_scaled.float()) ** 2
        #
        # #######
        #
        # n_quad_2 = PredictorQuadratic(architecture)
        # n_quad_2.load_state_dict(torch.load(path_nn_quad_2.format(mc_run)))
        #
        # mean, std = np.loadtxt(os.path.join(path_quad_2, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        # x_scaled = (x - mean) / std
        # n_quad_2_out = n_quad_2.n_beta(x_scaled.float()) ** 2
        #
        # #######
        #
        # n_cross = PredictorCross(architecture)
        # n_cross.load_state_dict(torch.load(path_nn_cross.format(mc_run)))
        #
        # mean, std = np.loadtxt(os.path.join(path_cross, 'mc_run_{}'.format(mc_run), 'scaling.dat'))
        # x_scaled = (x - mean) / std
        # n_cross_out = n_cross.n_gamma(x_scaled.float()) ** 2

    #r = 1 + c1 * n_lin_1_out + c2 * n_lin_2_out #+ c1 ** 2 * n_quad_1_out + c2 ** 2 * n_quad_2_out + c1 * c2 * n_cross_out

    r = 1 + cHW * n_lin_1_out #+ cHq3 * n_lin_2_out

    return r

def decision_function_nn(x, c, mc_run, lin=False, quad=False):
    ratio = likelihood_ratio_nn(x, c, lin, quad)
    return 1 / (1 + ratio)

def plot_heatmap(im, xlabel, ylabel, title, extent, cmap='GnBu', vmin=None, vmax=None):

    # discrete colorbar
    cmap_copy = copy.copy(mpl.cm.get_cmap(cmap))
    bounds = [0.95, 0.96, 0.97, 0.98, 0.99, 1.01, 1.02, 1.03, 1.04, 1.05]
    norm = mpl.colors.BoundaryNorm(bounds, cmap_copy.N, extend='both')
    cmap_copy.set_under("#fc8c03")
    cmap_copy.set_over("#fac05c")

    # continious colormap

    # cmap = copy.copy(plt.get_cmap(cmap))
    # cmap.set_bad(color='white')
    # cmap.set_over("#FFAF33")
    # cmap.set_under("#FFAF33")

    fig, ax = plt.subplots(figsize=(8, 7))
    heatmap = ax.imshow(im, extent=extent,
                   origin='lower', cmap=cmap_copy, aspect=(extent[1] - extent[0]) / (extent[-1] - extent[-2]), norm=norm)

    if vmin == 0:

        cbar = fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap_copy),
                     ax=ax, shrink=0.9)

        #cbar = fig.colorbar(heatmap, ax=ax, shrink=0.9, extend='max')
    else:
        #cbar = fig.colorbar(heatmap, ax=ax, shrink=0.9, extend='both')

        cbar = fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap_copy),
                     ax=ax, shrink=0.9)

    cbar.minorticks_on()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    return fig

def coeff_comp_rep(path_model, network_size, c1, c2):

    s = 14 ** 2
    mvh_min, mvh_max = 0.3, 2
    y_min, y_max = - np.log(np.sqrt(s) / mvh_min), np.log(np.sqrt(s) / mvh_min)

    x_spacing, y_spacing = 1e-2, 0.01
    mvh_span = np.arange(mvh_min, mvh_max, x_spacing)
    y_span = np.arange(y_min, y_max, y_spacing)

    mvh_grid, y_grid = np.meshgrid(mvh_span, y_span)
    grid = np.c_[mvh_grid.ravel(), y_grid.ravel()]
    grid_unscaled_tensor = torch.Tensor(grid)

    # truth
    if c1 != 0:
        ratio_truth_c1 = likelihood_ratio_truth(grid, np.array([10, 0]), lin=True)
        mask = ratio_truth_c1 == 0
        coeff_truth = np.ma.masked_where(mask, (ratio_truth_c1 - 1) / 10)
        coeff_truth = coeff_truth.reshape(mvh_grid.shape)
        title = r'$n_1^{\rm{truth}}/n_1^{\rm{NN}}\;\rm{(median)}$'
    elif c2 != 0:
        ratio_truth_c2 = likelihood_ratio_truth(grid, np.array([0, 10]), lin=True)
        mask = ratio_truth_c2 == 0
        coeff_truth = np.ma.masked_where(mask, (ratio_truth_c2 - 1) / 10)
        coeff_truth = coeff_truth.reshape(mvh_grid.shape)
        title = r'$n_2^{\rm{truth}}/n_2^{\rm{NN}}\;\rm{(median)}$'
    else:
        loggin.info("c1 and c2 cannot both be zero.")

    # models

    mean, std = np.loadtxt(os.path.join(path_model, 'scaling.dat'))
    loaded_model = quad_clas.PredictorLinear(network_size)
    network_path = os.path.join(path_model, 'trained_nn.pt')

    # load all the parameters into the trained network
    loaded_model.load_state_dict(torch.load(network_path))
    grid = (grid_unscaled_tensor - mean) / std

    coeff_nn = loaded_model.n_alpha(grid.float())
    coeff_nn = coeff_nn.view(mvh_grid.shape).detach().numpy()


    fig = plot_heatmap(coeff_truth/coeff_nn,
                        xlabel=r'$m_{ZH}\;\rm{[TeV]}$',
                        ylabel=r'$\rm{Rapidity}$',
                        title=title,
                        extent=[mvh_min, mvh_max, y_min, y_max],
                        cmap='seismic',
                        vmin=0.95,
                        vmax=1.05)

    return fig

def coeff_comp(path_sm_data):
    s = 14 ** 2
    epsilon = 1e-2
    mvh_min, mvh_max = mz + mh + epsilon, 2
    y_min, y_max = - np.log(np.sqrt(s) / mvh_min), np.log(np.sqrt(s) / mvh_min)

    x_spacing, y_spacing = 1e-2, 0.01
    mvh_span = np.arange(mvh_min, mvh_max, x_spacing)
    y_span = np.arange(y_min, y_max, y_spacing)

    mvh_grid, y_grid = np.meshgrid(mvh_span, y_span)
    grid = np.c_[mvh_grid.ravel(), y_grid.ravel()]
    grid_unscaled_tensor = torch.Tensor(grid)

    # truth
    ratio_truth_c1 = analysis.likelihood_ratio_truth(grid, np.array([10, 0]), lin=True)
    ratio_truth_c2 = analysis.likelihood_ratio_truth(grid, np.array([0, 10]), lin=True)
    mask = ratio_truth_c1 == 0

    n_alpha_truth = np.ma.masked_where(mask, (ratio_truth_c1 - 1) / 10)
    n_alpha_truth = n_alpha_truth.reshape(mvh_grid.shape)

    n_beta_truth = np.ma.masked_where(mask, (ratio_truth_c2 - 1) / 10)
    n_beta_truth = n_beta_truth.reshape(mvh_grid.shape)

    # models

    network_size = [2, 30, 30, 30, 30, 30, 1]
    model_dir = '/data/theorie/jthoeve/ML4EFT_higgs/models/17_11/model_final_lin_cHW/mc_run_{mc_run}'
    # model_dir = '/data/theorie/jthoeve/ML4EFT_higgs/models/model_test/mc_run_{mc_run}'

    n_betas = []
    mc_runs = 30
    for rep_nr in range(0, mc_runs):
        print(rep_nr)

        mean, std = np.loadtxt(os.path.join(model_dir.format(mc_run=rep_nr), 'scaling.dat'))
        loaded_model = quad_classifier_cluster.PredictorLinear(network_size)
        network_path = os.path.join(model_dir.format(mc_run=rep_nr), 'trained_nn.pt')

        # load all the parameters into the trained network
        loaded_model.load_state_dict(torch.load(network_path))
        grid = (grid_unscaled_tensor - mean) / std

        n_beta = loaded_model.n_alpha(grid.float())
        n_beta = n_beta.view(mvh_grid.shape).detach().numpy()

        n_betas.append(n_beta)

    n_betas = np.array(n_betas)
    n_beta_median = np.percentile(n_betas, 50, axis=0)
    n_beta_high = np.percentile(n_betas, 84, axis=0)
    n_beta_low = np.percentile(n_betas, 16, axis=0)
    n_beta_unc = (n_beta_high - n_beta_low) / 2

    # visualise sm events
    if path_sm_data is not None:
        path_dict_sm = {0: path_sm_data}
        data_sm = quad_classifier_cluster.EventDataset(c=0,
                                                       n_features=2,
                                                       path_dict=path_dict_sm,
                                                       n_dat=500,
                                                       hypothesis=1)
        sm_events = data_sm.events.numpy()
    else:
        sm_events = None

    # median
    fig1 = plot_heatmap(n_alpha_truth / n_beta_median,
                        xlabel=r'$m_{ZH}\;\rm{[TeV]}$',
                        ylabel=r'$\rm{Rapidity}$',
                        title=r'$n_1^{\rm{truth}}/n_1^{\rm{NN}}\;\rm{(median)}$',
                        extent=[mvh_min, mvh_max, y_min, y_max],
                        cmap='seismic',
                        bounds=[0.95, 0.96, 0.97, 0.98, 0.99, 1.01, 1.02, 1.03, 1.04, 1.05])

    fig1.savefig('/data/theorie/jthoeve/ML4EFT_higgs/plots/17_11/n_beta_ratio_v6.pdf')

    # pull
    fig2 = plot_heatmap((n_alpha_truth - n_beta_median) / n_beta_unc,
                        xlabel=r'$m_{ZH}\;\rm{[TeV]}$',
                        ylabel=r'$\rm{Rapidity}$',
                        title=r'$\rm{Pull}$',
                        extent=[mvh_min, mvh_max, y_min, y_max],
                        cmap='seismic',
                        bounds=np.linspace(-1.5, 1.5, 10))

    fig2.savefig('/data/theorie/jthoeve/ML4EFT_higgs/plots/17_11/n_beta_ratio_pull_v3.pdf')

def load_models(architecture, model_dir, model_nrs):
    """
    Load pretrained models

    Parameters
    ----------
    architecture: list
        Architecture of the models to be loaded
    model_dir: str
        Path to models
    model_nrs: numpy.ndarray, shape=(M, )
        Array of models numbers to be loaded

    Returns
    -------
    models: list
        list of pretrained model instances
    """

    models = []
    for rep_nr in model_nrs:

        # load statistics of pretrained models
        mean, std = np.loadtxt(os.path.join(model_dir.format(mc_run=rep_nr), 'scaling.dat'))
        loaded_model = quad_clas.PredictorLinear(architecture)
        network_path = os.path.join(model_dir.format(mc_run=rep_nr), 'trained_nn.pt')

        # load all the parameters into the trained network and save
        loaded_model.load_state_dict(torch.load(network_path))
        models.append([loaded_model, [mean, std]])

    return models

def point_by_point_comp(data, c, model_info):

    # load the models
    architecture, model_dir, model_nrs = model_info
    models = load_models(architecture, model_dir, model_nrs)

    for rep_nr in range(len(models)):
        model, [mean, std] = models[rep_nr]
        data_rescaled = (data - mean) / std
        n_alpha = model.n_alpha(data_rescaled)



def make_predictions_1d(x, network_path, network_size, cHW, cHq3, mean, std,
                        path_lin_1=None,
                        path_lin_2=None,
                        path_quad_1=None,
                        path_quad_2=None):

    # Set up coordinates and compute f
    x_unscaled = torch.from_numpy(x)
    #x_unscaled = torch.cat((x_unscaled, torch.zeros(len(x_unscaled), 1)), dim=1)
    x = (x_unscaled - mean) / std  # rescale the inputs

    # Be careful to use the same network architecture as during training

    if path_quad_1 is None:
        loaded_model = quad_clas.PredictorLinear(network_size)
        loaded_model.load_state_dict(torch.load(network_path))
        f_pred = loaded_model.forward(x.float(), cHW + cHq3)
    elif path_quad_2 is None:
        loaded_model = quad_clas.PredictorQuadratic(network_size)
        loaded_model.load_state_dict(torch.load(network_path))
        f_pred = loaded_model.forward(x.float(), cHW ** 2 + cHq3 ** 2, path_lin_1)
    else:
        loaded_model = quad_clas.PredictorCross(network_size)
        loaded_model.load_state_dict(torch.load(network_path))
        f_pred = loaded_model.forward(x.float(), cHW, cHq3, path_lin_1, path_lin_2, path_quad_1, path_quad_2)

    f_pred = f_pred.view(-1).detach().numpy()

    return f_pred


def plot_predictions_1d(network_size):
    # animate_learning_1d(path, network_size, ctg, cuu, epochs, mean, std)

    ################
    nrows = 6
    ncols = 3
    mtt_min, mtt_max = 1000, 4000
    fig = plt.figure(figsize=(ncols*10, nrows*6))
    outer = gridspec.GridSpec(6, 3, wspace=0.2, hspace=0.3)

    for i in range(18):
        # We use the gridspec package to display a grid of plots which in turn consist of 2 subplots
        inner = gridspec.GridSpecFromSubplotSpec(3, 1,
                                                 subplot_spec=outer[i], wspace=0.1, hspace=0.1)
        ctg, cuu = eft_points[i]

        mc_runs = 42
        f_pred = []
        for ii in range(1, mc_runs + 1):
            pred_path = '/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/trained_nn/run_7/mc_run_{}'.format(ii)
            mean, std = np.loadtxt(pred_path + '/scaling.dat')
            mtt, f_pred_i = make_predictions_1d(pred_path + '/trained_nn.pt', network_size, ctg, cuu, mean, std)
            f_pred.append(f_pred_i)

        f_pred = np.array(f_pred)
        f_pred_median_1 = np.median(f_pred, axis=0)
        f_pred_cl_low_1 = np.percentile(f_pred, 2.5, axis=0)
        f_pred_cl_high_1 = np.percentile(f_pred, 97.5, axis=0)
        #f_pred_std_1 = np.std(f_pred, axis=0)

        # repeat, but now for 100K data points (run 8)
        f_pred = []
        for ii in range(1, mc_runs + 1):
            pred_path = '/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/trained_nn/run_8/mc_run_{}'.format(ii)
            mean, std = np.loadtxt(pred_path + '/scaling.dat')
            mtt, f_pred_i = make_predictions_1d(pred_path + '/trained_nn.pt', network_size, ctg, cuu, mean, std)
            f_pred.append(f_pred_i)

        f_pred = np.array(f_pred)
        f_pred_median_2 = np.median(f_pred, axis=0)
        f_pred_cl_low_2 = np.percentile(f_pred, 2.5, axis=0)
        f_pred_cl_high_2 = np.percentile(f_pred, 97.5, axis=0)

        #f_pred_std_2 = np.std(f_pred, axis=0)

        for j in range(2):
            if j == 0: # the main subplot (error band)
                ax = fig.add_subplot(inner[0:-1, :])
                ax.set_xticks([])

                # Plot the NN prediction
                nn_med_plot_1, = ax.plot(mtt[:, 0], f_pred_median_1, '--', linewidth=0.75, color='C0')
                #ax.plot(mtt[:, 0], f_pred_cl_high_1, color='C0', linewidth=0.75)
                #ax.plot(mtt[:, 0], f_pred_cl_low_1, color='C0', linewidth=0.75)
                nn_band_plot_1 = ax.fill_between(mtt[:, 0], f_pred_cl_low_1, f_pred_cl_high_1,alpha=0.3, color='C0')

                # Plot the NN prediction
                nn_med_plot_2, = ax.plot(mtt[:, 0], f_pred_median_2, '--', linewidth=0.75, color='C1')
                #ax.plot(mtt[:, 0], f_pred_cl_high_2, color='C1', linewidth=0.75)
                #ax.plot(mtt[:, 0], f_pred_cl_low_2, color='C1', linewidth=0.75)
                nn_band_plot_2 = ax.fill_between(mtt[:, 0], f_pred_cl_low_2,f_pred_cl_high_2,alpha=0.3, color='C1')

                # Plot the analytical result
                x, y = axs.plot_likelihood_ratio_1D(mtt_min * 10 ** -3, mtt_max * 10 ** -3, ctg, cuu)
                x = np.array(x)
                y = np.array(y)
                ana_plot, = ax.plot(x * 1e3, y, color='red', linewidth=0.75)

                plt.ylabel(r'$f\;(m_{tt}, c)$')
                # plt.xlabel(r'$m_{tt}\;[GeV]$')
                plt.xlim((mtt_min, mtt_max))
                plt.ylim((0, 1))
                plt.title(
                    r'$\rm{cuu}$' + r'$\:={}$'.format(
                        cuu) + r'$\rm{\quad cug}$' + r'$\:={}$'.format(
                        ctg))
                # plt.legend([ana_plot, (nn_band_plot_1, nn_med_plot_1), (nn_band_plot_2, nn_med_plot_2), (nn_band_plot_3, nn_med_plot_3)], [r"$\rm{Theory}$", r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{50K}$', r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{100K}$', r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{20K}$'])
                # plt.legend([ana_plot, (nn_band_plot_1, nn_med_plot_1), (nn_band_plot_2, nn_med_plot_2)],
                #            [r"$\rm{Theory}$", r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{\:50K}$',
                #             r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{\:100K}$'], frameon=False, loc='best')

            if j == 1: # the second subplot (data versus theory)
                ax = fig.add_subplot(inner[-1, :])
                #ax.plot(x * 1e3, (y - f_pred_median_2) / f_pred_std_2)
                #ax.plot(x * 1e3, y / f_pred_median_1, color='C0')

                ax.fill_between(x * 1e3, y / f_pred_cl_low_1, y / f_pred_cl_high_1, alpha=0.3, color='C0')
                ax.fill_between(x * 1e3, y / f_pred_cl_low_2, y / f_pred_cl_high_2, alpha=0.3, color='C1')
                ax.plot(x * 1e3, y / f_pred_median_1, '--', color='C0')
                ax.plot(x * 1e3, y / f_pred_median_2, '--', color='C1')
                ax.hlines(1, mtt_min, mtt_max, linestyles='dashed', colors='black')
                plt.xlabel(r'$m_{tt}\;[\mathrm{GeV}]$')
                plt.ylabel(r'$\rm{theory/model}$')
                #plt.ylabel(r'$\rm{pull}$')
                plt.xlim((mtt_min, mtt_max))
                plt.ylim((0.9*(y / f_pred_median_1).min(), 1.1*(y / f_pred_median_1).max()))
                # plt.ylim((1.2 * np.min((y - f_pred_median_2) / f_pred_std_2),
                #           1.2 * np.max((y - f_pred_median_2) / f_pred_std_2)))

            fig.add_subplot(ax)

    lines = []
    labels = []
    for ax in fig.axes:
        Line, Label = ax.get_legend_handles_labels()
        # print(Label)
        lines.extend(Line)
        labels.extend(Label)
    fig.legend(lines, labels, loc='upper right')

    fig.savefig('/data/theorie/jthoeve/ML4EFT_v2/output/plots/nn_acc' + '/nn_acc.pdf')


def get_predictions_1d(network_path, network_size, mtt, ctg, cuu, mean, std):
    loaded_model = quad_clas.PredictorQuadratic(network_size)
    loaded_model.load_state_dict(torch.load(network_path))
    x = (mtt * 10**3 - mean) / std  # rescale the inputs
    x = torch.tensor([x])
    f_pred = loaded_model.forward(x.float(), ctg, cuu)
    f_pred = f_pred.detach().numpy()
    return f_pred


def get_likelihood_ratio_NN(network_path, network_size, mtt, ctg, cuu, mean, std):
    loaded_model = quad_clas.PredictorQuadratic(network_size)
    loaded_model.load_state_dict(torch.load(network_path))
    mtt = torch.from_numpy(mtt*10**3).unsqueeze(1)
    x = (mtt - mean) / std  # rescale the inputs
    #x = torch.tensor(x)
    f_pred = loaded_model.forward(x.float(), ctg, cuu)
    #f_pred = f_pred.detach().numpy()
    f_pred = f_pred.view(-1).detach().numpy()
    ratio = (1 - f_pred) / f_pred
    return ratio


def get_pull(network_size, ctg, cuu, mtt):
    mc_runs = 42

    f_pred = []
    for i in range(1, mc_runs + 1):
        pred_path = '/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/trained_nn/run_8/mc_run_{}'.format(i)
        mean, std = np.loadtxt(pred_path + '/scaling.dat')
        f_pred_i = get_predictions_1d(pred_path + '/trained_nn.pt', network_size, mtt, ctg, cuu, mean, std)
        f_pred.append(f_pred_i)

    f_pred = np.array(f_pred)
    f_pred_median = np.median(f_pred, axis=0)
    f_pred_std = np.std(f_pred, axis=0)

    theory = 1 / (1 + axs.likelihood_ratio_1D_v(mtt, ctg.numpy(), cuu.numpy()))
    pull = (theory - f_pred_median)/f_pred_std
    return pull


def plot_pull_heatmap(network_size,mtt):
    #plt.figure()


    ctg = np.arange(-10, 10, 0.5)
    cuu = np.arange(-2, 2, 0.1)
    # ctg = np.array([-2, -1, 1, 2])
    # cuu = np.array([-2, -1, 1, 2])
    ctg_grid, cuu_grid = np.meshgrid(ctg, cuu, indexing='xy')
    # pull = get_pull(network_size, torch.from_numpy(ctg_grid), torch.from_numpy(cuu_grid), mtt)


    #fig = plt.figure()
    #plt.imshow(pull, extent=[np.min(ctg), np.max(ctg), np.min(cuu), np.max(cuu)], origin='lower', cmap=plt.cm.summer,
    #           aspect=(np.max(ctg) - np.min(ctg)) / (cuu.max() - cuu.min()), interpolation='quadric')
    #plt.colorbar()
    #plt.xlabel(r'$\rm{ctg}$')
    #plt.ylabel(r'$\rm{cuu}$')
    #plt.title(r'$\rm{Pull\:heatmap\:at\:m_{tt}=\:}$' + r'${}$'.format(mtt) + r'$\:\mathrm{TeV}$')
    # fig.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/pull_heatmap.pdf')


    #################

    nrows = 3
    ncols = 2


    fig = plt.figure(figsize=(ncols * 10, nrows * 10))
    fig.subplots_adjust(hspace=0.4, wspace=0.4)
    for i in range(1, nrows*ncols+1):
        pull = get_pull(network_size, torch.from_numpy(ctg_grid), torch.from_numpy(cuu_grid), mtt[i-1])
        ax = fig.add_subplot(nrows, ncols, i)
        im = ax.imshow(pull, extent=[np.min(ctg), np.max(ctg), np.min(cuu), np.max(cuu)], origin='lower', cmap='RdBu', aspect=(np.max(ctg) - np.min(ctg)) / (cuu.max() - cuu.min()), interpolation='quadric', vmin=-1.0, vmax=1.0)
        cbar = fig.colorbar(im, ax=ax, extend='both', shrink=0.60)
        cbar.minorticks_on()


        #ax.colorbar()'
        #fig.colorbar(im, ax=ax)
        ax.set_xlabel(r'$\rm{ctg}$')
        ax.set_ylabel(r'$\rm{cuu}$')
        ax.set_title(r'$\rm{Pull\:at\:m_{tt}=\:}$' + r'${}$'.format(mtt[i-1]) + r'$\:\mathrm{TeV}$')
        fig.tight_layout()

    fig.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/pull_heatmap_v3.pdf')


def plot_predictions_2d(network_path, network_size, train_dataset, quadratic, ctg, cuu, epochs):
    """
    Plot several plots that gauge the performance of the NN
    :param network_path: p
    :param network_size: network architecture
    :param train_dataset:
    :param quadratic: Include Quadratic EFT (Boolean)
    :param ctg: Wilson coefficient (Float)
    :return:
    """

    #animate_learning_2d(path, network_size, train_dataset, quadratic, ctg, cuu, epochs)

    if quadratic:
        xx, yy, x_span, y_span, f_pred, n_alpha_nn, n_alpha_n_beta_nn, f_ana = make_predictions_2d(
            network_path + 'trained_nn.pt', network_size, train_dataset, quadratic, ctg, cuu, False)
    else:
        xx, yy, f_pred, n_alpha_nn, f_ana = make_predictions_2d(network_path + 'trained_nn.pt', network_size,
                                                                train_dataset, quadratic, ctg, cuu)

    mtt_min, mtt_max = 1000, 4000
    s = (14 * 10 ** 3) ** 2
    y_min, y_max = - np.log(np.sqrt(s) / mtt_min), np.log(np.sqrt(s) / mtt_min)

    # plot the nn prediction
    fig = plt.figure()
    plt.imshow(f_pred, extent=[mtt_min, mtt_max, y_min, y_max], origin='lower', cmap=plt.cm.Blues,
               aspect=(mtt_max - mtt_min) / (y_max - y_min), interpolation='quadric')
    plt.colorbar()
    plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    plt.ylabel('y')
    plt.title(r'$f\;(x, c)$' + ' at ctG = {}'.format(ctg))
    plt.show()
    fig.savefig(network_path + 'plots/f_nn.pdf')

    # plot the analytical result
    fig = plt.figure()
    # mask values outside the physical region
    # f_ana = np.where(f_ana == 1.0, -1.0, f_ana)
    f_ana = np.ma.masked_where(f_ana == 1.0, f_ana)
    cmap = copy.copy(plt.get_cmap("Blues"))  # Can be any colormap that you want after the cm
    cmap.set_bad(color='white')

    plt.imshow(f_ana, extent=[mtt_min, mtt_max, y_min, y_max], origin='lower', cmap=cmap,
               aspect=(mtt_max - mtt_min) / (y_max - y_min), interpolation='quadric')
    plt.colorbar()
    plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    plt.ylabel('y')
    plt.title(r'$f\;(x, c)$' + ' at ctG = {}'.format(ctg))
    plt.show()
    fig.savefig(network_path + 'plots/f_ana.pdf')

    # plot the ratio analytical/nn_prediction
    fig = plt.figure()
    cmap2 = copy.copy(plt.get_cmap("seismic"))
    cmap2.set_bad(color='#c8c9cc')
    f_comp = f_ana / f_pred
    plt.imshow(f_comp, extent=[mtt_min, mtt_max, y_min, y_max], origin='lower', cmap=cmap2, vmin=0.8, vmax=1.2,
               aspect=(mtt_max - mtt_min) / (y_max - y_min), interpolation='quadric')
    plt.colorbar()
    plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    plt.ylabel('y')
    plt.title('ratio at ctG = {}'.format(ctg))
    plt.show()
    fig.savefig(network_path + 'plots/f_comp.pdf')

    fig = plt.figure()
    mtt_index = np.where(x_span == 1100)[0][0]
    plt.plot(yy[:, mtt_index], f_pred[:, mtt_index], label='NN prediction')
    plt.plot(yy[:, mtt_index], f_ana[:, mtt_index], label='analytical')
    plt.xlabel('y')
    plt.legend()
    plt.show()


def make_predictions_2d(network_path, network_size, train_dataset, quadratic, ctg, cuu, make_animation):
    """
    :param network_path: path to the saved NN to be loaded
    :param train_dataset: training data needed to find the mean and std
    :param ctg: value of the Wilson coefficient ctg
    :return: comparison between NN prediction and analytically known result for the likelihood ratio
    """

    # Be careful to use the same network architecture as during training
    if quadratic:
        loaded_model = quad_clas.PredictorQuadratic(network_size)
    else:
        loaded_model = quad_clas.PredictorLinear(network_size)

    # load all the parameters into the trained network
    loaded_model.load_state_dict(torch.load(network_path))

    # Set up coordinates and compute f
    mtt_min, mtt_max = 1000.0, 4000.0
    s = (14 * 10 ** 3) ** 2
    y_min, y_max = - np.log(np.sqrt(s) / mtt_min), np.log(np.sqrt(s) / mtt_min)
    x_spacing, y_spacing = 10, 0.01
    x_span = np.arange(mtt_min, mtt_max, x_spacing)
    y_span = np.arange(y_min, y_max, y_spacing)
    xx, yy = np.meshgrid(x_span, y_span)
    grid = torch.Tensor(np.c_[xx.ravel(), yy.ravel()])
    # rescale the grid
    grid = (grid - train_dataset.mean) / train_dataset.std
    # grid = -1 + 2 / (train_dataset.max_value - train_dataset.min_value) * (grid - train_dataset.min_value)

    f_pred = loaded_model.forward(grid.float(), ctg)  # TODO: why .float() needed?
    f_pred = f_pred.view(xx.shape).detach().numpy()

    n_alpha = loaded_model.n_alpha(grid.float())
    n_alpha = n_alpha.view(xx.shape).detach().numpy()

    # if make_animation is true, don't compute the analytic prediction
    if make_animation and quadratic:
        n_beta = loaded_model.n_beta(grid.float())
        n_beta = n_beta.view(xx.shape).detach().numpy()
        n_alpha_n_beta = n_alpha ** 2 + n_beta ** 2
        return xx, yy, x_span, y_span, f_pred, n_alpha, n_alpha_n_beta

    f_ana = axs.plot_f_ana(mtt_min, mtt_max, y_min, y_max, x_spacing, y_spacing, ctg, cuu)

    if quadratic:
        n_beta = loaded_model.n_beta(grid.float())
        n_beta = n_beta.view(xx.shape).detach().numpy()
        n_alpha_n_beta = n_alpha ** 2 + n_beta ** 2
        return xx, yy, x_span, y_span, f_pred, n_alpha, n_alpha_n_beta, f_ana
    else:
        return xx, yy, f_pred, n_alpha, f_ana


def animate_learning_1d(path, network_size, ctg, cuu, epochs, mean, std):

    mtt_min, mtt_max = 0.3, 1.0
    # First set up the figure, the axis, and the plot element we want to animate
    fig, ax = plt.subplots(figsize=(1.1*10, 1.1*6))

    ax = plt.axes(ylim=(0, 1), xlim=(mtt_min, mtt_max))

    # Compute the analytic likelihood ratio and plot
    x, y = axs.plot_likelihood_ratio_1D(mtt_min, mtt_max, ctg, cuu)
    x = np.array(x)
    y = np.array(y)
    ax.plot(x, y, '--', c='red', label=r'$\rm{Truth}$')


    # matplotlib.use('agg')
    plt.ylabel(r'$f\;(m_{tt}, c)$')
    plt.xlabel(r'$m_{tt}\;[\mathrm{GeV}]$')
    #plt.xlim((mtt_min, mtt_max))
    plt.ylim((0, 1))
    #plt.title('NN versus analytical at ctg = {ctg} and cuu = {cuu}'.format(ctg=ctg, cuu=cuu))

    line, = ax.plot([], [], lw=2, label=r'$\rm{NN}$')
    epoch_text = ax.text(0.02, 0.92, '', transform=ax.transAxes, fontsize=15)
    loss_text = ax.text(0.02, 0.85, '', transform=ax.transAxes, fontsize=15)
    loss = np.loadtxt(path + 'loss.out')

    plt.legend(loc='upper right', fontsize=15, frameon=False)

    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        epoch_text.set_text('')
        loss_text.set_text('')
        return line, epoch_text, loss_text

    # animation function.  This is called sequentially
    def animate(i):
        print(i)
        _, f_pred = make_predictions_1d(path + 'trained_nn_{}.pt'.format(i + 1), network_size, ctg, cuu, mean, std)
        line.set_data(x, f_pred)
        epoch_text.set_text(r'$\rm{epoch\;%d}$'%i)
        loss_text.set_text(r'$\rm{loss\;=\;%.4f}$'%loss[i])
        return line, epoch_text, loss_text



    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=epochs, interval=200, blit=True)

    anim.save(path + 'animation/training_animation.gif')


def animate_learning_2d(path, network_size, train_dataset, quadratic, ctg, cuu, epochs):
    # stopping_point = int(glob.glob(path + "/trained_nn_*.pt", recursive=False)[0][-6:-3])
    # print(stopping_point)
    # sys.exit()

    with open(path + 'stopping.txt') as f:
        stopping_point = int(f.read())

    def reference():
        mtt_min, mtt_max = 1000.0, 4000.0
        s = (14 * 10 ** 3) ** 2
        reference.y_min, reference.y_max = - np.log(np.sqrt(s) / mtt_min), np.log(np.sqrt(s) / mtt_min)
        x_spacing = 10
        y_spacing = 0.01
        # First set up the figure, the axis, and the plot element we want to animate
        reference.f_ana = axs.plot_f_ana(mtt_min, mtt_max, reference.y_min, reference.y_max, x_spacing, y_spacing, ctg, cuu, np_order=2)
        reference.f_ana = np.ma.masked_where(reference.f_ana == 1.0, reference.f_ana)

    reference()

    cmap = copy.copy(plt.get_cmap("seismic"))
    cmap.set_bad(color='#c8c9cc')

    fig, ax = plt.subplots()
    img = plt.imshow(np.zeros(reference.f_ana.shape), extent=[1000.0, 4000.0, reference.y_min, reference.y_max],
                     origin='lower', cmap=cmap, aspect=(4000.0 - 1000.0) / (reference.y_max - reference.y_min),
                     interpolation='quadric', vmin=0.8, vmax=1.2)
    plt.colorbar()
    plt.xlabel(r'$m_{tt}\;\mathrm{[GeV]}$')
    plt.ylabel('Rapidity y')
    plt.title('NN performance at ctG = {}'.format(ctg))
    epoch_text = ax.text(0.70, 0.95, '', transform=ax.transAxes)
    loss_text = ax.text(0.70, 0.90, '', transform=ax.transAxes)
    loss = np.loadtxt(path + 'loss.out')

    # initialization function: plot the background of each frame
    def init():
        img.set_data(np.zeros(reference.f_ana.shape))
        epoch_text.set_text('')
        loss_text.set_text('')
        return img, epoch_text, loss_text

    # animation function.  This is called sequentially

    def animate(i):
        sys.stdout.write('\r')
        sys.stdout.flush()
        xx, yy, _, _, f_pred, n_alpha_nn, n_alpha_n_beta_nn = make_predictions_2d(
            path + 'trained_nn_{}.pt'.format(i + 1), network_size, train_dataset, quadratic, ctg, make_animation=True)
        img.set_array(reference.f_ana / f_pred)
        epoch_text.set_text('epoch = {}'.format(i))
        loss_text.set_text('loss = {:.4f}'.format(loss[i]))
        return img, epoch_text, loss_text

    # call the animator.  blit=True means only re-draw the parts that have changed.
    print("Creating the animation")
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=stopping_point, interval=200, blit=True)
    anim.save(path + 'animation/training_animation.gif')


def plot_mg5_ana_mtt(binWidth, mtt_max, cuGRe, cuu, path_to_file, save_path):
    """
    Create a plot that shows the mg5 histogram in m_tt on top of the analytical (exact) result.
    This allows for a visual cross-check of the analytical result.
    :param binWidth: binwidth in TeV
    :param mtt_max: maximum m_tt in TeV
    :param cuGRe: eft parameter cuGRe
    :param cuu: eft parameter cuu
    :param path_to_file: path to lhe file
    :param save_path: path where the plot should be stored
    """
    axs.plotData(binWidth, mtt_max, cuGRe, cuu, path_to_file, save_path)


def plot_xsec_ana(binWidth, mtt_max, cuGRe, cuu, path_to_file, save_path):
    """
    Create a plot that shows the mg5 histogram in m_tt on top of the analytical (exact) result.
    This allows for a visual cross-check of the analytical result.
    :param binWidth: binwidth in TeV
    :param mtt_max: maximum m_tt in TeV
    :param cuGRe: eft parameter cuGRe
    :param cuu: eft parameter cuu
    :param path_to_file: path to lhe file
    :param save_path: path where the plot should be stored
    """
    axs.plot_xsec_ana(binWidth, mtt_max, cuGRe, cuu, path_to_file, save_path)
