import matplotlib
from matplotlib import pyplot as plt
from matplotlib import rc
import numpy as np
import torch
import json
import sys
import os
import matplotlib.gridspec as gridspec

# import own pacakges
from quad_classifier_cluster import Predictor_quadratic
import xsec_cluster as ExS

matplotlib.use('PDF')
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica'], 'size': 22})
rc('text', usetex=True)

eft_points = [[-10.0, 0], [-5.0, 0], [-1.0, 0], [1.0, 0], [5.0, 0], [10.0, 0], [0, -2.0], [0, -1.0], [0, -0.5],[0, 0.5], [0, 1.0], [0, 2.0], [-10.0, -2.0], [-5.0, -1.0], [-1.0, -0.5], [1.0, 0.5], [5.0, 1.0],[10.0, 2.0]]


def make_predictions_1d(network_path, network_size, ctg, cuu, mean, std):
    """
    :param network_path: path to the saved NN to be loaded
    :param train_dataset: training data needed to find the mean and std
    :param ctg: value of the Wilson coefficient ctg
    :return: comparison between NN prediction and analytically known result for the likelihood ratio
    """

    # Be careful to use the same network architecture as during training
    loaded_model = Predictor_quadratic(network_size)
    loaded_model.load_state_dict(torch.load(network_path))

    # Set up coordinates and compute f
    mtt_min, mtt_max = 1000, 4000
    mtt = torch.arange(mtt_min, mtt_max, 10).unsqueeze(1)
    x = (mtt - mean) / std  # rescale the inputs

    f_pred = loaded_model.forward(x.float(), ctg, cuu)
    f_pred = f_pred.view(-1).detach().numpy()

    return mtt.numpy(), f_pred


