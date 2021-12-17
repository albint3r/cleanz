import pytest
from cleanz.swap_zero_values import swap_zerovalues_to_mean, quick_swap_zero, column_zero_checker
import pandas as pd


class TestSwapZeroValues(object):
    """Test the function Swap_Zero_Values"""

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

    def test_swap_zero_no_print(self, setup_df: pd.DataFrame):
        """The print function Resume

        Parameters
        ----------
        setup_df: pandas.DataFrame
            Is the test tabular data for the tests.
        """
        # Create DataFrame to test
        df = setup_df

        # Total Zero Remaining Results expected : None
        actual = swap_zerovalues_to_mean(dataframe=df, column_name='m2_terreno', min_search_value=10,
                                         type_of_listing_val='Casa',
                                         print_resume=False)  # <- This is the test
        expected = None
        msg = f'Expected Value:...{expected} and the actual Result was:...{actual}'

        assert actual == expected, msg

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
        actual = swap_zerovalues_to_mean(dataframe=df, column_name='m2_terreno', min_search_value=10,
                                         type_of_listing_val='Casa')
        expected = 1
        msg = f'Expected Value:...{expected} and the actual Result was:...{actual}'

        assert actual == expected, msg

        # |----------------------------------------------------------------------|
        # |This are the expected values result after the transformation Data.    |
        # |This Values was obtained from a regular mean operation.               |
        # |----------------------------------------------------------------------|

        # Expected results of 500+510/2 = 505 : Puerta de Hiero
        # 3 rows exist, two have values and 1 have zero
        name1 = df.loc[2, 'colonia']
        actual1 = df.loc[2, 'm2_terreno']
        expected1 = 505 # (510, 505)
        msg1 = f'Expected Value in {name1}:...{expected1} and the actual Result was:...{actual1}'

        assert actual1 == expected1, msg1

        # Expected results 200+210/2 = 205 : Loma Larga
        # 3 rows exist, two have values and 1 have zero
        name2 = df.loc[5, 'colonia']
        actual2 = df.loc[5, 'm2_terreno']
        expected2 = 205
        msg2 = f'Expected Value in {name2}:...{expected2} and the actual Result was:...{actual2}'

        assert actual2 == expected2, msg2

        # Expected results 250/1 = 250 (Just One row) =  : Valle
        # 2 rows exist, one have values and 1 have zero
        name3 = df.loc[7, 'colonia']
        actual3 = df.loc[7, 'm2_terreno']
        expected3 = 250
        msg3 = f'Expected Value in {name3}:...{expected3} and the actual Result was:...{actual3}'

        assert actual3 == expected3, msg3

        # Expected results 0 = 0 : Zero1
        # 1 row exist, one have zero values (that's it!, no more data  ZEROOOOOOO!)
        name4 = df.loc[8, 'colonia']
        actual4 = df.loc[8, 'm2_terreno']
        expected4 = 0
        msg4 = f'Expected Value in {name4}:...{expected4} and the actual Result was:...{actual4}'

        assert actual4 == expected4, msg4

    def test_swap_zero_const_not_alter_col(self, setup_df: pd.DataFrame):
        """Test the m2 Const complete works correctly

        Parameters
        ----------
        setup_df: pandas.DataFrame
            Is the test tabular data for the tests.
        """
        # Create DataFrame to test
        df = setup_df

        # Total Zero Remaining Results expected : 1
        actual = swap_zerovalues_to_mean(dataframe=df, column_name='m2_const', min_search_value=10)
        expected = 2
        msg = f'Expected Value:...{expected} and the actual Result was:...{actual}'

        assert actual == expected, msg

        # Expected results : Puerta de Hiero
        # 3 rows exist, two have values and 1 have zero
        name1 = df.loc[2, 'colonia']
        actual1 = df.loc[2, 'm2_const']
        expected1 = 225
        msg1 = f'Expected Value in {name1}:...{expected1} and the actual Result was:...{actual1}'

        assert actual1 == expected1, msg1

        # Expected results 220+230/2 = 215 AND 0 : Loma Larga
        # 3 rows exist, two have values and 1 have zero
        name2 = df.loc[5, 'colonia']
        actual2 = df.loc[5, 'm2_const']
        expected2 = 215
        msg2 = f'Expected Value in {name2}:...{expected2} and the actual Result was:...{actual2}'

        assert actual2 == expected2, msg2

        # Expected results 240/1 = 85 AND 0: Valle
        # 2 rows exist, one have values and 1 have zero
        name3 = df.loc[7, 'colonia']
        actual3 = df.loc[7, 'm2_const']
        expected3 = 240
        msg3 = f'Expected Value in {name3}:...{expected3} and the actual Result was:...{actual3}'

        assert actual3 == expected3, msg3

        # Expected results 0 = 0: Zero1
        # 1 rows exist, one have ZERO values.
        name4 = df.loc[8, 'colonia']
        actual4 = df.loc[8, 'm2_const']
        expected4 = 0
        msg4 = f'Expected Value in {name4}:...{expected4} and the actual Result was:...{actual4}'

        assert actual4 == expected4, msg4

        # Expected results 0 = 0 : Zero2
        # 1 rows exist, one have ZERO values.
        name5 = df.loc[9, 'colonia']
        actual5 = df.loc[9, 'm2_const']
        expected5 = 0
        msg5 = f'Expected Value in {name5}:...{expected5} and the actual Result was:...{actual5}'

        assert actual5 == expected5, msg5

        # Expected results 85+85/2 = 85 AND 0: Legacy
        # 2 rows exist, TWO have values
        name6 = df.loc[12, 'colonia']
        actual6 = df.loc[12, 'm2_const']
        expected6 = 85
        msg6 = f'Expected Value in {name6}:...{expected6} and the actual Result was:...{actual6}'

        assert actual6 == expected6, msg6

    def test_swap_zero_const_alter_col(self, setup_df: pd.DataFrame):
        """Test the m2 Const complete works correctly

        Parameters
        ----------
        setup_df: pandas.DataFrame
            Is the test tabular data for the tests.
        """
        # Create DataFrame to test
        df = setup_df

        # Total Zero Remaining Results expected : 1
        actual = swap_zerovalues_to_mean(dataframe=df, column_name='m2_const', min_search_value=10,
                                         alternative_value_complete='m2_terreno')
        expected = 1
        msg = f'Expected Value:...{expected} and the actual Result was:...{actual}'

        assert actual == expected, msg

        # Expected results : Puerta de Hiero
        # 3 rows exist, two have values and 1 have zero
        name1 = df.loc[2, 'colonia']
        actual1 = df.loc[2, 'm2_const']
        expected1 = 225
        msg1 = f'Expected Value in {name1}:...{expected1} and the actual Result was:...{actual1}'

        assert actual1 == expected1, msg1

        # Expected results 220+230/2 = 215 AND 0 : Loma Larga
        # 3 rows exist, two have values and 1 have zero
        name2 = df.loc[5, 'colonia']
        actual2 = df.loc[5, 'm2_const']
        expected2 = 215
        msg2 = f'Expected Value in {name2}:...{expected2} and the actual Result was:...{actual2}'

        assert actual2 == expected2, msg2

        # Expected results 240/1 = 85 AND 0: Valle
        # 2 rows exist, one have values and 1 have zero
        name3 = df.loc[7, 'colonia']
        actual3 = df.loc[7, 'm2_const']
        expected3 = 240
        msg3 = f'Expected Value in {name3}:...{expected3} and the actual Result was:...{actual3}'

        assert actual3 == expected3, msg3

        # Expected results 0 = 0: Zero1
        # 1 rows exist, one have ZERO values.
        name4 = df.loc[8, 'colonia']
        actual4 = df.loc[8, 'm2_const']
        expected4 = 0
        msg4 = f'Expected Value in {name4}:...{expected4} and the actual Result was:...{actual4}'

        assert actual4 == expected4, msg4

        # Expected results : Zero2
        # 1 rows exist, one have values ZERO VALUES but has activate the alternative_value_complete that
        # takes the target value the column name m2_terreno column that have the value of 100.
        name5 = df.loc[9, 'colonia']
        actual5 = df.loc[9, 'm2_const']
        expected5 = 100
        msg5 = f'Expected Value in {name5}:...{expected5} and the actual Result was:...{actual5}'

        assert actual5 == expected5, msg5

        # Expected results 85+85/2 = 85 AND 0: Legacy
        # 2 rows exist, TWO have values
        name6 = df.loc[12, 'colonia']
        actual6 = df.loc[12, 'm2_const']
        expected6 = 85
        msg6 = f'Expected Value in {name6}:...{expected6} and the actual Result was:...{actual6}'

        assert actual6 == expected6, msg6

    def test_quick_swap_zero(self, setup_df: pd.DataFrame):
        """Test the quick swap zero function

        Parameters
        ----------
        setup_df: pandas.DataFrame
            Is the test tabular data for the tests.
        """
        # Create DataFrame to test
        df = setup_df

        # Total Zero Remaining Results expected : 280
        actual = quick_swap_zero(df, 'm2_terreno')
        expected = 295
        msg = f'Expected Value:...{expected} and the actual Result was:...{actual}'

        assert actual == expected, msg

    def test_column_zero_checker(self):
        """This function Identify if it still haves missing values. And Complete the missing values
        with another target column in the table.
        """
        # Create DataFrame to test
        data = {'colonia': ['Puerta de Hierro', 'Puerta de Hierro', 'Puerta de Hierro', 'Loma Larga', 'Loma Larga',
                            'Loma Larga', 'Valle', 'Valle', 'zero_1', 'zero_2', 'Legacy', 'Legacy', 'Legacy', ],
                'm2_terreno': [500, 510, 0, 200, 210, 0, 250, 0, 0, 100, 0, 0, 0],
                'm2_const': [220, 230, 220, 200, 230, 100, 240, 0, 0, 0, 85, 85, 0],
                'habitaciones': [3, 3, 0, 2, 2, 0, 2, 0, 0, 0, 2, 2, 0],
                'banos': [3, 3, 0, 2, 2, 0, 2, 0, 0, 0, 2, 0, 2],
                'autos': [3, 3, 0, 2, 2, 0, 2, 0, 0, 0, 2, 2, 0],
                'tipo_inmueble': ['Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa', 'Casa',
                                  'Casa', 'Departamento', 'Departamento', 'Departamento']}

        df = pd.DataFrame(data)

        # Total Zero Remaining Results expected : [220, 100]
        column_zero_checker(df, {'tipo_inmueble': 'Casa', 'm2_terreno': 0}, 'm2_const')

        actual = list(df.loc[[2, 5], 'm2_terreno'])
        expected = [220, 100]
        msg = f'Expected Value:...{expected} and the actual Result was:...{actual}'

        assert actual == expected, msg
