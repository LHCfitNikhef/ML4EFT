import pandas as pd

save_dir = "/data/theorie/pherbsch/ML4EFT/subproj/data/shower_data/sm_test"



df = pd.read_csv('output_pt_ll.csv')
df.to_pickle(os.path.join(save_dir, "events_0.pkl.gz".format(r)), compression="infer")