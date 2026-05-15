from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
from src.logger import setup_logger

logger = setup_logger()

def run_pipeline():
    try:
        logger.info("🚀 Pipeline iniciado")

        df = extract_data()
        logger.info(f"Dados extraídos: {len(df)} linhas")

        df_transformed = transform_data(df)
        logger.info("Transformação concluída")

        load_data(df_transformed, "data/processed/clientes_tratados.csv")
        logger.info("Carga no MySQL concluída")

        logger.info("✅ Pipeline finalizado com sucesso")

    except Exception as e:
        logger.error(f"❌ Erro no pipeline: {e}")

run_pipeline()