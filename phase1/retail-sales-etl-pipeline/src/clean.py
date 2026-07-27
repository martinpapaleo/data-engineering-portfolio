'''
Clean:
- Replace missing Gender with "Unknown"
- Create Datetime by combining Date + Time using MM/DD/YYYY + HH:MM
- Drop raw Date and Time
- Drop Tax 5% and gross margin percentage
'''
import pandas as pd
from config import RAW_FILE_PATH

def clean_raw_data(
    raw_df: pd.DataFrame,
    debug: bool = False,
) -> pd.DataFrame:
    """
    Clean the raw supermarket sales dataset.

    The function fills missing gender values, combines the source date and
    time columns into a datetime column, and removes redundant fields.

    Parameters
    ----------
    raw_df : pd.DataFrame
        Raw supermarket sales data.
    debug : bool, default=False
        Whether to print information about the cleaned dataset.

    Returns
    -------
    pd.DataFrame
        A cleaned copy of the input dataset.
    """
    clean_df = raw_df.copy()

    clean_df["Gender"] = clean_df["Gender"].fillna("Unknown")

    clean_df["Datetime"] = pd.to_datetime(
        clean_df["Date"] + " " + clean_df["Time"],
        format="%m/%d/%Y %H:%M",
    )

    columns_to_drop = [
        "Date",
        "Time",
        "Tax 5%",
        "gross margin percentage",
    ]

    clean_df = clean_df.drop(columns=columns_to_drop)

    if debug:
        print("\nCleaned data preview:")
        print(clean_df.head())

        print("\nMissing values:")
        print(clean_df.isna().sum())

    return clean_df