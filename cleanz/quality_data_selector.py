import pandas as pd
import numpy as np


def quality_data_check(dataframe: pd.DataFrame, target_cols: list) -> pd.DataFrame:
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
    copy_df = dataframe[target_cols].replace(0, np.nan)
    # Drop NaN Values
    result = copy_df[target_cols].dropna(how='all')

    return result

