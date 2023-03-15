import argparse
import json
import pandas as pd
import numpy as np
from ml4eft.core.th_predictions import TheoryPred
from ml4eft.limits.optimize_ns import Optimize

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--fit_cards",
        required=True,
        type=str,
        help="fit card"
    )

    parser.add_argument(
        "-c",
        "--coeff",
        required=False,
        type=str,
        nargs = "*",
        help="subset of operators to include"
    )

    args = parser.parse_args()

    with open(args.fit_cards) as json_data:
        config = json.load(json_data)

    runner = Optimize(config, coeff=args.coeff)
    runner.run_sampling()