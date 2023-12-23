from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator

with DAG(
    "list_organization_latest_workflows",
    default_args={
        "depends_on_past": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5)
    },
    description="Lists latest workflows from an organization",
    schedule=timedelta(days=1),
    start_date=datetime(2023, 12, 23),
    catchup=False,
    tags=["github"]
) as dag:
    k = KubernetesPodOperator(
        name="hello-dry-run",
        image="debian",
        cmds=["bash", "-cx"],
        arguments=["echo", "10"],
        labels={"foo": "bar"},
        task_id="dry_run_demo",
        do_xcom_push=True,
    )

    k.dry_run()