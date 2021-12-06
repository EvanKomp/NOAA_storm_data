import pandas as pd
_2018 = pd.read_csv('./data/StormEvents_details-ftp_v1.0_d2018_c20211120.csv')
_2005 = pd.read_csv('./data/StormEvents_details-ftp_v1.0_d2005_c20210803.csv')
df = pd.concat([_2005, _2018])

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

df_ = clean_raw_csv(df)
# df_.dropna(inplace=True)

df_.to_csv('cleaned_data.csv')
