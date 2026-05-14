from src.database import get_engine

engine = get_engine()

with engine.connect() as conn:
    print("Conectado com sucesso 🚀")