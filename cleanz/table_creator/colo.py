import pandas as pd


def colo_table_creator(dataframe: pd.DataFrame, tipo_inmueble: str, tipo_oferta: str,
                       name_final_csv: str = 'colonias.csv', create_csv: bool = True) -> pd.DataFrame:
    """Create a Table of the general stats of the neighborhood

    Parameters
    ----------
    dataframe: pd.DataFrame :
        
    tipo_inmueble: str :
        
    tipo_oferta: str :
        
    name_final_csv: str :
         (Default value = 'colonias.csv')

    create_csv: bol
        (Default value = True)

    Returns
    -------
    pd.DataFrame

    """

    # Setup the General Filters for the Table result
    tipo_inmueble = dataframe.tipo_inmueble == tipo_inmueble
    tipo_oferta = dataframe.tipo_oferta == tipo_oferta

    # Create a List to iterate of the neighbors
    colonias = dataframe.loc[(tipo_inmueble & tipo_oferta), 'colonia'].unique()

    list_of_colonias = []  # <- Save all the colonias to concatenate at the end
    for colonia_name in colonias:
        # Select the target colonia to create a subset
        colonia = dataframe.colonia == colonia_name

        colonia_subset = dataframe.loc[(colonia & tipo_oferta & tipo_inmueble)]

        # Separate the Statistics Values: Just for make it more readable

        # General Data
        total_listings = colonia_subset['colonia'].count()
        estado = colonia_subset.estado.mode()[0]
        municipio = colonia_subset.municipio.mode()[0]
        moda_fecha_pub = colonia_subset['fecha_pub'].dt.year.mode()[0]

        # Price Data
        avg_price = colonia_subset['price'].mean()
        median_price = colonia_subset['price'].median()
        max_price = colonia_subset['price'].max()
        min_price = colonia_subset['price'].min()
        std_price = colonia_subset['price'].std()

        # Price m2 Data
        avg_price_m2 = colonia_subset['price_m2'].mean()
        median_price_m2 = colonia_subset['price_m2'].median()
        max_price_m2 = colonia_subset['price_m2'].max()
        min_price_m2 = colonia_subset['price_m2'].min()
        std_price_m2 = colonia_subset['price_m2'].std()

        # Price Const Data
        avg_price_const = colonia_subset['price_const'].mean()
        median_price_const = colonia_subset['price_const'].median()
        max_price_const = colonia_subset['price_const'].max()
        min_price_const = colonia_subset['price_const'].min()
        std_price_const = colonia_subset['price_const'].std()

        # M2 Terreno
        avg_m2 = colonia_subset['m2_terreno'].mean()
        median_m2 = colonia_subset['m2_terreno'].median()
        max_m2 = colonia_subset['m2_terreno'].max()
        min_m2 = colonia_subset['m2_terreno'].min()
        std_m2 = colonia_subset['m2_terreno'].std()

        # M2 Const
        avg_const = colonia_subset['m2_const'].mean()
        median_const = colonia_subset['m2_const'].median()
        max_const = colonia_subset['m2_const'].max()
        min_const = colonia_subset['m2_const'].min()
        std_const = colonia_subset['m2_const'].std()

        # Habitaciones
        avg_hab = colonia_subset['habitaciones'].mean()
        median_hab = colonia_subset['habitaciones'].median()
        max_hab = colonia_subset['habitaciones'].max()
        min_hab = colonia_subset['habitaciones'].min()
        std_hab = colonia_subset['habitaciones'].std()
        mode_hab = colonia_subset['habitaciones'].mode()[0]

        # Banos
        avg_banos = colonia_subset['banos'].mean()
        median_banos = colonia_subset['banos'].median()
        max_banos = colonia_subset['banos'].max()
        min_banos = colonia_subset['banos'].min()
        std_banos = colonia_subset['banos'].std()
        mode_banos = colonia_subset['banos'].mode()[0]

        # Autos
        avg_autos = colonia_subset['autos'].mean()
        median_autos = colonia_subset['autos'].median()
        max_autos = colonia_subset['autos'].max()
        min_autos = colonia_subset['autos'].min()
        std_autos = colonia_subset['autos'].std()
        mode_autos = colonia_subset['autos'].mode()[0]

        # Create a dict to append in a list and then concatenate.
        new_df = {
            'colonia': colonia_name,
            'total_listings': total_listings,
            'estado': estado,
            'municipio': municipio,
            'moda_fecha_pub': moda_fecha_pub,
            'avg_price': avg_price,
            'median_price': median_price,
            'max_price': max_price,
            'min_price': min_price,
            'std_price': std_price,
            'avg_price_m2': avg_price_m2,
            'median_price_m2': median_price_m2,
            'max_price_m2': max_price_m2,
            'min_price_m2': min_price_m2,
            'std_price_m2': std_price_m2,
            'avg_price_const': avg_price_const,
            'median_price_const': median_price_const,
            'max_price_const': max_price_const,
            'min_price_const': min_price_const,
            'std_price_const': std_price_const,
            'avg_m2': avg_m2,
            'median_m2': median_m2,
            'max_m2': max_m2,
            'min_m2': min_m2,
            'std_m2': std_m2,
            'avg_const': avg_const,
            'median_const': median_const,
            'max_const': max_const,
            'min_const': min_const,
            'std_const': std_const,
            'avg_hab': avg_hab,
            'median_hab': median_hab,
            'max_hab': max_hab,
            'min_hab': min_hab,
            'std_hab': std_hab,
            'mode_hab': mode_hab,
            'avg_banos': avg_banos,
            'median_banos': median_banos,
            'max_banos': max_banos,
            'min_banos': min_banos,
            'std_banos': std_banos,
            'mode_banos': mode_banos,
            'avg_autos': avg_autos,
            'median_autos': median_autos,
            'max_autos': max_autos,
            'min_autos': min_autos,
            'std_autos': std_autos,
            'mode_autos': mode_autos,
        }

        list_of_colonias.append(new_df)

    # Concatenate all the data frames
    df_result = pd.DataFrame(list_of_colonias)

    if create_csv:
        # Create a CSV of the results
        df_result.sort_values('colonia').to_csv(name_final_csv)

    return df_result
