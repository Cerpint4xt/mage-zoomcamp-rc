import re
import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def change_case(str):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    #data = data[data['passenger_count'] > 0]
    #data = data[data['trip_distance'] > 0]
    columns_list = []
    count = 0
    for column in data.columns:
        column_without_change = column
        column = change_case(column)
        column_with_change = column
        if column_without_change != column_with_change:
            count += 1
        
        columns_list.append(column)
    data.columns = columns_list

    data['lpep_pickup_datetime'] = pd.to_datetime(data['lpep_pickup_datetime'], format='%Y-%m-%dT%H:%M:%S')
    data['lpep_dropoff_datetime'] = pd.to_datetime(data['lpep_dropoff_datetime'], unit='ns')
    
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date # valid statement to create a column 
    print(data.dtypes)
    print('Number of column names changed:', count)
    print('Shape of data after transformation:', data.shape)
    print('Unique values of VendorID:', data.vendor_id.unique())
    
    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    #assert True if 'vendor_id' in output.columns else False == True

    #assert output['passenger_count'].isin([0]).sum() == 0, 'There is rides with zero passengers'
    #assert output['trip_distance'].isin([0]).sum() == 0, 'There is trip distance with zero distance