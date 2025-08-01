import pandas as pd
import random
import os
# from s3 import S3, ConfigFileLoader

# Путь до конфигурационного файла AWS (обычно ~/.aws/credentials)


def load_data_s3(df: pd.DataFrame, params: dict, random_key: str, *args, **kwargs):
    
    """
    НА ДАННЫЙ МОМЕНТ ЗАГРУЗКА ИММИТИРУЕТСЯ
    """

    bucket_name = "weather_daily"
    object_key = f"{params['q']}_{params['dt']}_{random_key}.parquet"
    
    config_profile = "default"
    # config_path = os.path.expanduser("~/.aws/credentials")

    print("Делаю backup файлов")
    if not os.path.isdir('data_backup'):
        os.mkdir('data_backup')
    df.to_parquet(f"data_backup/{object_key}", index=False)

    print(f"Загружаю объект {object_key}. Количество строк: {len(df)}")

    # # Экспорт в S3 как parquet
    # S3.with_config(ConfigFileLoader(config_path, config_profile)).export(
    #     df,
    #     bucket_name,
    #     object_key,
    #     format='parquet'
    # )