from pandas import DataFrame

def filter_nan(dataframe: DataFrame, column: str) -> DataFrame:
    return dataframe[dataframe[column].notna()]

def filter_ok_status(dataframe: DataFrame) -> DataFrame:
    
    return dataframe.loc[dataframe["status"] == "OK"]