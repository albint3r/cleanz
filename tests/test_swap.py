import pytest
from cleanz.swap_zero_values import swap_zerovalues_to_mean
import pandas as pd
import numpy as np

class TestSwapZeroValues(object):
    """Test the function Swap_Zero_Values"""

    @pytest.fixture
    def setup_df(self):
        data = {'colonia': ['Puerta de Hierro', 'Puerta de Hierro', 'Puerta de Hierro', 'Chapalita', 'Chapalita',
                            'Chapalita',
                            'Valle', 'Valle', 'zero_1', 'zero_2'],
                'm2_terreno': [200, 210, 0, 200, 210, 0, 250, 0, 0, 0],
                'm2_const': [220, 230, 0, 220, 230, 0, 240, 0, 0, 0],
                'habitaciones': [3, 3, 0, 2, 2, 0, 2, 0, 0, 0],
                'banos': [3, 3, 0, 2, 2, 0, 2, 0, 0, 0],
                'autos': [3, 3, 0, 2, 2, 0, 2, 0, 0, 0],
                'tipo_inmueble': ['Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa']}

        return pd.DataFrame(data)

    def test_swap_zero_m2(self, setup_df):
        """Test the m2 complete works correctly

        Parameters
        ----------
        setup_df: pandas.DataFrame
            Is the test tabular data for the tests.
        """

        df = setup_df
        actual = df.loc[2, 'm2_terreno']
        expected = 200.5
        swap_zerovalues_to_mean(df, 'm2_terreno', min_search_value=10, type_of_listing_val='Casa')

        assert actual == expected, f'Expected Value: {expected} and the actual.....{actual}'