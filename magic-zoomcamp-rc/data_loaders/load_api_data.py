# import io
import pandas as pd
# import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    df_2022 = pd.DataFrame()

    taxi_dtypes = {
            'VendorID': pd.Int64Dtype(),
            'passenger_count': pd.Int64Dtype(),
            'trip_distance': float,
            'RatecodeID': pd.Int64Dtype(),
            'store_and_fwd_flag': str,
            'PULocationID': pd.Int64Dtype(),
            'DOLocationID': pd.Int64Dtype(),
            'payment_type': pd.Int64Dtype(),
            'fare_amount': float,
            'extra': float,
            'mta_tax': float,
            'tip_amount': float,
            'tolls_amount': float,
            'improvement_surcharge': float,
            'total_amount': float,
            'congestion_surcharge': float,
            'ehail_fee': float,
            'trip_type': pd.Int64Dtype(),
            'lpep_pickup_datetime': str,
            'lpep_dropoff_datetime': str
    }
    #parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    for month in months:
    #month = 12
        url= 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{}.parquet'.format(month)
        
        df_aux = pd.read_parquet(url)
        df_2022 = pd.concat([df_2022, df_aux])
    print('Shape of the resultating df with concat:', df_2022.shape)
    df_2022 = df_2022.astype(taxi_dtypes)
    print(df_2022.dtypes)
    return df_2022
    '''
    response = requests.get(url)

    return pd.read_csv(io.StringIO(response.text), sep=',')
    '''


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
