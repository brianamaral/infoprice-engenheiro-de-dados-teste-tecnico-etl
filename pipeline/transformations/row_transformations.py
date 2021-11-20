from pandas import DataFrame


def filter_nan(dataframe: DataFrame, column: str) -> DataFrame:
    return dataframe[dataframe[column].notna()]


def filter_ok_status(dataframe: DataFrame) -> DataFrame:

    return dataframe.loc[dataframe["status"] == "OK"]


def filter_boolean_column(dataframe: DataFrame, column: str) -> DataFrame:
    return dataframe.loc[dataframe[column] == True]
