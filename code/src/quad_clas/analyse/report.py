# this scripts produces the pdf plots for the training report

import numpy as np
import quad_clas.analyse.analyse as analyse
import os
import pandas as pd
import json
from pandas import json_normalize
import re
import subprocess
import PyPDF2

path_to_models = {'lin': {
    'ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/08/model_ctgre_lin_v1',
    'ctgre': '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/models/tt/2022/06/08/model_ctgre_lin_v1'}}

path_to_runcard = os.path.join(path_to_models['lin']['ctgre'], 'mc_run_0/run_card.json')
report_path = os.path.join(path_to_models['lin']['ctgre'], 'report')
if not os.path.exists(report_path):
    os.makedirs(report_path)

# point by point comparison

# ttbar

sm_data_path = '/data/theorie/jthoeve/ML4EFT_jan/ML4EFT/training_data/tt/topU3l/sm/events_0.pkl.gz'

n_dat = 5000
events_sm = pd.read_pickle(sm_data_path).iloc[1:, :].sample(int(n_dat), random_state=1)
#events_sm = events_sm[(events_sm['m_tt'] < 0.5)]
luminosity = 5e3

fig_reps, fig_median = analyse.point_by_point_comp(
    events=events_sm,
    c=np.array([-2, 0]),
    path_to_models=path_to_models,
    c_train={
        "ctgre": -10.0,
        "cuu": 0
    },
    n_kin=2,
    process='tt',
    lin=True,
    quad=False,
    epoch=-1)


fig_reps.savefig(os.path.join(report_path, 'reps_pbp.pdf'))
fig_median.savefig(os.path.join(report_path, 'median_pbp.pdf'))

# decision function (1d)

fig_accuracy_1d = analyse.accuracy_1d(c=[-5,0],
                                      path_to_models=path_to_models,
                                      c_train={"ctgre": -10,"cuu_quad": 100.0},
                                      epoch=-1,
                                      lin=True,
                                      quad=False)

fig_accuracy_1d.savefig(os.path.join(report_path, 'decision_fct_1d.pdf'))

# performance heatmaps (2d)

heatmap_median, heatmap_pull = analyse.coeff_comp(
    path_to_models=path_to_models,
    c1=-10,
    c2=0,
    c_train={
        "ctgre": -10,
        "cuu_quad": 100.0
    },
    n_kin=2,
    process='tt',
    lin=True,
    quad=False,
    cross=False,
    path_sm_data=None)

heatmap_median.savefig(os.path.join(report_path, 'heatmap_med.pdf'))
heatmap_pull.savefig(os.path.join(report_path, 'heatmap_pull.pdf'))


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
    pdfs = ['my_report.pdf', 'median_pbp.pdf', 'reps_pbp.pdf', 'decision_fct_1d.pdf', 'heatmap_med.pdf', 'heatmap_pull.pdf']
    pdfs = [os.path.join(report_path, pdf_i) for pdf_i in pdfs]

    # output pdf file name
    output = os.path.join(report_path, 'training_report.pdf')

    # calling pdf merge function
    PDFmerge(pdfs=pdfs, output=output)


if __name__ == "__main__":
    # calling the main function
    main()