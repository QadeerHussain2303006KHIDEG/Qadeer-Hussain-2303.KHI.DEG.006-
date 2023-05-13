import fire
import mlflow
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import f1_score
from sklearn.preprocessing import StandardScaler
def preprocess_data(data):
    scaler = StandardScaler()
    X_train = scaler.fit_transform(data.data)
    y_train = data.target
    return X_train, y_train
def train_svm(X_train, y_train):
    clf = SVC(kernel='linear')
    clf.fit(X_train, y_train)
    return clf
def evaluate_svm(clf, X_test, y_test):
    y_pred = clf.predict(X_test)
    f1 = f1_score(y_test, y_pred, average='micro')
    return f1
def track_with_mlflow(f1, model_metadata):
    mlflow.log_params(model_metadata)
    mlflow.log_metric("f1_score", f1)
    mlflow.sklearn.log_model(f1, "svm", registered_model_name="sklearn_svm")
def main(file_name: str, max_k: int):
    df = preprocess_data(pd.read_csv(file_name))

    X_train, X_test, Y_train, Y_test = train_test_split(df.iloc[:, :-1], df.iloc[:, -1], test_size=0.2)
    k_list = range(1, max_k)

    for k in k_list:
        with mlflow.start_run():
            knn_pipe = train_svm(k)
            knn_pipe.fit(X_train, Y_train)
            model_metadata = {"k": k}
            track_with_mlflow(knn_pipe, X_test, Y_test, mlflow, model_metadata)

if __name__ == "__main__":
    fire.Fire(main)