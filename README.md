# prueba_apex

Pipeline ETL desarrollado en PySpark para el procesamiento de datos de entregas de productos.  El flujo implementa buenas prácticas de ingeniería de datos: estandarización de columnas, control de calidad, filtrado parametrizado, transformación de unidades y generación de métricas.

---

## 📌 Requisitos

Antes de ejecutar el pipeline es necesario contar con:

- Python 3.9 o superior
- Apache Spark instalado y configurado (`spark-submit` disponible en PATH)
- Java 11 o 17
- Git

Instalar dependencias de Python:

```bash
pip install -r requirements.txt
```
---
## ⚙️ Configuración

La configuración del pipeline se define en un archivo YAML utilizando OmegaConf (`config/base.yaml`)

```yaml
paths:
  input_csv: data/raw/product_deliveries.csv
  output_base: data/processed

date_range:
  date_column: fecha_proceso
  start_date: 20250101
  end_date: 20250630

filters:
  country: PE
```
---
## ▶️ Run

El pipeline se ejecuta exclusivamente mediante el archivo `run_etl.py`

```bash
spark-submit run_etl.py \
  --start-date 20250101 \
  --end-date 20250630 \
  --country PE
```
 `country` puede tomar los valores de `EC` (Ecuador), `GT` (Guatemala), `HN` (Honduras), `JM` (Jamaica), `PE` (Perú), `SV` (El Salvador)

El rango global de la `fecha_proceso` es `20250114` hasta `20250602`. Por lo tanto, `start-date` y `end-date` deberia estar entre esas fechas.

Para facilitar la revisión del flujo y visualizar únicamente los outputs relevantes del ETL (esquemas, muestras de datos, métricas y reportes), el pipeline puede ejecutarse utilizando una configuración de logging reducida.

```bash
spark-submit \
  --conf "spark.driver.extraJavaOptions=-Dlog4j.configurationFile=log4j2.properties" \
  run_etl.py \
  --start-date 20250101 \
  --end-date 20250630 \
  --country PE
```


---
## 🗂️ Estructura 
El proyecto está organizado bajo un enfoque modular para facilitar mantenibilidad, escalabilidad y separación de responsabilidades dentro del flujo ETL. La siguiente estructura refleja los distintos componentes del pipeline, desde la configuración y validación de datos hasta la generación de salidas particionadas.

```text
.
├── README.md
├── requirements.txt
├── run_etl.py
├── log4j2.properties
├── config
│   └── base.yaml
├── data
│   ├── raw
│   │   └── product_deliveries.csv
│   └── processed
│       ├── pais=PE
│       │   └── fecha_proceso=20250114
│       │       └── part-00000.csv
│       └── pais=GT
│           └── fecha_proceso=20250513
│               └── part-00000.csv
├── docs
│   └── enunciado_prueba.pdf
├── logs
└── src
    ├── main.py
    ├── config
    ├── filters
    │   └── selection.py
    ├── io
    │   └── writer.py
    ├── transformers
    │   ├── units.py
    │   ├── deliveries.py
    │   └── enrichment.py
    ├── utils
    │   ├── initial_explore.py
    │   ├── reporting.py
    │   └── snake_case.py
    └── validators
        └── quality.py

