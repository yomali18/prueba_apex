import argparse
from omegaconf import OmegaConf
from src.main import run_pipeline


def parse_args():
    parser = argparse.ArgumentParser(description="Product Delivery ETL")
    parser.add_argument("--start-date", required=True, help="YYYYMMDD")
    parser.add_argument("--end-date", required=True, help="YYYYMMDD")
    parser.add_argument("--country", required=True, help="Country code")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    cfg = OmegaConf.load("config/base.yaml")

    cfg.date_range.start_date = args.start_date
    cfg.date_range.end_date = args.end_date
    cfg.filters.country = args.country

    run_pipeline(cfg)

