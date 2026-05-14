# credit-risk-pipeline
📂 Arquitetura do Projeto
credit-risk-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── pipeline.py
│   ├── database.py
│   └── logger.py
│
├── .env
├── requirements.txt
└── README.md
⚙️ Como executar o projeto

1️⃣ Instalar dependências

pip install -r requirements.txt

2️⃣ Criar banco MySQL

CREATE DATABASE credit_risk;

3️⃣ Configurar variáveis de ambiente (.env)

DB_USER=***
DB_PASSWORD=***
DB_HOST=***
DB_PORT=***
DB_NAME=credit_risk

4️⃣ Executar pipeline

python src/pipeline.py
📊 Pipeline

Etapas executadas:

Extração de dados CSV
Transformação e limpeza
Criação de logs
Carga no MySQL
🧾 Exemplo de Log
2026-01-01 15:32:10 - INFO - Pipeline iniciado
2026-01-01 15:32:10 - INFO - Dados extraídos: 5000 linhas
2026-01-01 15:32:11 - INFO - Transformação concluída
2026-01-01 15:32:11 - INFO - Dados carregados no MySQL
2026-01-01 15:32:11 - INFO - Pipeline finalizado com sucesso