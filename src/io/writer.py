def write_output(df, cfg):
    output_path = cfg.paths.output_base

    (
        df
        .write
        .mode("overwrite")
        .partitionBy("pais", "fecha_proceso")
        .option("header", True)
        .csv(output_path)
    )

    return {
        "path": output_path,
        "rows": df.count(),
        "columns": len(df.columns)
    }


