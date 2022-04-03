import argparse
import json
import pandas as pd
import numpy as np
from quad_clas.core.th_predictions import TheoryPred
from quad_clas.limits.optimize_ns import Optimize

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--fit_cards",
        required=True,
        type=str,
        help="fit card"
    )

    args = parser.parse_args()

    with open(args.fit_cards) as json_data:
        config = json.load(json_data)

    # load theory predictions

    event_path = config['theory_pred_path']
    theory_pred = TheoryPred(coeff=['chw', 'chq3'],
                             event_path=event_path,
                             nreps=30)

    # load dataset (pseudo data)
    sm_data_path = config['observed_data_path']
    sm_data = pd.read_pickle(sm_data_path).iloc[1:, :]

    # construct observed dataset

    theory_pred_total = theory_pred.df.sum(axis=1)
    xsec_sm = theory_pred_total['sm']
    nu_tot_sm = xsec_sm * config['lumi']
    n_tot_sm = np.random.poisson(nu_tot_sm, 1)

    observed_data = sm_data.sample(int(n_tot_sm), random_state=1)

    runner = Optimize(config, observed_data, theory_pred)
    runner.run_sampling()