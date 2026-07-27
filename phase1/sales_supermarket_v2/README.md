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
