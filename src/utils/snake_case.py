import re

def to_snake_case(name: str) -> str:
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", name)
    return name.lower()

def snake_case(df):
    for c in df.columns:
        df = df.withColumnRenamed(c, to_snake_case(c))
    return df
