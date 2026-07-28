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

    datetime = transform_df["Datetime"]

    # Calendar features
    transform_df["Year"] = transform_df["Datetime"].dt.year
    transform_df["Month"] = transform_df["Datetime"].dt.month
    transform_df["Day"] = transform_df["Datetime"].dt.day
    transform_df["Weekday"] = transform_df["Datetime"].dt.day_name()
    

    # Time-of-day features
    transform_df["Hour"] = transform_df["Datetime"].dt.hour

    if debug:
        print("\nTransformed data preview:")
        print(transform_df.head())

        print("\nNew features added:")
        print(["Year", "Month", "Day", "Weekday", "Hour"])

    return transform_df