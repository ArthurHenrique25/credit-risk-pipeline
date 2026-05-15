import pandas as pd

print("📥 EXTRAINDO DADOS...")

dados = {
    "cliente": ["Ana", "Bruno", "Carlos"],
    "score": [650, 720, 580],
}

df = pd.DataFrame(dados)
df.to_csv("/tmp/dados_brutos.csv", index=False)

print("Dados extraídos com sucesso!")