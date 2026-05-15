import pandas as pd
import mysql.connector

print("💾 CARREGANDO NO MYSQL...")

df = pd.read_csv("/tmp/dados_tratados.csv")

conn = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="credit_risk"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    nome VARCHAR(50),
    score INT,
    aprovado BOOLEAN
)
""")

for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO clientes VALUES (%s, %s, %s)",
        (row["cliente"], int(row["score"]), bool(row["aprovado"]))
    )

conn.commit()
conn.close()

print("Carga finalizada 🚀")