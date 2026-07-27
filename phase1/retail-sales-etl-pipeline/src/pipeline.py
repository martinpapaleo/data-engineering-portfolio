from ingest import load_raw_data
from clean import clean_raw_data
from transform import transform_data
from validate import valid_data
from persist import save_data
from pathlib import Path
import pandas as pd
import os

def main():

    df_raw_ = load_raw_data(debug=False)
    df_clean = clean_raw_data(df_raw_, debug=False)
    df_trans = transform_data(df_clean)
    valid_data(df_trans)
    save_data(df_trans, debug=False)
    src_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(src_dir)
    processed_path = os.path.join(project_dir, "data", "processed", "sales_clean.parquet")
    df_final = pd.read_parquet(processed_path)
    print(df_final.head(5))
    print('Pipeline finished succesfully.')
if __name__ == "__main__":
    main()