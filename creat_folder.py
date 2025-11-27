import os

folders = [
    "configs",
    "configs/airflow",
    "configs/models",
    "data",
    "data/raw",
    "data/news",
    "data/prices",
    "data/features",
    "data/externals",
    "notebooks",
    "src",
    "src/app",
    "src/ingest",
    "src/ingest/parsers",
    "src/pipeline",
    "src/pipeline/dags",
    "src/nlp",
    "src/features",
    "src/models",
    "src/backtest",
    "src/risk",
    "src/api",
    "src/api/routers",
    "src/dashboard",
    "src/dashboard/components",
    "src/alerts",
    "src/alerts/templates",
    "src/db",
    "src/storage",
    "src/utils",
    "src/tests",
    "src/tests/unit",
    "src/tests/integration",
    "models",
    "models/finbert",
    "models/xgboost",
    "scripts",
    "deployments",
    "deployments/docker",
    "deployments/k8s",
    "deployments/terraform",
    "deployments/helm",
    "infra",
    "infra/db",
    "infra/monitoring",
    "infra/monitoring/grafana_dashboards",
    "ci",
    "docs"
]

files = {
    "README.md": "# FinTech NLP + Prediction + Portfolio Optimization System\n",
    "requirements.txt": "",
    ".gitignore": "",
    "docker-compose.yml": "",
    ".env.example": "",
    "configs/app_config.yaml": "",
    "configs/logging.yml": "",
    "configs/models/finbert.yaml": "",
    "configs/models/xgboost.yaml": "",
    "src/app/main.py": "",
    "src/ingest/news_scraper.py": "",
    "src/nlp/finbert_model.py": "",
    "src/api/main.py": "",
    "src/dashboard/streamlit_app.py": "",
    "docs/architecture.md": "",
    "docs/data_dictionary.md": "",
    "docs/runbook.md": "",
    "docs/API_DOCUMENTATION.md": "",
}

def create_structure():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    for file_path, content in files.items():
        with open(file_path, "w") as f:
            f.write(content)
        print(f"Created file: {file_path}")

    print("\n✨ Project structure created successfully!")


if __name__ == "__main__":
    create_structure()
