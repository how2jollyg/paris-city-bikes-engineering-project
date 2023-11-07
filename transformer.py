import io
import pandas as pd
import requests
import datetime as dt 
import json 

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

"""Transform code"""
#information change

@transformer
def transformer(df_data,df_data1):
    df_data1['rental_methods'] = df_data1['rental_methods'].fillna(value='SUBSCRIPTION')
    df_data1['rental_methods'] = [ x if x=='SUBSCRIPTION' else 'CREDITCARD' for x in df_data1['rental_methods']]

    #information dimension 
    information_dim = pd.DataFrame()
    information_dim['station_id'] = df_data1['station_id']
    information_dim['lat'] =df_data1['lat']
    information_dim['lon'] =df_data1['lon']
    information_dim['rental_methods'] =df_data1['rental_methods']
    information_dim['capacity'] = df_data1['capacity']

    #datetime dimension
    df_data['last_reported'] = pd.to_datetime(df_data['last_reported'], unit= 's')
    datetime_dim = pd.DataFrame()
    datetime_dim['last_reported_timestamp'] = df_data['last_reported']
    datetime_dim['date'] = datetime_dim['last_reported_timestamp'].dt.strftime('%Y-%m-%d')
    #print(datetime_dim['date'].dtypes)
    datetime_dim['day'] = datetime_dim['last_reported_timestamp'].dt.strftime('%d')
    datetime_dim['month'] = datetime_dim['last_reported_timestamp'].dt.strftime('%m')
    datetime_dim['year'] = datetime_dim['last_reported_timestamp'].dt.strftime('%Y')

    #removing columns
    
    df_data = df_data[['stationCode','station_id','num_bikes_available','mechanical',
    'ebike','num_docks_available','is_installed','is_returning','is_renting','last_reported',
    ]]

    fact_table = df_data.merge(information_dim, how = 'left', on='station_id') 
    fact_table['num_bikes_available1'] = fact_table['capacity'] - fact_table['num_docks_available']
    fact_table = fact_table[['stationCode','station_id','num_bikes_available','num_bikes_available1','mechanical',
    'ebike','num_docks_available','is_installed','is_returning','is_renting','last_reported',
    'lat','lon','rental_methods','capacity']]
    
    return {
    "datetime_dim":datetime_dim.to_dict(orient="dict"),
    "information_dim":information_dim.to_dict(orient="dict"),
    "fact_table":fact_table.to_dict(orient="dict")}
