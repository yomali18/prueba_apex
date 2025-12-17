from pyspark.sql.functions import col

def apply_execution_filters(df, cfg):
    return df.filter(
        (col(cfg.date_range.date_column) >= cfg.date_range.start_date) &
        (col(cfg.date_range.date_column) <= cfg.date_range.end_date) &
        (col("pais") == cfg.filters.country)
    )
