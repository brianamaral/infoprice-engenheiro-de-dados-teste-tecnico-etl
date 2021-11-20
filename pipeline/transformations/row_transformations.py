from pandas import DataFrame
import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

def filter_nan(dataframe: DataFrame, column: str) -> DataFrame:
    logging.info(f"filtering nan values from column {column}")
    return dataframe[dataframe[column].notna()]


def filter_ok_status(dataframe: DataFrame) -> DataFrame:
    logging.info(f"filtering ok status from dataframe")
    return dataframe.loc[dataframe["status"] == "OK"]


def filter_boolean_column(dataframe: DataFrame, column: str) -> DataFrame:
    logging.info(f"filtering boolena values from column {column}")
    return dataframe.loc[dataframe[column] == True]
