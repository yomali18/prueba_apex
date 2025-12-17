import os
import json
from datetime import datetime


def generate_data_report(cfg, pre_profile, post_profile, final_count):
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"reports/data_report_{timestamp}.json"

    report = {
        "execution_params": {
            "start_date": cfg.date_range.start_date,
            "end_date": cfg.date_range.end_date,
            "country": cfg.filters.country
        },
        "pre_filter_profile": pre_profile,
        "post_filter_profile": post_profile,
        "final_row_count": final_count
    }

    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)
