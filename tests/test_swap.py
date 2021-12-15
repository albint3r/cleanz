import pytest
from cleanz.swap_zero_values import swap_zerovalues_to_mean
import pandas as pd


class TestSwapZeroValues(object):
    """Test the function Swap_Zero_Values"""

    @pytest.fixture
    def setup_df(self) -> pd.DataFrame:
        """Create the initial DataFrame for the test"""

        data = {'colonia': ['Puerta de Hierro', 'Puerta de Hierro', 'Puerta de Hierro', 'Loma Larga', 'Loma Larga',
                            'Loma Larga', 'Valle', 'Valle', 'zero_1', 'zero_2', 'Legacy', 'Legacy', 'Legacy', ],
                'm2_terreno': [500, 510, 0, 200, 210, 0, 250, 0, 0, 100, 0, 0, 0],
                'm2_const': [220, 230, 0, 220, 230, 0, 240, 0, 0, 0, 85, 85, 0],
                'habitaciones': [3, 3, 0, 2, 2, 0, 2, 0, 0, 0, 2, 2, 0],
                'banos': [3, 3, 0, 2, 2, 0, 2, 0, 0, 0, 2, 0, 2],
                'autos': [3, 3, 0, 2, 2, 0, 2, 0, 0, 0, 2, 2, 0],
                'tipo_inmueble': ['Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa',
                                  'Casa', 'Departamento', 'Departamento', 'Departamento']}

        return pd.DataFrame(data)

    def test_swap_zero_m2(self, setup_df: pd.DataFrame):
        """Test the m2 complete works correctly

        Parameters
        ----------
        setup_df: pandas.DataFrame
            Is the test tabular data for the tests.
        """
        # Create DataFrame to test
        df = setup_df

        # Total Zero Remaining Results expected : 1
        actual = swap_zerovalues_to_mean(df, 'm2_terreno', min_search_value=10, type_of_listing_val='Casa')
        expected = 1
        msg = f'Expected Value:...{expected} and the actual Result was:...{actual}'

        assert actual == expected, msg

        # Expected results : Puerta de Hiero
        name1 = df.loc[2, 'colonia']
        actual1 = df.loc[2, 'm2_terreno']
        expected1 = 505
        msg1 = f'Expected Value in {name1}:...{expected1} and the actual Result was:...{actual1}'

        assert actual1 == expected1, msg1

        # Expected results : Loma Larga
        name2 = df.loc[5, 'colonia']
        actual2 = df.loc[5, 'm2_terreno']
        expected2 = 205
        msg2 = f'Expected Value in {name2}:...{expected2} and the actual Result was:...{actual2}'

        assert actual2 == expected2, msg2

        # Expected results : Valle
        name3 = df.loc[7, 'colonia']
        actual3 = df.loc[7, 'm2_terreno']
        expected3 = 250
        msg3 = f'Expected Value in {name3}:...{expected3} and the actual Result was:...{actual3}'

        assert actual3 == expected3, msg3

        # Expected results : Zero1
        name4 = df.loc[8, 'colonia']
        actual4 = df.loc[8, 'm2_terreno']
        expected4 = 0
        msg4 = f'Expected Value in {name4}:...{expected4} and the actual Result was:...{actual4}'

        assert actual4 == expected4, msg4