def plot_predictions_1d(network_size):
    # animate_learning_1d(path, network_size, ctg, cuu, epochs, mean, std)



    # plt.legend([ana_plot, (nn_band_plot_1, nn_med_plot_1)], [r"$\rm{Theory}$", r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{50K}$'])

    out_pdf = '/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/' + 'test.pdf'
    pdf = matplotlib.backends.backend_pdf.PdfPages(out_pdf)

    ################
    nrows = 6
    ncols = 3
    mtt_min, mtt_max = 1000, 4000
    fig = plt.figure(figsize=(ncols*10, nrows*6))
    outer = gridspec.GridSpec(6, 3, wspace=0.2, hspace=0.3)

    for i in range(18):
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
        f_pred_std_1 = np.std(f_pred, axis=0)

        f_pred = []
        for ii in range(1, mc_runs + 1):
            pred_path = '/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/trained_nn/run_8/mc_run_{}'.format(ii)
            mean, std = np.loadtxt(pred_path + '/scaling.dat')
            mtt, f_pred_i = make_predictions_1d(pred_path + '/trained_nn.pt', network_size, ctg, cuu, mean, std)
            f_pred.append(f_pred_i)

        f_pred = np.array(f_pred)
        f_pred_median_2 = np.median(f_pred, axis=0)
        f_pred_std_2 = np.std(f_pred, axis=0)

        for j in range(2):
            if j == 0:
                ax = fig.add_subplot(inner[0:-1, :])
                ax.set_xticks([])




                # Plot the NN prediction
                nn_med_plot_1, = ax.plot(mtt[:, 0], f_pred_median_1, '--', linewidth=0.75)
                ax.plot(mtt[:, 0], f_pred_median_1 + 2 * f_pred_std_1, color='C0', linewidth=0.75)
                ax.plot(mtt[:, 0], f_pred_median_1 - 2 * f_pred_std_1, color='C0', linewidth=0.75)
                nn_band_plot_1 = ax.fill_between(mtt[:, 0], f_pred_median_1 - 2 * f_pred_std_1,
                                                 f_pred_median_1 + 2 * f_pred_std_1,
                                                 alpha=0.3)


                # Plot the NN prediction
                nn_med_plot_2, = ax.plot(mtt[:, 0], f_pred_median_2, '--', linewidth=0.75)
                ax.plot(mtt[:, 0], f_pred_median_2 + 2 * f_pred_std_2, color='C1', linewidth=0.75)
                ax.plot(mtt[:, 0], f_pred_median_2 - 2 * f_pred_std_2, color='C1', linewidth=0.75)
                nn_band_plot_2 = ax.fill_between(mtt[:, 0], f_pred_median_2 - 2 * f_pred_std_2,
                                                 f_pred_median_2 + 2 * f_pred_std_2,
                                                 alpha=0.3)

                x, y = ExS.plot_likelihood_ratio_1D(mtt_min * 10 ** -3, mtt_max * 10 ** -3, ctg, cuu)
                x = np.array(x)
                y = np.array(y)
                ana_plot, = ax.plot(x * 1e3, y, color='red', linewidth=0.75)

                plt.ylabel(r'$f\;(m_{tt}, c)$')
                # plt.xlabel(r'$m_{tt}\;[GeV]$')
                plt.xlim((mtt_min, mtt_max))
                plt.ylim((0, 1))
                plt.title(
                    r'$\rm{NN\:versus\:analytical\:at\:cuu}$' + r'$\:={}$'.format(
                        cuu) + r'$\rm{\:and\:ctg}$' + r'$\:={}$'.format(
                        ctg))
                # plt.legend([ana_plot, (nn_band_plot_1, nn_med_plot_1), (nn_band_plot_2, nn_med_plot_2), (nn_band_plot_3, nn_med_plot_3)], [r"$\rm{Theory}$", r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{50K}$', r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{100K}$', r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{20K}$'])
                plt.legend([ana_plot, (nn_band_plot_1, nn_med_plot_1), (nn_band_plot_2, nn_med_plot_2)],
                           [r"$\rm{Theory}$", r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{\:50K}$',
                            r'$\rm{NN\:(Median\:}$' + r'$+\:2\sigma)$' + r'$\rm{\:100K}$'])

            if j == 1: #data versus theory
                ax = fig.add_subplot(inner[-1, :])

                ax.plot(x * 1e3, (y - f_pred_median_2) / f_pred_std_2)
                #ax.plot(x * 1e3, y / f_pred_median_1, color='C0')
                #ax.plot(x * 1e3, y / f_pred_median_2, color='C1')
                #ax.hlines(1, mtt_min, mtt_max, linestyles='dashed', colors='black')
                plt.xlabel(r'$m_{tt}\;[\mathrm{GeV}]$')
                #plt.ylabel(r'$\rm{theory/model}$')
                plt.ylabel(r'$\rm{pull}$')
                plt.xlim((mtt_min, mtt_max))
                #plt.ylim((0.9*(y / f_pred_median_1).min(), 1.1*(y / f_pred_median_1).max()))
                plt.ylim((1.2 * np.min((y - f_pred_median_2) / f_pred_std_2),
                          1.2 * np.max((y - f_pred_median_2) / f_pred_std_2)))
                # fig.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/' + 'pull_v2.pdf')










            fig.add_subplot(ax)
    #     if i%6 == 0:
    #         pdf.savefig(fig)
    # pdf.close()
    fig.savefig('/data/theorie/jthoeve/ML4EFT/quad_clas/qc_results/' + 'test_pull.pdf')


def get_predictions_1d(network_path, network_size, mtt, ctg, cuu, mean, std):
    loaded_model = Predictor_quadratic(network_size)
    loaded_model.load_state_dict(torch.load(network_path))
    x = (mtt * 10**3 - mean) / std  # rescale the inputs
    x = torch.tensor([x])
    f_pred = loaded_model.forward(x.float(), ctg, cuu)
    f_pred = f_pred.detach().numpy()
    return f_pred


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

    theory = 1 / (1 + ExS.likelihood_ratio_1D_v(mtt, ctg.numpy(), cuu.numpy()))
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

if __name__ == '__main__':
    with open(sys.argv[1]) as json_data:
        run_dict = json.load(json_data)

    trained = run_dict['trained']
    quadratic = run_dict['quadratic']
    n_dat = run_dict['n_dat']
    epochs = run_dict['epochs']
    ctg = run_dict['coeff'][0]['value']
    cuu = run_dict['coeff'][1]['value']
    network_size = [run_dict['input_size']] + run_dict['hidden_sizes'] + [run_dict['output_size']]

    #pull = get_pull(network_size, torch.tensor([0]), torch.tensor([1]))
    #print(pull)
    plot_pull_heatmap(network_size, [1.50, 1.80, 2.10, 2.40, 3.00, 3.50])



    #plot_predictions_1d(network_size)