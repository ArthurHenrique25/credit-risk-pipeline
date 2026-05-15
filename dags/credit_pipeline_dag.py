from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="pipeline_credito_etl",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    extract = BashOperator(
        task_id="extract",
        bash_command="docker compose run --rm credit-pipeline python scripts/extract.py"
    )

    transform = BashOperator(
        task_id="transform",
        bash_command="docker compose run --rm credit-pipeline python scripts/transform.py"
    )

    load = BashOperator(
        task_id="load",
        bash_command="docker compose run --rm credit-pipeline python scripts/load.py"
    )

    extract >> transform >> load