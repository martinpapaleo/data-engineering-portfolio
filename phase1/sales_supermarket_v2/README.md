# Sales Supermarket Data Pipeline

## Overview

This project implements a modular batch data pipeline that transforms raw supermarket sales data into a clean and validated analytical dataset.

The pipeline separates ingestion, cleaning, transformation, validation, and persistence into independent modules to improve readability, maintainability, and reproducibility.

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
Processed Parquet

## Pipeline Stages

### Ingest

Loads the raw CSV dataset without modifying the source data.

### Clean

- Handles missing gender values
- Combines date and time into a single datetime column
- Removes unnecessary columns
- Standardizes data types

### Transform

Creates analytical fields such as:

- Year
- Month
- Day
- Weekday
- Hour

### Validate

Checks:

- Duplicate invoice IDs
- Missing values
- Positive numerical values
- Quantity constraints
- Rating constraints
- Datetime and integer data types

The pipeline stops with an error when validation fails.

### Persist

Stores the validated dataset in Parquet format for downstream analytical use.

## Project Structure

```text
sales_supermarket_v2/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── ingest.py
│   ├── clean.py
│   ├── transform.py
│   ├── validate.py
│   ├── persist.py
│   └── pipeline.py
└── README.md