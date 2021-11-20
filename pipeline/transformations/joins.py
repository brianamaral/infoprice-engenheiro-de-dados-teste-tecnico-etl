import pandas as pd


def inner_join(
    left_dataframe: pd.DataFrame, right_dataframe: pd.DataFrame, key: str
) -> pd.DataFrame:

    return left_dataframe.merge(right=right_dataframe, on=key, how="inner")


def left_join(
    left_dataframe: pd.DataFrame, right_dataframe: pd.DataFrame, key: str
) -> pd.DataFrame:

    return left_dataframe.merge(right=right_dataframe, on=key, how="left")
