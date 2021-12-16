import pandas as pd
import numpy as np


def count_drop_zero(dataframe: pd.DataFrame, target_cols: list) -> tuple[int, int]:
    """Count the posible drop values if apply the apply de replace drop zero

    Parameters
    -----------
    dataframe: pd.DataFrame:
        This is the dataframe to drop the columns

    target_cols: list:
        This is the list of the columns you want to know how many rows will be drop
        if you apply the NaN drop.

    Returns
    ----------
    Int
    """
    start_total_vals = len(dataframe)
    # Convert Zero to NaN to then drop it
    copy_df = dataframe[target_cols].replace(0, np.nan)
    count_drop_nan = len(copy_df[target_cols].dropna(how='all'))
    result = start_total_vals - count_drop_nan

    print(f'Total rows DataFrame:...{start_total_vals}')
    print(f'Total rows remaining:...{count_drop_nan}')
    print(f'Total rows drop it:...{result}')

    return result, count_drop_nan

def replace_drop_zero(dataframe: pd.DataFrame, target_cols: list) -> pd.DataFrame:
    """Check the quality of the final data Swap Zero Values

    First change the 0 values for Nan Values. Then it would drop it the row that have
    NaN values in all the columns that was passed in the target columns.

    But this is only create by default a copy of the Real DataFrame.

    Parameters
    -----------
    dataframe: pd.DataFrame:
        This is the dataframe to drop the columns

    target_cols: list:
        This is the list of the columns you want to drop it.

    Returns
    ----------
    pd.DataFrame
    """

    # Convert Zero to NaN to then drop it
    dataframe[target_cols] = dataframe[target_cols].replace(0, np.nan)
    # Drop NaN Values
    result = dataframe[target_cols].dropna(how='all')

    return result

