from cleanz.swap_zero_values import swap_zerovalues_to_mean, column_zero_checker
from cleanz.quality_data_selector import drop_zero
import pandas as pd


def run(dataframe: pd.DataFrame):
    """Initialize the Swap Zero Values Function"""

    # Run All the Filters Functions

    swap_zerovalues_to_mean(dataframe=dataframe, column_name='m2_terreno', min_search_value=50,
                            type_of_listing_val='Casa', print_resume=False)

    swap_zerovalues_to_mean(dataframe=dataframe, column_name='m2_const', min_search_value=50,
                            alternative_value_complete='m2_terreno', print_resume=False)

    swap_zerovalues_to_mean(dataframe=dataframe, column_name='habitaciones', min_search_value=0,
                            print_resume=False)

    swap_zerovalues_to_mean(dataframe=dataframe, column_name='banos', min_search_value=0,
                            print_resume=False)

    swap_zerovalues_to_mean(dataframe=dataframe, column_name='autos', min_search_value=0,
                            print_resume=False)

    drop_zero(dataframe, {'m2_const': 0, 'm2_terreno': 0})

    column_zero_checker(dataframe, {'tipo_inmueble': 'Casa', 'm2_terreno': 0}, 'm2_const')


if __name__ == '__main__':
    df = pd.read_csv('data/listings_13_12_2021.csv')
    run(dataframe=df)
