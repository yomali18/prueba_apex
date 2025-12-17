from pyspark.sql import functions as F

def explore(df, stage: str):
    profile = {"stage": stage}

    cols = df.columns

    agg_exprs = [
        F.count("*").alias("row_count")
    ]

    if "fecha_proceso" in cols:
        agg_exprs.extend([
            F.min("fecha_proceso").alias("min_fecha_proceso"),
            F.max("fecha_proceso").alias("max_fecha_proceso"),
        ])

    null_exprs = [
        F.sum(F.col(c).isNull().cast("int")).alias(f"nulls_{c}")
        for c in cols
    ]

    agg = df.agg(*(agg_exprs + null_exprs)).collect()[0].asDict()

    profile["row_count"] = agg.pop("row_count")

    if "min_fecha_proceso" in agg:
        profile["date_range"] = {
            "min": agg.pop("min_fecha_proceso"),
            "max": agg.pop("max_fecha_proceso"),
        }
    else:
        profile["date_range"] = None

    profile["nulls"] = {
        k.replace("nulls_", ""): v
        for k, v in agg.items()
        if k.startswith("nulls_")
    }

    return profile

