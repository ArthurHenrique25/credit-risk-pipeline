from extract import extract_data
from transform import transform_data
from load import load_data
from logger import logger

def run_pipeline():
    logger.info("Pipeline iniciado")

    df = extract_data("data/raw/clientes.csv")
    logger.info(f"Dados extraídos: {len(df)} linhas")

    df_transformed = transform_data(df)
    logger.info("Transformação concluída")

    load_data(df_transformed)
    logger.info("Dados carregados no MySQL")

    logger.info("Pipeline finalizado com sucesso")
    
if __name__ == "__main__":
    run_pipeline()