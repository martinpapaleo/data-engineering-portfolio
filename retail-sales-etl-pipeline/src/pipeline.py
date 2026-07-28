"""
Run the complete Retail Sales ETL pipeline.

Pipeline stages:
1. Ingest
2. Clean
3. Transform
4. Validate
5. Persist
"""

from ingest import load_raw_data
from clean import clean_raw_data
from transform import transform_data
from validate import valid_data
from persist import save_data
from pathlib import Path
import pandas as pd
import os

try: 
    def main():
        # Ingest
        df_raw = load_raw_data(debug=False)

        # Clean
        df_clean = clean_raw_data(df_raw, debug=False)

        # Transform
        df_transformed = transform_data(df_clean, debug=False)

        # Validate
        valid_data(df_transformed)

        # Persist
        save_data(df_transformed, debug=False)
        
        BASE_DIR = Path(__file__).resolve().parent
        PROJECT_ROOT = BASE_DIR.parent

        processed_path = (
            PROJECT_ROOT
            / "data"
            / "processed"
            / "sales_clean.parquet")

        df_final = pd.read_parquet(processed_path)
        print("\nProcessed dataset preview:")
        print(df_final.head())
        print("Pipeline completed successfully.")
        print(f"Rows: {len(df_final)}")
        print(f"Columns: {len(df_final.columns)}")
except Exception as error:
    print(f"Pipeline failed: {error}")
    raise

if __name__ == "__main__":
    main()