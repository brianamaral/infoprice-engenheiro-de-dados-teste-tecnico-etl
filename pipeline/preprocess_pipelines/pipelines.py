import pandas as pd

from transformations.response_transformations import (
    is_status_ok,
    get_city,
    get_state,
    get_name,
)
from transformations.row_transformations import filter_ok_status, filter_nan


def preprocess_gs1(gs1_dataframe: pd.DataFrame) -> pd.DataFrame:

    gs1_dataframe["status"] = gs1_dataframe["response"].apply(is_status_ok)

    gs1_dataframe = filter_ok_status(dataframe=gs1_dataframe)

    gs1_dataframe = filter_nan(dataframe=gs1_dataframe, column="cnpj_manufacturer")

    gs1_dataframe["cidade"] = gs1_dataframe["response"].apply(get_city)

    gs1_dataframe["estado"] = gs1_dataframe["response"].apply(get_state)

    return gs1_dataframe


def preprocess_cnpj(cnpj_dataframe: pd.DataFrame) -> pd.DataFrame:

    cnpj_dataframe["status"] = cnpj_dataframe["response"].apply(is_status_ok)

    cnpj_dataframe = filter_ok_status(dataframe=cnpj_dataframe)

    cnpj_dataframe = cnpj_dataframe.rename(columns={"cnpj": "cnpj_manufacturer"})

    cnpj_dataframe["razao_social"] = cnpj_dataframe["response"].apply(get_name)

    return cnpj_dataframe
