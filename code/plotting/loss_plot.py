import os
from ml4eft.analyse.analyse import Analyse


report_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt_llvlvlbb_pt_ll_eta_l_v7/2022/10/06/losses'
path_to_models_root = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt_llvlvlbb_pt_ll_eta_l_v7/2022/10/06'
order = 'lin'

models_paths_dict = Analyse.build_path_dict(root=path_to_models_root,
                        order='lin',
                        prefix='model')

analyser = Analyse(models_paths_dict, order)

for c_name in ["ctGRe"]:#analyser.path_to_models[order].keys():
    fig, train_losses = analyser.plot_loss_overview(c_name, order)
    fig.savefig(os.path.join(report_path, 'loss_{}.pdf'.format(c_name)))


