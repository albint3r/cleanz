import pandas as pd
import numpy as np


def swap_zerovalues_to_mean(dataframe: pd.DataFrame, column_name: str, min_search_value: int = 0,
                            type_of_listing_val: str = None, alternative_value_complete: str = None,
                            print_msg_results: bool = True) -> int:
    """ Swap the zero values for the mean of the area

    Select a Column name and add the minimum values you want to change for the mean in the area.

    Parameters
    ----------
    dataframe: pandas.DataFrame:
        Is the dataframe you will use to clean.

    column_name: str:
        Is the name of the column that contain the Zero values Rows. You need to selected to swap for the mean
        values that contains data.

    min_search_value: int:
        Is the minimal value you want to change for the mean. By the default is 0, but in some cases
        is good idea to add more range to identify odd values.
        (Optional: Default = 0)

    type_of_listing_val: str:
        This select a type of listing to create a more specific subset. A good idea to use this
        is when the apartments don't need to be modify.
        (Optional: Default = None)

    alternative_value_complete: str:
        This is the name of a column that you want to substitute the missing value for this.
        (Optional: Default = None)

    print_msg_results: bool:
        If is True you will see a output msg to corroborate all the work

    Returns
    ---------
    int
    """
    # Len initial dataframe size and after that this would be subtracted by the final total of missing values
    # This helps to calculate the percentage of missing values over all the data.
    init_total_rows = len(dataframe)

    # Select the Zero Values Column
    zero_values_column = dataframe[column_name] <= min_search_value

    # Adds an additional subset to the Dataframe adding + the type of listing
    if type_of_listing_val is not None:
        type_of_listing = dataframe['tipo_inmueble'] == type_of_listing_val

        # Only apply this subset if is TRUE
        list_zone_zero_vals = dataframe.loc[(zero_values_column & type_of_listing), 'colonia'].unique()
        # Count total of Missing Values: -> n
        star_total_zero_values = (zero_values_column & type_of_listing).sum()
        doble_subset = True  # <- Helps to the  print statement
    else:
        # This is list creator of the name of the zones that doesn't have the value
        list_zone_zero_vals = dataframe.loc[zero_values_column, 'colonia'].unique()
        # Count total of Missing Values: -> n
        star_total_zero_values = zero_values_column.sum()
        doble_subset = False

    for zone_name in list_zone_zero_vals:

        # Set the values to subset
        zone = dataframe['colonia'] == zone_name
        zone_value_not_null = dataframe[column_name] >= min_search_value

        # Calculate the mean of the columns that have values
        mean_value = np.mean(dataframe.loc[(zone & zone_value_not_null), column_name])

        try:
            # Change NaN values to zero = 0
            if pd.isna(mean_value) and alternative_value_complete is None:
                mean_value = 0
                dataframe.loc[(zone & zero_values_column), column_name] = mean_value
                msg = f'{zone_name}:..........{mean_value:.1f} m2'

            # Update Nan Values by the Mean
            elif pd.isna(mean_value) and alternative_value_complete is not None:
                alternative_value = dataframe.loc[zone, alternative_value_complete]
                dataframe.loc[(zone & zero_values_column), column_name] = alternative_value
                msg = f'{zone_name}:..........{alternative_value} m2'

            else:
                dataframe.loc[(zone & zero_values_column), column_name] = np.round(mean_value)  # <- Round Result
                msg = f'{zone_name}:..........{mean_value:.1f} m2'

        except ValueError:
            # Update Zero Values by 0 or Alternative Value.
            if alternative_value_complete is not None:
                alternative_value = dataframe.loc[zone, alternative_value_complete]  # <- Select the alternative value
                dataframe.loc[(zone & zero_values_column), column_name] = alternative_value
                msg = f'{zone_name}:..........{alternative_value} m2'

            else:
                dataframe.loc[(zone & zero_values_column), column_name] = 0
                msg = f'{zone_name}:..........0 m2'

        if print_msg_results:
            print(msg)

    # Calculate again the 0 Values remaining in the DataFrame
    corroborate_zero_val = dataframe[column_name] <= min_search_value  # <- Corroborate the Cleaning Rows

    # Count and Print the Results of the Swap Zero Values for Mean Values
    if print_msg_results:
        if doble_subset:
            end_total_zero_values = (corroborate_zero_val & type_of_listing).sum()
        else:
            end_total_zero_values = corroborate_zero_val.sum()

        # Subtract the initial zero values with the result
        total_values_corrected = star_total_zero_values - end_total_zero_values
        percentage_values_corrected = (total_values_corrected / star_total_zero_values) * 100
        percentage_of_missing_data = (star_total_zero_values / init_total_rows) * 100

        # Print results of the corrections
        print(f'|------------------------<{column_name.title()}>------------------------------------|')
        print(f'\n\nStart total rows with: Zero Values ----> {star_total_zero_values}')
        print(f'End total rows with: Zero Values:----> {end_total_zero_values}')
        print(f'Total Data Repare:----> {total_values_corrected}\n')
        print(f'Percentage Data Repare:---->  {np.round(percentage_values_corrected)}%')
        print(f'Percentage of Missing General Data in Table:----> {np.round(percentage_of_missing_data)}%\n\n')
        print(f'|------------------------<{column_name.title()}>------------------------------------|')

        return end_total_zero_values
