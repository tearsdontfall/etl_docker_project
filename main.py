import pandas as pd
import os
from dotenv import load_dotenv
import json
from extract import extract_data
from datetime import datetime, timedelta
import transform_funcs as td
from transform import transform_data
from load import load_data_s3
import random
import string

load_dotenv()

params = {
    "key": os.getenv("API_KEY"),
    "dt": (datetime.now() + timedelta(hours=3) - timedelta(days=1)).strftime("%Y-%m-%d"),
    "q": "Moscow"

}

random_key = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

##Загружаем
data = extract_data(params)

##Трансформируем
data = transform_data(data)

##Загружаем (пока иммитируем)

load_data_s3(df=data, params=params, random_key=random_key)