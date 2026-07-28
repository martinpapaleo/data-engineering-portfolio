'''
No duplicate Invoice_ID
No nulls in required columns (your full list)
Unit_price > 0
Quantity >= 1
Total > 0
cogs > 0
0 <= Rating <= 10
Datetime is datetime dtype
'''
import pandas as pd

def value_pos_in_df(df_, col_name):
    if (df_[col_name] <= 0).sum() != 0:
        return False
    return True

def valid_data(data_):

    # Primary key validation
    if data_['Invoice_ID'].duplicated().sum() != 0:
        raise ValueError("Invoice_ID column has duplicated values")

    # No nulls in required columns (your full list)
    required_columns = [
    "Invoice_ID",
    "Branch",
    "City",
    "Product_line",
    "Unit_price",
    "Quantity",
    "Total",
    "Datetime",
    "cogs",
    "Gross_income"]
    null_counts = data_[required_columns].isnull().sum()

    if null_counts.any():
        invalid_columns = null_counts[null_counts > 0].to_dict()
        raise ValueError(
            f"Null values detected in required columns: {invalid_columns}"
        )
    
    # Numeric validation
    # Unit_price > 0 
    if not value_pos_in_df(data_, 'Unit_price'):
        raise ValueError("Unit_price column has values <= 0")

    # Total > 0
    if not value_pos_in_df(data_, 'Total'):
        raise ValueError("Total column has values <= 0")

    # cogs > 0
    if not value_pos_in_df(data_, 'cogs'):
        raise ValueError("cogs column has values <= 0")
    # I do know that Unit_price, Total and cogs could be chacked in one single line, but I'd want to differenciate with a differet print each possible fail

    # Quantity >= 1
    if (data_["Quantity"] < 1).any():
        raise ValueError("Quantity column has values < 1")
    
    # 0 <= Rating <= 10
    if ((data_["Rating"] < 0) | (data_["Rating"] > 10)).any():
        raise ValueError("Rating column has values outside the range [0, 10]")

    # Datetime validation
    # Datetime type datetime[ns]
    if not pd.api.types.is_datetime64_any_dtype(data_['Datetime']):
        raise ValueError("Datetime column is not datetime dtype")

    # Time columns have int dtype
    time_columns = ['Year', 'Month', 'Day', 'Hour']
    for i in time_columns:
        if not pd.api.types.is_integer_dtype(data_[i]):
            raise ValueError(f'{i} column has values which are not int dtype')

    # Weekday column has str dtype
    if not pd.api.types.is_string_dtype(data_['Weekday']):
            raise ValueError("Weekday column is not a string dtype")
    return True