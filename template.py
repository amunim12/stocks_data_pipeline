import os
from pathlib import Path

list_of_files = [
    "airflow/__init__.py",
    "airflow/dags/__init__.py",
    "airflow/dags/ingestion_dag.py",
    "airflow/dags/processing_dag.py",
    "airflow/dags/redshift_dag.py",
    "airflow/plugins/__init__.py",
    "airflow/plugins/s3_uploader.py",
    "airflow/plugins/kafka_consumer.py",
    "airflow/docker-compose.yaml",
    "airflow/requirements.txt",
    "config/__init__.py",
    "config/airflow.cfg",
    "config/connections.yaml",
    "config/kubernetes_config.yaml",
    "data_ingestion/__init__.py",
    "data_ingestion/fetch_api_data.py",
    "data_ingestion/fetch_db_data.py",
    "data_processing/__init__.py",
    "data_processing/transform_data.py",
    "data_processing/deduplicate_data.py",
    "data_processing/validate_schema.py",
    "redshift_loader/__init__.py",
    "redshift_loader/load_to_redshift.py",
    "redshift_loader/redshift_queries.py",
    "pipelines/__init__.py",
    "pipelines/ingestion.py",
    "pipelines/processing.py",
    "pipelines/redshift.py",
    "ci-cd/githubactions/build.yml",
    "ci-cd/githubactions/security_scan.yml",
    "ci-cd/argo_cd/app.yaml",
    "ci-cd/argo_cd/customize.yaml"
    "ci-cd/terraform/main.tf",
    "ci-cd/terraform/s3.tf",
    "ci-cd/terraform/redshift.tf",
    "ci-cd/terraform/eks.tf",
    "ci-cd/terraform/ouput.tf",
    "kubernetes/deployment.yaml",
    "kubernetes/service.yaml",
    "kubernetes/ingress.yaml",
    "security/__init__.py",
    "security/iam_policy.json",
    "security/secrets_manager.py",
    "security/vulnerability_scan.sh",
    "tests/__init__.py",
    "tests/test_ingestion.py",
    "tests/test_processing.py",
    "tests/test_redshift.py",
    "scripts/start_airflow.sh",
    "scripts/cleanup_s3.sh",
    "scripts/deploy_k8s.sh",
    "pyproject.toml",
    "tox.ini",
    "requirements.txt",
    "Dockerfile",
    "Makefile",
    ".pre_commit-config.yaml",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filename)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass 