from cleanz.swap_zero_values import swap_zerovalues_to_mean
import pandas as pd


def run(dataframe: pd.DataFrame):
    """Initialize the Swap Zero Values Function"""

    # import data
    swap_zerovalues_to_mean(dataframe=dataframe, column_name='m2_terreno', min_search_value=10,
                            type_of_listing_val='Casa', print_resume=False)
    swap_zerovalues_to_mean(dataframe=dataframe, column_name='m2_const', min_search_value=10,
                            alternative_value_complete='m2_terreno', print_resume=False)
    swap_zerovalues_to_mean(dataframe=dataframe, column_name='habitaciones', min_search_value=0,
                            print_resume=False)
    swap_zerovalues_to_mean(dataframe=dataframe, column_name='banos', min_search_value=0,
                            print_resume=False)
    swap_zerovalues_to_mean(dataframe=dataframe, column_name='autos', min_search_value=0,
                            print_resume=False)


if __name__ == '__main__':
    df = pd.read_csv('data/listings_13_12_2021.csv')
    run(df)
