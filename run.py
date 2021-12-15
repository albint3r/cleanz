from cleanz.swap_zero_values import swap_zerovalues_to_mean
import pandas as pd


# import data
df = pd.read_csv('data/listings_13_12_2021.csv')


if __name__ == '__main__':
    swap_zerovalues_to_mean(df, 'm2_terreno', min_search_value=10)
    swap_zerovalues_to_mean(df, 'm2_const', min_search_value=10,
                            alternative_value_complete='m2_terreno')
    swap_zerovalues_to_mean(df, 'habitaciones', min_search_value=0)
    swap_zerovalues_to_mean(df, 'banos', min_search_value=0)
    swap_zerovalues_to_mean(df, 'autos', min_search_value=0)
