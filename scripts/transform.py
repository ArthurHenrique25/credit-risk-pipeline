import pandas as pd

print("🔄 TRANSFORMANDO DADOS...")

df = pd.read_csv("/tmp/dados_brutos.csv")

df["aprovado"] = df["score"] >= 700

df.to_csv("/tmp/dados_tratados.csv", index=False)

print("Transformação concluída!")