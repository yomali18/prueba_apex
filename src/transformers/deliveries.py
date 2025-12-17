from pyspark.sql.functions import col, when, lit


def classify_deliveries(df, cfg):
    rutina = cfg.delivery_types.routine
    bono = cfg.delivery_types.bonus

    df = df.filter(col("tipo_entrega").isin(*(rutina + bono)))

    df = df.withColumn(
        "entrega_rutina_unidades",
        when(col("tipo_entrega").isin(*rutina), col("cantidad_unidades"))
        .otherwise(lit(0))
    )

    df = df.withColumn(
        "entrega_bonificacion_unidades",
        when(col("tipo_entrega").isin(*bono), col("cantidad_unidades"))
        .otherwise(lit(0))
    )

    return df
