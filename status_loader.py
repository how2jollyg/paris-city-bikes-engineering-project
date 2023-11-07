import io
import pandas as pd
import requests
import datetime as dt 
import json 

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def status_loader(*args,**kwargs):
        #loader function of station status API 
        url = 'https://velib-metropole-opendata.smoove.pro/opendata/Velib_Metropole/station_status.json'
        response = requests.get(url).json()

        df_data = pd.json_normalize(response['data']['stations'])

        #df_new = pd.DataFrame.from_dict(df_data['num_bikes_available_types']) 


        # Assuming you have a DataFrame df_data with the 'num_bikes_available_types' column
        # The 'num_bikes_available_types' column contains dictionaries

        df_data['ebike'] = df_data['num_bikes_available_types'].apply(lambda y: y[1]['ebike'] if y else 0)
        df_data['mechanical'] = df_data['num_bikes_available_types'].apply(lambda x: x[0]['mechanical'] if x else 0)
        print(df_data[['mechanical','ebike']])

        return df_data

@test 
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'