from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    "list_organization_latest_workflows",
    default_args={
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    description="A simple tutorial DAG",
    schedule=timedelta(days=1),
    catchup=False,
    tags=["github"]
) as dag:    
    t1 = BashOperator(task_id="", bash_command="ls -l")
    t1