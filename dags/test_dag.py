from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("AIRFLOW ESTA FUNCIONANDO 🚀")

with DAG(
    dag_id="teste_airflow",
    start_date=datetime(2024,1,1),
    schedule_interval=None,
    catchup=False
) as dag:

    tarefa = PythonOperator(
        task_id="print_hello",
        python_callable=hello
    )