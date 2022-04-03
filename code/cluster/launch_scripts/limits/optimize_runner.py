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

    runner = Optimize(config)
    runner.run_sampling()