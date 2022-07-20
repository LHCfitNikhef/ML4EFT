import numpy as np
import quad_clas.analyse.analyse as analyse
import os
import json
from pandas import json_normalize
import re
import pandas as pd
import subprocess
import PyPDF2
import sys

# generate report for
order = "lin"
c_name = "cHWB"

yr = "2022"
month = "07"
day = "15"
date = "{yr}_{m}_{d}".format(yr=yr, m=month, d=day)

name = "model_cbhre_lin"

# path_to_models = {'lin': {
#     'ctgre': [-10, '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctgre_lin'],
#     'cut': [10, '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctgre_quad']},
#     'quad': {'ctgre': [-10, '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctgre_quad'],
#              'cut': [10, '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/22/model_ctu1_quad']}}

# path_to_models = {
#     "lin": {"cbhre": [-20, "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/zh_llbb/2022/07/15/model_cbhre_lin"],
#             "chw": [50, "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/zh_llbb/2022/07/15/model_chw_lin"]}}

path_to_models = {
    "lin": {"cHu": [10, "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/zh_llbb/2022/07/19/model_cHu"],
    "cHd":  [-10, "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/zh_llbb/2022/07/19/model_cHd"],
    "cHj1":  [-10, "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/zh_llbb/2022/07/19/model_cHj1"],
    "cHj3":  [10, "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/zh_llbb/2022/07/19/model_cHj3"],
    "cbHRe":  [-10, "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/zh_llbb/2022/07/19/model_cbHRe"],
    "cHW":  [10, "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/zh_llbb/2022/07/19/model_cHW"],
    "cHWB":  [10, "/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/zh_llbb/2022/07/19/model_cHWB"]}}

path_to_runcard = os.path.join(path_to_models[order][c_name][-1], 'mc_run_0', 'run_card.json')

analyser = analyse.Analyse(path_to_models)
analyser.build_model_dict()

event_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/topU3l_mtt_05/sm/events_0.pkl.gz'
events_sm = pd.read_pickle(event_path)
events_sm = events_sm.iloc[1:,:]

#events_sm = events_sm[(events_sm['m_tt'] > 0.5)]
events_sm = events_sm.sample(5000, random_state=1)

model_dir = os.path.dirname(analyser.model_df.loc[order, c_name]['rep_paths'][0])
report_path = os.path.join(model_dir, 'report')
if not os.path.exists(report_path):
    os.makedirs(report_path)



# # pbp comparison
# fig1, fig2 = analyser.point_by_point_comp(events_sm, {'ctgre': -2, 'cut': 0}, ['y', 'm_tt'], 'tt', 'lin')
# fig1.savefig(os.path.join(report_path, 'pbp_rep.pdf'))
# fig2.savefig(os.path.join(report_path, 'pbp_med.pdf'))

# # loss overview
fig, losses = analyser.plot_loss_overview(c_name, order)
fig.savefig(os.path.join(report_path, 'loss_{}_{}.pdf'.format(c_name, order)))
sys.exit()
#fig.savefig(os.path.join(report_path, 'loss_overview.pdf'))

loss_ana = analyser.analytical_loss({'ctgre': 10, 'cut': 0},  ['y', 'm_tt'], 'tt', order)
fig = analyser.plot_loss_dist(losses, loss_ana)

fig.savefig(os.path.join(report_path, 'loss_dist.pdf'))


# 1d accuracy
fig = analyser.plot_accuracy_1d(c={'ctgre': -2, 'cut': 0}, process='tt', order='lin', cut=0.5, epoch=-1)
fig.savefig(os.path.join(report_path, '1d_accuracy.pdf'))

# heatmap med and pull
fig1, fig2 = analyser.accuracy_heatmap('ctgre', 'lin', 'tt', cut=0.5)
fig1.savefig(os.path.join(report_path, 'heatmap_med.pdf'))
fig2.savefig(os.path.join(report_path, 'heatmap_pull.pdf'))

# heatmap overview plot
fig = analyser.plot_heatmap_overview('ctgre', 'lin', 'tt', cut=0.5, reps=np.arange(20))
fig.savefig(os.path.join(report_path, 'heatmap_overview.pdf'))


L = [
    r"\documentclass{article}",
    r"\usepackage{float}",
    r"\usepackage{amsmath}",
    r"\usepackage{amssymb}",
    r"\usepackage{booktabs}",
    r"\usepackage[a4paper]{geometry}",
    r"\usepackage{array}",
    r"\usepackage{hyperref}",
    r"\usepackage{xcolor}",
    r"\usepackage{multirow}",
    r"\usepackage{pdflscape}",
    r"\allowdisplaybreaks",
    r"\newcolumntype{C}[1]{>{\centering\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}",
    r"\usepackage{graphicx}",
    r"\usepackage{tabularx}",
    r"\geometry{verbose, tmargin = 1.5cm, bmargin = 1.5cm, lmargin = 1cm, rmargin = 1cm}",
    r"\begin{document}"
]


with open(path_to_runcard) as json_data:
    dict = json.load(json_data)

df = json_normalize(dict, max_level=1).T

ch = '/ML4EFT'
# The Regex pattern to match al characters on and before '-'
pattern  = ".*" + ch
# Remove all characters before the character '-' from string
df.loc[['event_data']] = re.sub(pattern, '', df.loc[['event_data']][0].values[0])

df = df.drop('pretrained_models.lin')

df.loc['model_date'] = date
df[0] = [fr'\verb|{row}|' for row in df[0]]

df.rename(index=lambda s: fr'\verb|{s}|', inplace=True)

with pd.option_context("max_colwidth", 1000):
    with open(os.path.join(report_path, 'mytable.tex'), 'w') as tf:
        tf.write(df.to_latex(index=True, header=False, column_format='l|r', caption='Training settings', longtable=False, escape=False,
                             bold_rows=False))

json_tex_path = os.path.join(report_path, 'mytable.tex')
L.append("\input{" + json_tex_path + "}")
L.append(r"\end{document}")

L = [l + "\n" for l in L]
latex_src = os.path.join(report_path, "my_report.tex")
with open(latex_src, "w") as file:
    file.writelines(L)

file.close()
subprocess.call(
    f"pdflatex -halt-on-error -output-directory {report_path} {latex_src}", shell=True
)

subprocess.call(f"rm {report_path}/*.log {report_path}/*.aux {report_path}/*.out", shell=True)


def PDFmerge(pdfs, output):
    # creating pdf file merger object
    pdfMerger = PyPDF2.PdfFileMerger()

    # appending pdfs one by one
    for pdf in pdfs:
        pdfMerger.append(pdf)

    # writing combined pdf to output pdf file
    with open(output, 'wb') as f:
        pdfMerger.write(f)


def main():
    # pdf files to merge
    pdfs = ['my_report.pdf', 'pbp_med.pdf', 'pbp_rep.pdf', 'loss_overview.pdf', '1d_accuracy.pdf', 'heatmap_med.pdf',
            'heatmap_pull.pdf', 'heatmap_overview.pdf']
    pdfs = [os.path.join(report_path, pdf_i) for pdf_i in pdfs]

    # output pdf file name

    output = os.path.join(report_path, 'report_{date}_{model_name}_v2.pdf'.format(date=date, model_name=name))

    # calling pdf merge function
    PDFmerge(pdfs=pdfs, output=output)


if __name__ == "__main__":
    # calling the main function
    main()

