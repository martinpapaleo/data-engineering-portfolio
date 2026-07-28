# Sales Supermarket Data Pipeline

A modular batch ETL pipeline built with Python that transforms raw supermarket sales data into a clean, validated, and analytics-ready dataset.

This project demonstrates a typical Data Engineering workflow by separating ingestion, cleaning, transformation, validation, and persistence into independent modules. The modular architecture improves readability, maintainability, testability, and reproducibility.

---

## Overview

The pipeline performs the following tasks:

- Reads raw supermarket sales data from a CSV file
- Cleans and standardizes the dataset
- Creates additional analytical features
- Validates data quality
- Stores the processed dataset in Parquet format

The project focuses on clean software design and ETL best practices rather than exploratory analysis.

---

## Pipeline Architecture

```text
Raw CSV
   │
   ▼
Ingest
   │
   ▼
Clean
   │
   ▼
Transform
   │
   ▼
Validate
   │
   ▼
Parquet Dataset
```

---

## Pipeline Stages

### Ingest

- Reads the raw CSV dataset
- Loads the data into a Pandas DataFrame without modifying the source data

### Clean

- Handles missing gender values
- Combines the Date and Time columns into a single Datetime field
- Removes unnecessary columns
- Standardizes column names
- Converts data types

### Transform

Creates analytical features including:

- Year
- Month
- Day
- Weekday
- Hour

### Validate

The pipeline performs several data quality checks:

- Duplicate invoice IDs
- Missing values in required columns
- Positive numerical values
- Quantity constraints
- Rating constraints
- Datetime data type
- Integer data types for generated features

If any validation fails, execution stops immediately to prevent invalid data from propagating downstream.

### Persist

Stores the validated dataset in Parquet format for downstream analytical use.

Output file:

```text
data/processed/sales_clean.parquet
```

---

## Technologies

- Python
- Pandas
- PyArrow
- Pathlib
- Parquet

---

## Project Structure

```text
sales_supermarket_v2/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── config.py
│   ├── ingest.py
│   ├── clean.py
│   ├── transform.py
│   ├── validate.py
│   ├── persist.py
│   └── pipeline.py
├── requirements.txt
└── README.md
```

---

## Usage

Clone the repository:

```bash
git clone https://github.com/<your-username>/sales-supermarket-data-pipeline.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python src/pipeline.py
```

Successful execution produces output similar to:

```text
Processed dataset preview:
...

Pipeline completed successfully.
Rows: 1000
Columns: 19
```

---

## Future Improvements

Possible extensions include:

- Unit testing
- Logging
- Docker support
- Configuration files
- CI/CD with GitHub Actions
- Automated data quality reports

---

## Author

**Martín Papaleo**

Data Science Student — ITBA

Aspiring Data Engineer