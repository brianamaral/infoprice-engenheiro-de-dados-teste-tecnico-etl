import pandas as pd

from transformations.response_transformations import (
    get_city,
    get_name,
    get_state,
    is_status_ok,
)
from transformations.row_transformations import filter_nan, filter_ok_status

from preprocess_pipelines.pipelines import preprocess_gs1, preprocess_cnpj

if __name__ == "__main__":

    produtos_scaneados = pd.read_csv("data/input/infomix.tsv", sep="\t")

    gs1_dataframe = pd.read_json("data/input/gs1.jl", lines=True)
    gs1_dataframe = preprocess_gs1(gs1_dataframe)

    cnpj_dataframe = pd.read_json("data/input/cnpjs_receita_federal.jl", lines=True)
    cnpj_dataframe = preprocess_cnpj(cnpj_dataframe)

    descricoes_externas = pd.read_csv("data/input/descricoes_externas.tsv", sep="\t")

    descricoes_externas = descricoes_externas.loc[
        descricoes_externas["flag_infoprice"] == True
    ]

    produtos_validados = produtos_scaneados.merge(gs1_dataframe, on="gtin")

    produtos_validados["cnpj_manufacturer"] = produtos_validados[
        "cnpj_manufacturer"
    ].apply(lambda x: int(x))

    produtos_validados = produtos_validados.merge(
        cnpj_dataframe, on="cnpj_manufacturer"
    )

    produtos_validados = produtos_validados.merge(
        descricoes_externas, on="gtin", how="left"
    )

    produtos_validados = produtos_validados[
        ["gtin", "cnpj", "razao_social", "cidade", "estado", "category", "description"]
    ]

    produtos_validados.columns = [
        "gtin",
        "cnpj",
        "razao_social",
        "cidade",
        "estado",
        "categoria",
        "descricao",
    ]

    produtos_validados.to_csv(
        path_or_buf="data/output/gtins_vendidos.tsv", sep="\t", index=False
    )
