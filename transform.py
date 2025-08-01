import transform_funcs as td
import pandas as pd

def transform_data(data: dict, *args, **kwargs) -> pd.DataFrame:
    hourly_data = data['forecast']['forecastday'][0]['hour']
    df = pd.json_normalize(hourly_data)

    df['location'] = data['location']['name']
    df['country'] = data['location']['country']
    df['date'] = data['forecast']['forecastday'][0]['date']

    df.columns = [td.normalize_cols(col) for col in df.columns]
    df = td.replace_nan(df)
    df = td.clean_str_convertation(df)
    
    return df