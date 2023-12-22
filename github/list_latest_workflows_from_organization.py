from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    "list_organization_latest_workflows",
    default_args = {
        description="A simple tutorial DAG",
        schedule=timedelta(days=1),
        catchup=False,
        tags=["github"]
    }
) as dag:    
    t1 = BashOperator(task_id="", bash_command="ls -l")
    t1