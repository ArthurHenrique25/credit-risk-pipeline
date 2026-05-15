import pandas as pd
from src.database import get_engine

def load_data(df, path):
    print("Carregando no MySQL...")
    
    engine = get_engine()
    
    df.to_sql(
        "clientes_tratados",
        engine,
        if_exists="append",
        index=False
    )

    print("Dados carregados no MySQL com sucesso!")