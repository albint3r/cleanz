"""Wrapper function for Resumen info"""


def df_resume_repare(original_function):
    """Wrapper to show the stats"""
    def wrapper_function(*arg, **kwargs):

        # Identify if the user add the values to start the calculation
        dataframe = kwargs.get('dataframe')
        target_col_name = kwargs.get('column_name')
        type_of_listing = kwargs.get('type_of_listing_val')

        # Start Calculation:
        if type_of_listing is not None:
            start_miss_values = (
                    (dataframe[target_col_name] == 0) & (dataframe['tipo_inmueble'] == type_of_listing)).mean()
        else:
            start_miss_values = (dataframe[target_col_name] == 0).mean()

        result = original_function(*arg, **kwargs)

        # End Calculation:
        if type_of_listing:
            end_miss_values = (
                    (dataframe[target_col_name] == 0) & (dataframe['tipo_inmueble'] == type_of_listing)).mean()
        else:
            end_miss_values = (dataframe[target_col_name] == 0).mean()

        print(f'\n\n|------{target_col_name.upper()}------|')
        print(f'\n% Missing Starting Data:...{start_miss_values:.2f}%')
        print(f'% Missing Ending Data:...{end_miss_values:.2f}%\n')
        print(f'|-----------------------------------------|\n\n')

        return result

    return wrapper_function


def total_data_remaining(original_function): # TODO this function need to be repair
    """Count the end data remaining with all the transformations"""

    def wrapper_function(*args, **kwargs):
        # Set up the data frame to count
        df = kwargs.get('dataframe')
        start_total_vals = len(df)
        # Apply all the transformation
        original_function(df)
        # Count the final length of the data frame
        end_total_vals = len(kwargs.get('dataframe'))

        print(f'This is the final data:...{start_total_vals - end_total_vals}')

    return wrapper_function


