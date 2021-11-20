import pandas as pd
import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
def select_columns(dataframe: pd.DataFrame, columns: list) -> pd.DataFrame:
    logging.info(f"selecting columns: {columns}")
    return dataframe[columns]
