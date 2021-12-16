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
    print(f'\n\n------------{target_cols}------------------')
    print(f'Total rows DataFrame:...{start_total_vals}')
    print(f'Total rows remaining:...{count_drop_nan}')
    print(f'Total rows drop it:...{result}\n\n')
    print(f'--------------------------------------------')

    return result, count_drop_nan


def drop_zero(dataframe: pd.DataFrame, target_cols: dict) -> pd.DataFrame:
    """Check the quality of the final data Swap Zero Values

    First change the 0 values for Nan Values. Then it would drop it the row that have
    NaN values in all the columns that was passed in the target columns.

    But this is only create by default a copy of the Real DataFrame.

    Parameters
    -----------
    dataframe: pd.DataFrame:
        This is the dataframe to drop the columns

    target_cols: dict:
        This is a dict with the name of the column and the value you want to drop.

    Returns
    ----------
    pd.DataFrame
    """

    # Convert Zero to NaN to then drop it
    dataframe.replace(target_cols, np.nan, inplace=True)
    # Drop NaN Values
    dataframe.dropna(subset= list(target_cols.keys()) , how='all', inplace=True)

    # Add again the 0 to the NaN remain values
    dataframe.fillna(0, inplace=True)

    return dataframe

