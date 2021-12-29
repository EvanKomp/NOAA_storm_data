import pandas as pd
import os
dfs = [pd.read_csv('./data/'+filename) for filename in os.listdir('./data')]
df = pd.concat(dfs)

def clean_raw_csv(df):
    df_ = df[
        [
            'BEGIN_DATE_TIME',
            'EVENT_TYPE',
            'INJURIES_DIRECT',
            'INJURIES_INDIRECT',
            'DEATHS_DIRECT',
            'DEATHS_INDIRECT',
            'DAMAGE_PROPERTY',
            'DAMAGE_CROPS',
            'BEGIN_LAT',
            'BEGIN_LON'
        ]
    ]
    df_.rename(columns={'BEGIN_LAT': 'LATITUDE', 'BEGIN_LON': 'LONGITUDE'}, inplace=True)
    df_.reset_index(inplace=True, drop=True)
    df_.dropna(inplace=True)
    print(len(df_))
    
    def numerical_price(inp):
        try:
            return float(inp)*1000
        except:
            return float(inp[:-1])*1000
    for column in df_.columns:
        if column.startswith('DAMAGE'):
            df_[column] = df_[column].astype(str).apply(lambda x: numerical_price(x))
    return df_

df_ = clean_raw_csv(df).sample(50000)
print(len(df_))

df_.to_csv('cleaned_data.csv')
