import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # renda disponível após dívidas
    df["renda_liquida"] = df["salario"] - df["dividas"]

    # percentual de uso do limite
    df["uso_limite"] = df["dividas"] / df["limite_cartao"]

    # score simples de risco
    df["score_risco"] = (
        df["atrasos_pagamento"] * 0.5 +
        df["uso_limite"] * 0.3 -
        (df["renda_liquida"] / 10000) * 0.2
    )

    return df

print(f"Transformando dados")