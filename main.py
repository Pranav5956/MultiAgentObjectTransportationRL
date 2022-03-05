import argparse

from config import PROJECT_TITLE


def main() -> None:
    parser = argparse.ArgumentParser(
        description=PROJECT_TITLE)
    sub_parser = parser.add_subparsers(
        title="Mode", description="Run in \"training\" mode or \"inference\" mode.", dest="mode", help="modes")

    train_parser = sub_parser.add_parser("train", help="Run in training mode.")
    infer_parser = sub_parser.add_parser(
        "infer", help="Run in inference mode.")

    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
