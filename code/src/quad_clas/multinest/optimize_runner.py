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
    runner = Optimize(args.fit_cards)
    runner.run_sampling()