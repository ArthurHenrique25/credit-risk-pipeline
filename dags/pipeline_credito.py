from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="pipeline_credito",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    rodar_pipeline = BashOperator(
        task_id="executar_pipeline_docker",
        bash_command="docker compose run --rm credit-pipeline"
    )

    rodar_pipeline