from pyspark.sql.functions import col

def enrich_metrics(df):
    return (
        df
        .withColumn("total_value", col("cantidad_unidades") * col("precio"))
    )
