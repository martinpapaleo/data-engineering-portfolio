from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent

OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_data(data_, debug=False):
    """
    Save the validated dataset as a Parquet file.

    Parameters
    ----------
    data_ : pd.DataFrame
        Validated dataset.
    debug : bool, default=False
        Whether to print the output location.

    Returns
    -------
    bool
        True if the dataset is saved successfully.
    """

    output_path = OUTPUT_DIR / "sales_clean.parquet"

    data_.to_parquet(output_path, index=False)

    if debug:
        print(f"Saved dataset to: {output_path}")

    return True