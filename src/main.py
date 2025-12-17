from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pprint import pprint

from src.utils.initial_explore import explore
from src.utils.reporting import generate_data_report
from src.utils.snake_case import snake_case

from src.validators.quality import apply_quality_rules
from src.filters.selection import apply_execution_filters

from src.transformers.units import normalize_units
from src.transformers.deliveries import classify_deliveries
from src.transformers.enrichment import enrich_metrics

from src.io.writer import write_output


def run_pipeline(cfg):

    spark = (
    SparkSession.builder
    .appName("product_delivery_etl")
    .config("spark.sql.sources.partitionOverwriteMode", "dynamic")
    .getOrCreate()
)


    # 1. Leer .csv
    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(cfg.paths.input_csv)
    )
    print("=== RAW DATA SAMPLE ===")
    df.show(5, truncate=False)
    print(f"Row count (raw): {df.count()}")
    print(f"Columns: {df.columns}")

    # 2. Nomenclatatura de columnas
    df = snake_case(df)

    # 3. Exploración inicial
    pre_profile = explore(df, stage="pre_filter")
    print("=== DATA EXPLORATION  ===")
    pprint(pre_profile)

    # 4. Control de calidad
    df = apply_quality_rules(df)

    # 5. Filtros (rango de fechas y con un solo país, anomalías)
    df = apply_execution_filters(df, cfg)

    # 6. Exploración post-filtros
    post_profile = explore(df, stage="post_filter")
    print("=== POST FILTERS  ===")
    pprint(post_profile)

    # 7. Transformar unidades
    df = normalize_units(df, cfg)

    # 8. Tipo de entrega - crear columnas 
    df = classify_deliveries(df, cfg)

    # 9. Otras metricas
    df = enrich_metrics(df)

    print("=== FINAL DATA ===")
    df.show(5, truncate=False)


    # 10. Generar data procesada
    out = write_output(df, cfg)

    print("=== DATA SAVED ===")
    print(out)

    
    spark.stop()