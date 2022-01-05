import pandas as pd
import numpy as np
import os
import shutil
import pytest
from cleanz.pdcolumns.columns import segment_sector_inmo, set_sector_inmob


class TestColumns(object):
    """This test the Columns Function in pd Columns Module"""

    @pytest.fixture
    def setup(self):
        """Crate the setup dataframe that would be use to test the module columns """
        # Create a temporal directory for the File created by the function
        os.mkdir('tests/table_creator/data/')

        # Set the path of the listing
        data = 'data/clean_data/listing_17_12_2021.csv'

        yield pd.read_csv(data, parse_dates=['fecha_pub'])

        # Remove File Created by the function in the Data Directory inside the Test Directory
        shutil.rmtree('tests/table_creator/data/')

    def test_set_sector_inmob_col(self, setup: pd.DataFrame):
        """test the set_sector_inmob tha create to validate if the new column was
        created.

        Parameters
        ----------
        setup : pd.DataFrame
            This is the dataframe that would be use for all the test. It contains
            all tipo de inmueble and price that helps to segment de values
            and create the new column: sector_inmo.
            

        Returns
        -------

        """
        # Select tipo oferta and price
        df = setup

        df = set_sector_inmob(df)
        actual = pd.Series(df.columns, name = 'columns')
        expected = ['sector_inmo']
        msg = f'The expected value is: {expected} and you have {actual}'
        result = actual.isin(expected).any()
        assert result, msg

    def test_set_sector_inmob_values(self, setup: pd.DataFrame):
        """

        Parameters
        ----------
        setup : pd.DataFrame
            This is the dataframe that would be use for all the test. It contains
            all tipo de inmueble and price that helps to segment de values
            and create the new column: sector_inmo.
            

        Returns
        -------

        """
        # Select tipo oferta and price
        df = setup

        df = set_sector_inmob(df)
        actual = list(df.sector_inmo.unique())
        expected = ['Residencial Plus', 'Premium', 'Interés Medio', 'Residencial','Interés Social']
        msg = f'The expected value is: {expected} and you have {actual}'
        assert actual == expected, msg

    def test_segment_sector_inmo_social_buy(self, setup: pd.DataFrame):
        """

        Parameters
        ----------
        setup : pd.DataFrame
            This is the dataframe that would be use for all the test. It contains
            all tipo de inmueble and price that helps to segment de values
            and create the new column: sector_inmo.
            

        Returns
        -------

        """
        # Select tipo oferta and price
        df = setup

        # Select Segment: $ -> 1,000,000 and Buy
        df_segment = df[(df.price <= 1000000) & (df.tipo_oferta == 'Buy')]

        # Select a random index for the subset result
        random_index = np.random.randint(0, len(df_segment), 1)[0]
        index = df_segment.index[random_index]

        tipo_oferta = df_segment.loc[index, 'tipo_oferta']
        price = df_segment.loc[index, 'price']

        actual = segment_sector_inmo(tipo_oferta, price)
        expected = 'Interés Social'
        msg = f'The expected value is: {expected} and you have {actual}'
        assert actual == expected, msg

    def test_segment_sector_inmo_social_rent(self, setup: pd.DataFrame):
        """

        Parameters
        ----------
        setup : pd.DataFrame
            This is the dataframe that would be use for all the test. It contains
            all tipo de inmueble and price that helps to segment de values
            and create the new column: sector_inmo.
            

        Returns
        -------

        """
        # Select tipo oferta and price
        df = setup

        # Select Segment: $ -> 5,000 and Rent
        df_segment = df[(df.price <= 5000) & (df.tipo_oferta == 'Rent')]
        # Select a random index for the subset result
        random_index = np.random.randint(0, len(df_segment), 1)[0]
        index = df_segment.index[random_index]

        tipo_oferta = df_segment.loc[index, 'tipo_oferta']
        price = df_segment.loc[index, 'price']

        actual = segment_sector_inmo(tipo_oferta, price)
        expected = 'Interés Social'
        msg = f'The expected value is: {expected} and you have {actual}'
        assert actual == expected, msg

    def test_segment_sector_inmo_medio_buy(self, setup: pd.DataFrame):
        """

        Parameters
        ----------
        setup : pd.DataFrame
            This is the dataframe that would be use for all the test. It contains
            all tipo de inmueble and price that helps to segment de values
            and create the new column: sector_inmo.
            

        Returns
        -------

        """
        # Select tipo oferta and price
        df = setup

        # Select Segment: $ -> 1000001 & 3000000 and Buy
        df_segment = df[(df.price >= 1000001) & (df.price <= 3000000) \
                        & (df.tipo_oferta == 'Buy')]
        # Select a random index for the subset result
        random_index = np.random.randint(0, len(df_segment), 1)[0]
        index = df_segment.index[random_index]

        tipo_oferta = df_segment.loc[index, 'tipo_oferta']
        price = df_segment.loc[index, 'price']

        actual = segment_sector_inmo(tipo_oferta, price)
        expected = 'Interés Medio'
        msg = f'The expected value is: {expected} and you have {actual}'
        assert actual == expected, msg

    def test_segment_sector_inmo_medio_rent(self, setup: pd.DataFrame):
        """

        Parameters
        ----------
        setup : pd.DataFrame
            This is the dataframe that would be use for all the test. It contains
            all tipo de inmueble and price that helps to segment de values
            and create the new column: sector_inmo.
            

        Returns
        -------

        """
        # Select tipo oferta and price
        df = setup

        # Select Segment: $ -> 1000001 & 3000000 and Buy
        df_segment = df[(df.price >= 5001) & (df.price <= 10000) \
                        & (df.tipo_oferta == 'Rent')]
        # Select a random index for the subset result
        random_index = np.random.randint(0, len(df_segment), 1)[0]
        index = df_segment.index[random_index]

        tipo_oferta = df_segment.loc[index, 'tipo_oferta']
        price = df_segment.loc[index, 'price']

        actual = segment_sector_inmo(tipo_oferta, price)
        expected = 'Interés Medio'
        msg = f'The expected value is: {expected} and you have {actual}'
        assert actual == expected, msg

    def test_segment_sector_inmo_residencial_buy(self, setup: pd.DataFrame):
        """

        Parameters
        ----------
        setup : pd.DataFrame
            This is the dataframe that would be use for all the test. It contains
            all tipo de inmueble and price that helps to segment de values
            and create the new column: sector_inmo.
            

        Returns
        -------

        """
        # Select tipo oferta and price
        df = setup

        # Select Segment: $ -> 1000001 & 3000000 and Buy
        df_segment = df[(df.price >= 3000001) & (df.price <= 7000000) \
                        & (df.tipo_oferta == 'Buy')]
        # Select a random index for the subset result
        random_index = np.random.randint(0, len(df_segment), 1)[0]
        index = df_segment.index[random_index]

        tipo_oferta = df_segment.loc[index, 'tipo_oferta']
        price = df_segment.loc[index, 'price']

        actual = segment_sector_inmo(tipo_oferta, price)
        expected = 'Residencial'
        msg = f'The expected value is: {expected} and you have {actual}'
        assert actual == expected, msg

    def test_segment_sector_inmo_residencial_rent(self, setup: pd.DataFrame):
        """

        Parameters
        ----------
        setup : pd.DataFrame
            This is the dataframe that would be use for all the test. It contains
            all tipo de inmueble and price that helps to segment de values
            and create the new column: sector_inmo.
            

        Returns
        -------

        """
        # Select tipo oferta and price
        df = setup

        # Select Segment: $ -> 1000001 & 3000000 and Buy
        df_segment = df[(df.price >= 10001) & (df.price <= 15000) \
                        & (df.tipo_oferta == 'Rent')]
        # Select a random index for the subset result
        random_index = np.random.randint(0, len(df_segment), 1)[0]
        index = df_segment.index[random_index]

        tipo_oferta = df_segment.loc[index, 'tipo_oferta']
        price = df_segment.loc[index, 'price']

        actual = segment_sector_inmo(tipo_oferta, price)
        expected = 'Residencial'
        msg = f'The expected value is: {expected} and you have {actual}'
        assert actual == expected, msg

    def test_segment_sector_inmo_plus_buy(self, setup: pd.DataFrame):
        """

        Parameters
        ----------
        setup : pd.DataFrame
            This is the dataframe that would be use for all the test. It contains
            all tipo de inmueble and price that helps to segment de values
            and create the new column: sector_inmo.
            

        Returns
        -------

        """
        # Select tipo oferta and price
        df = setup

        # Select Segment: $ -> 1000001 & 3000000 and Buy
        df_segment = df[(df.price >= 7000001) & (df.price <= 15000000) \
                        & (df.tipo_oferta == 'Buy')]
        # Select a random index for the subset result
        random_index = np.random.randint(0, len(df_segment), 1)[0]
        index = df_segment.index[random_index]

        tipo_oferta = df_segment.loc[index, 'tipo_oferta']
        price = df_segment.loc[index, 'price']

        actual = segment_sector_inmo(tipo_oferta, price)
        expected = 'Residencial Plus'
        msg = f'The expected value is: {expected} and you have {actual}'
        assert actual == expected, msg

    def test_segment_sector_inmo_plus_rent(self, setup: pd.DataFrame):
        """

        Parameters
        ----------
        setup : pd.DataFrame
            This is the dataframe that would be use for all the test. It contains
            all tipo de inmueble and price that helps to segment de values
            and create the new column: sector_inmo.
            

        Returns
        -------

        """
        # Select tipo oferta and price
        df = setup

        # Select Segment: $ -> 1000001 & 3000000 and Buy
        df_segment = df[(df.price >= 15001) & (df.price <= 30000) \
                        & (df.tipo_oferta == 'Rent')]
        # Select a random index for the subset result
        random_index = np.random.randint(0, len(df_segment), 1)[0]
        index = df_segment.index[random_index]

        tipo_oferta = df_segment.loc[index, 'tipo_oferta']
        price = df_segment.loc[index, 'price']

        actual = segment_sector_inmo(tipo_oferta, price)
        expected = 'Residencial Plus'
        msg = f'The expected value is: {expected} and you have {actual}'
        assert actual == expected, msg

    def test_segment_sector_inmo_premium_buy(self, setup: pd.DataFrame):
        """

        Parameters
        ----------
        setup : pd.DataFrame
            This is the dataframe that would be use for all the test. It contains
            all tipo de inmueble and price that helps to segment de values
            and create the new column: sector_inmo.
            

        Returns
        -------

        """
        # Select tipo oferta and price
        df = setup

        # Select Segment: $ -> 1000001 & 3000000 and Buy
        df_segment = df[(df.price >= 15000001) & (df.tipo_oferta == 'Buy')]
        # Select a random index for the subset result
        random_index = np.random.randint(0, len(df_segment), 1)[0]
        index = df_segment.index[random_index]

        tipo_oferta = df_segment.loc[index, 'tipo_oferta']
        price = df_segment.loc[index, 'price']

        actual = segment_sector_inmo(tipo_oferta, price)
        expected = 'Premium'
        msg = f'The expected value is: {expected} and you have {actual}'
        assert actual == expected, msg

    def test_segment_sector_inmo_premium_rent(self, setup: pd.DataFrame):
        """

        Parameters
        ----------
        setup : pd.DataFrame
            This is the dataframe that would be use for all the test. It contains
            all tipo de inmueble and price that helps to segment de values
            and create the new column: sector_inmo.
            

        Returns
        -------

        """
        # Select tipo oferta and price
        df = setup

        # Select Segment: $ -> 1000001 & 3000000 and Buy
        df_segment = df[(df.price >= 30001) & (df.tipo_oferta == 'Rent')]
        # Select a random index for the subset result
        random_index = np.random.randint(0, len(df_segment), 1)[0]
        index = df_segment.index[random_index]

        tipo_oferta = df_segment.loc[index, 'tipo_oferta']
        price = df_segment.loc[index, 'price']

        actual = segment_sector_inmo(tipo_oferta, price)
        expected = 'Premium'
        msg = f'The expected value is: {expected} and you have {actual}'
        assert actual == expected, msg


