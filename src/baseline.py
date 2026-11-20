import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn

# Simple placeholder: load CSV if exists
data_path = "../data/raw/dataset.csv"
if not os.path.exists(data_path):
    print(f"Data not found at {data_path}. Please place a CSV file there.")
    exit(1)

df = pd.read_csv(data_path)
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)

print(f"Baseline accuracy: {acc:.4f}")

# Log with MLflow
mlflow.set_experiment("baseline")
with mlflow.start_run():
    mlflow.log_params({"model": "LogisticRegression", "max_iter": 1000})
    mlflow.log_metric("accuracy", acc)
    mlflow.sklearn.log_model(model, "model")
