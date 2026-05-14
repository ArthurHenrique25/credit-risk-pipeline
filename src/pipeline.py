from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    df = extract_data("data/raw/clientes.csv")
    df_transformed = transform_data(df)
    load_data(df_transformed, "data/processed/clientes_tratados.csv")

if __name__ == "__main__":
    run_pipeline()