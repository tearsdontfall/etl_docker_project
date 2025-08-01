import pandas as pd
import os
from dotenv import load_dotenv
import json
from extract import extract_data

load_dotenv()

params = {
    "key": os.getenv("API_KEY"),
    "dt": "2025-07-30",
    "q": "Moscow"

}

test = extract_data(params)
print(type(test))


