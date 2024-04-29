from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner':'Giri Ragam',
    'start_date': days_ago(0),
    'email':['girisairam4474@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay':timedelta(minutes=5)
}

dag = DAG(
    'my-first-dag',
    default_args = default_args,
    description = 'My First DAG',
    schedule_interval = timedelta(days=1)
)

extract = BashOperator(
    task_id = 'extract',
    bash_command = 'cut -d":" -f1,3,6 /etc/passwd > /opt/airflow/dags/extracted-data.txt',
    dag = dag
)

transform_and_load = BashOperator(
    task_id='transform',
    bash_command='tr ":" "," < /opt/airflow/dags/extracted-data.txt > /opt/airflow/dags/transformed-data.csv',
    dag=dag
)

extract >> transform_and_load