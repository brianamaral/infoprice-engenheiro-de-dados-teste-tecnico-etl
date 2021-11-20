import pandas as pd

from transformations.response_transformations import get_city, get_name, get_state, is_status_ok
from transformations.row_transformations import filter_nan, filter_ok_status

if __name__ == "__main__":

    # pipeline produtos scaneados
    produtos_scaneados = pd.read_csv("dados/infomix.tsv", sep="\t")

    # pipeline registros de gtin
    registros_de_gtin = pd.read_json("dados/gs1.jl", lines=True)

    registros_de_gtin["status"] = registros_de_gtin["response"].apply(is_status_ok)

    registros_de_gtin = filter_ok_status(dataframe=registros_de_gtin)

    registros_de_gtin = filter_nan(dataframe=registros_de_gtin,column="cnpj_manufacturer")

    registros_de_gtin["cidade"] = registros_de_gtin["response"].apply(get_city)

    registros_de_gtin["estado"] = registros_de_gtin["response"].apply(get_state)

    # pipeline base da receita
    base_da_receita = pd.read_json("dados/cnpjs_receita_federal.jl", lines=True)

    base_da_receita["status"] = base_da_receita["response"].apply(is_status_ok)

    base_da_receita = filter_ok_status(dataframe=base_da_receita)

    base_da_receita = base_da_receita.rename(columns={"cnpj": "cnpj_manufacturer"})

    base_da_receita["razao_social"] = base_da_receita["response"].apply(get_name)
    # pipeline descricoes externas
    descricoes_externas = pd.read_csv("dados/descricoes_externas.tsv", sep="\t")

    descricoes_externas = descricoes_externas.loc[
        descricoes_externas["flag_infoprice"] == True
    ]

    # merges
    produtos_validados = produtos_scaneados.merge(registros_de_gtin, on="gtin")

    produtos_validados["cnpj_manufacturer"] = produtos_validados[
        "cnpj_manufacturer"
    ].apply(lambda x: int(x))

    produtos_validados = produtos_validados.merge(
        base_da_receita, on="cnpj_manufacturer"
    )

    produtos_validados = produtos_validados.merge(
        descricoes_externas, on="gtin", how="left"
    )

    produtos_validados[
        ["gtin", "cnpj", "razao_social", "cidade", "estado", "category", "description"]
    ].to_csv(path_or_buf="gtins_vendidos.tsv", sep="\t", index=False)

    print(produtos_validados[
        ["gtin", "cnpj", "razao_social", "cidade", "estado", "category", "description"]
    ])
