import pylhe
import pandas as pd
import numpy as np
import sys, os
import subprocess
import ml4eft.preproc.lhe_reader as lhe

# event_dir = sys.argv[1]
# process = sys.argv[2]
# save_root = sys.argv[3]

def lhe_to_pandas(path_to_lhe):

    lhe_init = pylhe.read_lhe_init(path_to_lhe)

    xsec = 0
    for process in lhe_init['procInfo']:
        xsec += process['xSection']

    events = []

    for e in pylhe.read_lhe(path_to_lhe):
        # create particle instances
        for part in e.particles:
            if part.id == 6: # t
                t = lhe.Kinematics(part)

            elif part.id == -6: #tbar
                tbar = lhe.Kinematics(part)

        # create particle systems
        tt = t + tbar

        # append kinematics
        events.append([t.get_pt() * 1e-3,
                       tt.get_inv_mass() * 1e-3,
                       tt.get_rapidity()
                       ])

    events.insert(0, [xsec] * len(events[0]))
    df = pd.DataFrame(events, columns=['pt_t',
                                       'm_tt',
                                       'y'
                                       ])

    return df

df = lhe_to_pandas('/Users/jaco/Documents/PhD/MG5_aMC_v3_4_1/bin/positivity_test/Events/run_03/unweighted_events.lhe')
df2 = lhe_to_pandas('/Users/jaco/Documents/PhD/MG5_aMC_v3_4_1/bin/positivity_test/Events/run_02/unweighted_events.lhe')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df.iloc[1:, :]['m_tt'])
ax.hist(df2.iloc[1:, :]['m_tt'])
ax.set_yscale('log')
fig.savefig('/Users/jaco/Documents/ML4EFT/plots/test.pdf')

# rep_nr = 0
# if os.path.basename(event_dir).startswith(process) is True:
#
#     job_dirs = os.listdir(event_dir)
#
#     # loop over all jobs
#     for job in job_dirs:
#
#         run_path = os.path.join(event_dir, job, 'Events')
#
#         # exclude non-job directories
#         if not job.startswith('job'):
#             continue
#
#         # check for successful run
#         if len(os.listdir(run_path)) == 0:
#             continue
#         else:
#             run_nrs = [int(runs.split("_", 1)[-1]) for runs in os.listdir(run_path)]
#             run_nr_max = max(run_nrs)
#
#         # build lhe path
#         if run_nr_max < 10:
#             lhe_path = os.path.join(run_path, 'run_0{}'.format(run_nr_max), 'unweighted_events.lhe')
#         else:
#             lhe_path = os.path.join(run_path, 'run_{}'.format(run_nr_max), 'unweighted_events.lhe')
#
#         # extract .gz file if necessary
#         if os.path.isfile('{}.gz'.format(lhe_path)):
#             subprocess.run("gunzip {}.gz".format(lhe_path), shell=True)
#
#         # feed lhe file to pandas converter
#         df = lhe_to_pandas(lhe_path)
#
#         event_name = os.path.basename(event_dir)
#         save_dir = os.path.join(save_root, event_name)
#
#         if not os.path.exists(save_dir):
#             os.makedirs(save_dir)
#
#         df.to_pickle(os.path.join(save_dir, "events_{}.pkl.gz".format(rep_nr)), compression="infer")
#
#         rep_nr += 1
# else:
#     sys.exit()

