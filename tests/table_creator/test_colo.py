import pandas as pd
import os
import shutil
import pytest
from cleanz.table_creator.colo import colo_table_creator


class TestTableCreator(object):
    """Test the function of Table Creator"""

    @pytest.fixture
    def set_up(self):
        """Take the listing CSV to make the test"""

        # Create a temporal directory for the File created by the function
        os.mkdir('tests/table_creator/data/')

        # Set the path of the listing
        data = 'data/clean_data/listing_17_12_2021.csv'

        yield pd.read_csv(data, parse_dates=['fecha_pub'])

        # Remove File Created by the function in the Data Directory inside the Test Directory
        shutil.rmtree('tests/table_creator/data/')

    def test_colo_avg_price_rent(self, set_up):
        """Test the function create the correct avg price by type fo listing: Rent or Buy

        In this case it test the Rent.

        Parameters
        ----------
        set_up :
            Is the dataframe for all the tests

        Returns
        -------

        """

        df = set_up
        # Run function
        df_result = colo_table_creator(df, 'Casa', 'Rent', 'test', False)

        # Colonia: 5 de Diciembre
        colonia_americana = df_result.colonia == 'Americana'

        # Test
        actual_price = df_result.loc[colonia_americana, 'avg_price'].values[0]
        expected_avg_price = [35698.72]
        msg = f'This is the expected result:...{expected_avg_price} and you have:...{actual_price}'
        assert actual_price == expected_avg_price, msg

    def test_colo_avg_const_rent(self, set_up):
        """Test the function create the correct avg m2_const by type fo listing: Rent or Buy

        In this case it test the Rent.

        Parameters
        ----------
        set_up :
            Is the dataframe for all the tests

        Returns
        -------

        """

        df = set_up
        # Run function
        df_result = colo_table_creator(df, 'Casa', 'Rent', 'test', False)

        # Colonia: 'Zapopan Centro'
        colonia_zapopan_centro = df_result.colonia == 'Zapopan Centro'

        # Test
        actual_avg_m2 = df_result.loc[colonia_zapopan_centro, 'avg_const'].values[0]
        expected_avg_m2 = 181.13114754098362
        msg = f'This is the expected result:...{expected_avg_m2} and you have:...{actual_avg_m2}'
        assert actual_avg_m2 == expected_avg_m2, msg

    def test_colo_avg_price_buy(self, set_up):
        """Test the function create the correct avg price by type fo listing: Rent or Buy

        In this case it test the Buy.

        Parameters
        ----------
        set_up :
            Is the dataframe for all the tests

        Returns
        -------

        """

        df = set_up
        # Run function
        df_result = colo_table_creator(df, 'Casa', 'Buy', 'test', False)

        # Colonia: 'Valle Imperial'
        colonia_valle_imperial = df_result.colonia == 'Valle Imperial'

        # Test
        actual_price = df_result.loc[colonia_valle_imperial, 'avg_price'].values[0]
        expected_avg_price = 4611172.641196013
        msg = f'This is the expected result:...{expected_avg_price} and you have:...{actual_price}'
        assert actual_price == expected_avg_price, msg

    def test_colo_avg_m2_buy(self, set_up):
        """Test the function create the correct avg m2_const by type fo listing: Rent or Buy

        In this case it test the Buy.

        Parameters
        ----------
        set_up :
            Is the dataframe for all the tests

        Returns
        -------

        """

        df = set_up
        # Run function
        df_result = colo_table_creator(df, 'Casa', 'Buy', 'test', False)

        # Colonia: 'Solares
        colonia_solares = df_result.colonia == 'Solares'

        # Test
        actual_avg_m2 = df_result.loc[colonia_solares, 'avg_m2'].values[0]
        expected_avg_m2 = 183.5130890052356
        msg = f'This is the expected result:...{expected_avg_m2} and you have:...{actual_avg_m2}'
        assert actual_avg_m2 == expected_avg_m2, msg

    def test_colo_file_creator(self, set_up):
        """Test the File Result Creator

        In this case it test the Buy.

        Parameters
        ----------
        set_up :
            Is the dataframe for all the tests

        Returns
        -------

        """

        df = set_up
        # Run function
        colo_table_creator(df, 'Casa', 'Buy', 'tests/table_creator/data/test.csv', True)

        # Test
        actual = os.path.isfile('tests/table_creator/data/test.csv')
        expected = 'tests/table_creator/data/test.csv'
        msg = f'This is the expected result:...{expected} and you have:...{actual}'
        assert actual, msg
