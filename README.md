# prueba_apex

Pipeline ETL desarrollado en PySpark para el procesamiento de datos de entregas de productos.  El flujo implementa buenas prácticas de ingeniería de datos: estandarización de columnas, control de calidad, filtrado parametrizado, transformación de unidades y generación de métricas.

---

## 📌 Objetivo

Procesar un dataset de entregas de productos aplicando:

- Validaciones de calidad de datos
- Filtros dinámicos por rango de fechas y país
- Normalización de unidades
- Clasificación de tipos de entrega
- Enriquecimiento de métricas
- Exportación particionada

---

## 🗂️ Estructura del proyecto
```text
.
├── config
│   └── base.yaml
├── data
│   ├── raw
│   │   └── product_deliveries.csv
│   └── processed
│       ├── pais=PE
│       │   └── fecha_proceso=20250114
│       └── pais=GT
│           └── fecha_proceso=20250513
├── src
│   ├── main.py
│   ├── transformers
│   ├── utils
│   └── validators
├── run_etl.py
├── requirements.txt
└── README.md
