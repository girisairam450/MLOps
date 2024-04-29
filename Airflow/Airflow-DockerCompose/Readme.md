## Steps to start Airflow using docker compose
1. Download the docker-compose file from the airflow repository `https://airflow.apache.org/docs/apache-airflow/2.8.4/docker-compose.yaml`.
2. We need to init the environment using `docker-compose up airflow-init`.
3. Run the airflow using `docker-compose up`.
4. To clean up run `docker compose down --volumes --remove-orphans`


