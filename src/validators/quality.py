from pyspark.sql.functions import col

def apply_quality_rules(df):
    return df.filter(
        col("fecha_proceso").isNotNull() &                          #Excluir registros sin fechas
        col("pais").isNotNull() &                                   #Excluir registros sin data en pais
        col("precio").isNotNull() & (col("precio") >= 0) &          #Excluir registros sin precio o >=0
        col("cantidad").isNotNull() & (col("cantidad") > 0)         #Excluir registros que tengan como cantidad 0
    )
