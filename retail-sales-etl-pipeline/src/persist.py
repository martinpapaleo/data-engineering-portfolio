from pathlib import Path
# Get current file directory (data/src/)
BASE_DIR = Path(__file__).resolve().parent

# Move up one level to data/
DATA_DIR = BASE_DIR.parent

# Define processed folder
OUTPUT_DIR = DATA_DIR / "data" / "processed"

# Save file

def save_data(data_, debug=False):
    data_.to_parquet(OUTPUT_DIR / "sales_clean.parquet", index=False)
    return True
