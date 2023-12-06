"""
This file is meant to make adjustments to existing
data for debugging purposes.

"""  

import pandas as pd
import pylhe
import ml4eft.preproc.lhe_reader as lhe

# SETTINGS
# location of .lhe input file
#lhe_loc = "/data/theorie/wgautier/wgautier/followup/sample_data/lhes/ctG/unweighted_events.lhe"
#lhe_loc = "/data/theorie/wgautier/wgautier/followup/sample_data/unweighted_events.lhe"
lhe_loc = "/data/theorie/jthoeve/ML4EFT_events/tt_sm/job10/Events/run_01/unweighted_events.lhe"

# location of .csv data samples
csv_loc_events = "/data/theorie/wgautier/wgautier/followup/sample_data/csv/unweighted_events/events.csv"
csv_loc_weights = "/data/theorie/wgautier/wgautier/followup/sample_data/csv/unweighted_events/weights_ctG.csv"
csv_loc_events = "/data/theorie/wgautier/wgautier/followup/sample_data/csv/unweighted_events/event_sm.csv"

# pickled files (final model input)
pkl_loc_events = "/data/theorie/wgautier/wgautier/followup/sample_data/separate_w_ev/events/tt_sm/events_1.pkl.gz"
#pkl_loc_weights = "/data/theorie/wgautier/wgautier/followup/sample_data/separate_w_ev/weights/tt_ctGRe/weights_1.pkl.gz"

def lhe_to_pandas(path_to_lhe):

	lhe_init = pylhe.read_lhe_init(path_to_lhe)

	xsec = 0
	for process in lhe_init['procInfo']:
		xsec += process['xSection']

	events = []
	weight_values = []

	for e in pylhe.read_lhe_with_attributes(path_to_lhe):
		# create particle instances
		for part in e.particles:
			if part.id == 6: # t
				t = lhe.Kinematics(part)

			elif part.id == -6: #tbar
				tbar = lhe.Kinematics(part)

		# create particle systems
		tt = t + tbar

		# append kinematics
		events.append([#t.get_pt() * 1e-3,
					   tt.get_inv_mass() * 1e-3,
					   tt.get_rapidity()])
		#weight_values.append([
	#				   e.weights['ctgre_0'],
	#					e.weights['ctgre_1']
	#				   ])

	# no cross-sec total needed anymore
	#events.insert(0, [xsec] * len(events[0]))
	columns_events = ['m_tt',
				'y']
	#columns_weights = ['-2.0',
	#			'2.0'
	#			]
	df_events = pd.DataFrame(events, columns=columns_events)
	#df_weights = pd.DataFrame(weight_values, columns=columns_weights)

	return df_events#, df_weights

#df_events, df_weights = lhe_to_pandas(lhe_loc)
df_events = lhe_to_pandas(lhe_loc)

df_events.to_csv(csv_loc_events, index=False)
#df_weights.to_csv(csv_loc_weights, index=False)
df_events.to_pickle(pkl_loc_events, compression='gzip')
#df_weights.to_pickle(pkl_loc_weights, compression='gzip')