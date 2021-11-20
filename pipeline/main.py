import pandas as pd

from transformations.response_transformations import (
    get_city,
    get_name,
    get_state,
    is_status_ok,
)
from transformations.row_transformations import (
    filter_nan,
    filter_ok_status,
    filter_boolean_column,
)

from preprocess_pipelines.pipelines import preprocess_gs1, preprocess_cnpj

if __name__ == "__main__":

    scaned_codes_dataframe = pd.read_csv("data/input/infomix.tsv", sep="\t")

    gs1_dataframe = pd.read_json("data/input/gs1.jl", lines=True)
    gs1_dataframe = preprocess_gs1(gs1_dataframe)

    cnpj_dataframe = pd.read_json("data/input/cnpjs_receita_federal.jl", lines=True)
    cnpj_dataframe = preprocess_cnpj(cnpj_dataframe)

    external_descriptions_dataframe = pd.read_csv(
        "data/input/descricoes_externas.tsv", sep="\t"
    )

    external_descriptions_dataframe = filter_boolean_column(
        dataframe=external_descriptions_dataframe, column="flag_infoprice"
    )

    validated_scans = scaned_codes_dataframe.merge(gs1_dataframe, on="gtin")

    validated_scans["cnpj_manufacturer"] = validated_scans["cnpj_manufacturer"].apply(
        lambda x: int(x)
    )

    validated_scans = validated_scans.merge(cnpj_dataframe, on="cnpj_manufacturer")

    validated_scans = validated_scans.merge(
        external_descriptions_dataframe, on="gtin", how="left"
    )

    validated_scans = validated_scans[
        ["gtin", "cnpj", "razao_social", "cidade", "estado", "category", "description"]
    ]

    validated_scans.columns = [
        "gtin",
        "cnpj",
        "razao_social",
        "cidade",
        "estado",
        "categoria",
        "descricao",
    ]

    validated_scans.to_csv(
        path_or_buf="data/output/gtins_vendidos.tsv", sep="\t", index=False
    )
