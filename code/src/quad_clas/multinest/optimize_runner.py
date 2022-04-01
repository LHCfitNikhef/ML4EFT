from ..core.th_predictions import TheoryPred
import argparse
from optimize_ns import Optimize

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

    # observed data

    theory_pred = TheoryPred(coeff=['cHW', 'cHq3'],
                             bins=[0, 4000],
                             kinematic='pt_z',
                             event_path='/data/theorie/jthoeve/training_data/zh/features_mzh_y_ptz_v2',
                             nreps=30)

    # load observed dataset (pseudo data)
    sm_data_path = '/data/theorie/jthoeve/training_data/zh/features_mzh_y_ptz_v2/sm/events_0.pkl.gz'
    events_sm = pd.read_pickle(sm_data_path).iloc[1:, :]

    import pdb; pdb.set_trace()

    runner = Optimize(args.fit_cards, events_sm)
    runner.run_sampling()