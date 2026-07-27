"""
Load the raw supermarket sales dataset.

Returns
-------
pd.DataFrame
    Raw dataset exactly as stored on disk, without any preprocessing.
"""
import pandas as pd
from config import RAW_FILE_PATH
def load_raw_data(debug) -> pd.DataFrame:
    import os
    import pandas as pd
    if debug:
        print("cwd:", os.getcwd())
        print("__file__:", __file__)
    src_dir = os.path.dirname(os.path.abspath(__file__))
    if debug:
        print("src_dir:", src_dir)
    project_dir = os.path.dirname(src_dir)  # goes from /src to /sales_supermarket_v2
    if debug:
        print(project_dir)

    raw_path = os.path.join(project_dir, "data", "raw", "supermarket_sales.csv")
    if debug:
        print(raw_df.head())

    try:
        df_raw = pd.read_csv(RAW_FILE_PATH) #obtained from scr_dir and modifying it properly.
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Raw dataset not found: {RAW_FILE_PATH}")

    if debug:
        print('loaded shape:',df_raw.shape)
        print(df_raw.head())
    return(df_raw)
