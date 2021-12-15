import numpy as np


def df_resume_repare(original_function):
    """Wrapper to show the stats"""
    def wrapper_function(*arg, **kwargs):
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

