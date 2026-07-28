import pandas as pd

def transform_data(
    clean_df: pd.DataFrame,
    debug: bool = False,
) -> pd.DataFrame:
    """
    Create analytical features from the cleaned dataset.

    Parameters
    ----------
    clean_df : pd.DataFrame
        Clean supermarket sales dataset.
    debug : bool, default=False
        Whether to print transformation results.

    Returns
    -------
    pd.DataFrame
        Dataset enriched with analytical features.
    """

    transform_df = clean_df.copy()

    datetime_col = transform_df["Datetime"]

    # Calendar features
    transform_df["Year"] = datetime_col.dt.year
    transform_df["Month"] = datetime_col.dt.month
    transform_df["Day"] = datetime_col.dt.day
    transform_df["Weekday"] = datetime_col.dt.day_name()

    # Time-of-day features
    transform_df["Hour"] = datetime_col.dt.hour

    if debug:
        print(transform_df.head())

    return transform_df