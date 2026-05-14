import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus

def get_engine():
    load_dotenv()

    user = os.getenv("DB_USER")
    raw_password = os.getenv("DB_PASSWORD")   # pega do .env
    password = quote_plus(raw_password)       # codifica a senha AGORA ✔
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    
    engine = create_engine(connection_string)
    return engine