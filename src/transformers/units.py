from pyspark.sql.functions import col, when, lit


def normalize_units(df, cfg):
    factor = cfg.unit_conversion.cs_to_st_multiplier

    df = df.withColumn(
        "cantidad_unidades",
        when(col("unidad") == "CS", col("cantidad") * lit(factor))
        .when(col("unidad") == "ST", col("cantidad"))
        .otherwise(lit(None))
    )

    df = df.withColumn("unidad_std", lit("ST"))

    return df
