import os
from ml4eft.analyse.analyse import Analyse


report_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/10/15/losses'
path_to_models_root = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/10/15/'
order = 'quad'

models_paths_dict = Analyse.build_path_dict(root=path_to_models_root,
                        order='quad',
                        prefix='model')

analyser = Analyse(models_paths_dict, order)

for c_name in analyser.path_to_models[order].keys():
    fig, train_losses = analyser.plot_loss_overview(c_name, order)
    fig.savefig(os.path.join(report_path, 'loss_{}_{}.pdf'.format(c_name, c_name)))


