import pytest
import pandas as pd
from cleanz.quality_data_selector import drop_zero, count_drop_zero


class TestQualityData(object):

    @pytest.fixture
    def setup_df(self) -> pd.DataFrame:
        """Create the initial DataFrame for the test"""

        data = {'colonia': ['Puerta de Hierro', 'Puerta de Hierro', 'Puerta de Hierro', 'Loma Larga', 'Loma Larga',
                            'Loma Larga', 'Valle', 'Valle', 'zero_1', 'zero_2', 'Legacy', 'Legacy', 'Legacy', ],
                'm2_terreno': [500, 510, 0, 200, 210, 0, 250, 0, 0, 100, 0, 0, 0],
                'm2_const': [220, 230, 0, 200, 230, 0, 240, 0, 0, 0, 85, 85, 0],
                'habitaciones': [3, 3, 0, 2, 2, 0, 2, 0, 0, 0, 2, 2, 0],
                'banos': [3, 3, 0, 2, 2, 0, 2, 0, 0, 0, 2, 0, 2],
                'autos': [3, 3, 0, 2, 2, 0, 2, 0, 0, 0, 2, 2, 0],
                'tipo_inmueble': ['Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa',
                                  'Casa', 'Departamento', 'Departamento', 'Departamento']}

        return pd.DataFrame(data)

    def test_count_drop_zero_result(self, setup_df: pd.DataFrame):
        """Test the function drop zero to identify the total row it will drop if apply the function"""

        df = setup_df

        actual, _ = count_drop_zero(df, ['m2_const', 'm2_terreno'])
        expected = 5  # <- Rows
        msg = f'The expected result is: {expected} and you have  {actual}'
        assert actual == expected, msg

    def test_count_drop_zero_count(self, setup_df: pd.DataFrame):
        """Test the function drop zero to identify the total row it will keep"""

        df = setup_df

        _, actual = count_drop_zero(df, ['m2_const', 'm2_terreno'])
        expected = 8  # <- Rows
        msg = f'The expected result is: {expected} and you have  {actual}'
        assert actual == expected, msg

    def test_drop_zero(self, setup_df: pd.DataFrame):
        """Test the fucntion Quality Data Selector"""

        df = setup_df

        actual = len(drop_zero(df, {'m2_const': 0, 'm2_terreno': 0}))
        expected = 8  # <- Rows
        msg = f'The expected result is: {expected} and you have  {actual}'
        assert actual == expected, msg

    def test_drop_zero_diff(self, setup_df: pd.DataFrame):
        """Test the diferencen between the initial data and the final result"""

        df = setup_df
        initial_len_df = len(df)

        actual = initial_len_df - len(drop_zero(df, {'m2_const': 0, 'm2_terreno': 0}))
        expected = 5  # <- Rows
        msg = f'The expected result is: {expected} and you have  {actual}'
        assert actual == expected, msg
