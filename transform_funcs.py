import pandas as pd
import re
import numpy as np

def normalize_cols(cols: str) -> str:
    cols = re.sub(r"[ .,-?/'&$#]", '_', cols)
    cols = re.sub(r"[_]+", '_', cols)
    
    return cols.lower()

def replace_nan(df:pd.DataFrame) -> pd.DataFrame:

    """
    Обрабатываем пустые значения
    """

    values_to_nan = ['--', '', 'none', 'NaN', 'None', 'NONE', 'nan', None]
    df.replace(values_to_nan, np.nan, inplace=True)

    df.dropna(how='all', inplace=True)
    df.fillna('', inplace=True)

    return df

def clean_str_convertation(df:pd.DataFrame) -> pd.DataFrame:
    """
    Конвертируем колонки в str с приведением чисел
    """

    def convert(x):
        try:
            if isinstance(x, (list, dict, pd.Series, np.ndarray)):
                return str(x)
            elif isinstance(x, float) and x.is_integer():
                return str(int(x))
            elif isinstance(x, float):
                return f"{x:.15f}".rstrip('0').rstrip('.')
            elif isinstance(x, int):
                return str(x)
            elif isinstance(x, str):
                return x
            elif pd.isna(x):
                return ''
            return str(x)
        except Exception as e:
            print(f"Ошибка при обработке значения: {x} ({type(x)}) — {e}")
            raise  # пробрасываем дальше, чтобы не проглотить исключение
    return df.map(convert)

