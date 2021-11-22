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

from transformations.column_transformations import select_columns

from transformations.joins import inner_join, left_join

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

      
    validated_scans = inner_join(
        left_dataframe=scaned_codes_dataframe, right_dataframe=gs1_dataframe, key="gtin"
    ) 

     

    validated_scans = inner_join(
        left_dataframe=validated_scans,
        right_dataframe=cnpj_dataframe,
        key="cnpj",
    )


    validated_scans = left_join(
        left_dataframe=validated_scans,
        right_dataframe=external_descriptions_dataframe,
        key="gtin",
    )

    validated_scans = select_columns(
        dataframe=validated_scans,
        columns=
            [
                "gtin",
                "cnpj",
                "razao_social",
                "cidade",
                "estado",
                "category",
                "description",
            ]
            
    )

    validated_scans = validated_scans.rename(
        columns={"category": "categoria", "description": "descricao"}
    )

    validated_scans.to_csv(
        path_or_buf="data/output/gtins_vendidos.tsv", sep="\t", index=False
    )
    