from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / 'data'
RAW_DIR = DATA_DIR / 'raw'
PROCESSED_DIR = DATA_DIR / 'processed'
RAW_FILE_PATH = RAW_DIR / 'supermarket_sales.csv'
OUTPUT_FILE_PATH = PROCESSED_DIR / 'sales_clean.parquet'