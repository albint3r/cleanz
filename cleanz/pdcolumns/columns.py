import pandas as pd


def set_sector_inmob(data: pd.DataFrame) -> pd.DataFrame:
    """Apply the function segment sector inmob to all the rows to create a new column
    named sector_inmo.

    Parameters
    ----------
    data : pd.DataFrame :
        Is the dataframe that would have the New Column

    Returns
    -------
    pd.DataFrame
    
    """

    df = data
    df['sector_inmo'] = df.apply(lambda row: segment_sector_inmo(row.loc['tipo_oferta'], row.loc['price']),
                                       axis=1)

    return df


def segment_sector_inmo(tipo_oferta: str, price: float) -> str:
    """Select the text that would be insert in the new column sector inmobiliario.

    This function works with the funcition set_sector_inmo, that use the apply method in pandas
    to add the value.

    Parameters
    ----------
    tipo_oferta : str:
        This is a text row inside the column tipo_oferta
        
    price : float:
        This is a number row inside the column price
        

    Returns
    -------
    str
    
    """

    tipo_oferta = tipo_oferta
    price = price

    # Validate if is a Sale
    if 'Buy' == tipo_oferta or tipo_oferta == 'Venta':

        # Depend of the price_col of the listing assign a value.
        if price <= 1000000:
            sector_inmobilia = 'Interés Social'

        if 1000001 <= price <= 3000000:
            sector_inmobilia = 'Interés Medio'

        if 3000001 <= price <= 7000000:
            sector_inmobilia = 'Residencial'

        if 7000001 <= price <= 15000000:
            sector_inmobilia = 'Residencial Plus'

        if 15000001 <= price:
            sector_inmobilia = 'Premium'

    # Validate if is a Apartment
    if tipo_oferta == 'Rent' or tipo_oferta == 'Renta':
        # Depend of the price_col of the listing assign a value.
        if 5000 >= price:
            sector_inmobilia = 'Interés Social'

        if 5001 <= price <= 10000:
            sector_inmobilia = 'Interés Medio'

        if 10001 <= price <= 15000:
            sector_inmobilia = 'Residencial'

        if 15001 <= price <= 30000:
            sector_inmobilia = 'Residencial Plus'

        if 30001 <= price:
            sector_inmobilia = 'Premium'

    return sector_inmobilia



