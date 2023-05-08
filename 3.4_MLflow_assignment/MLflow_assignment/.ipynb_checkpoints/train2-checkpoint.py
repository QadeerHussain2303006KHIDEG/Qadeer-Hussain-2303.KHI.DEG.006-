# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.datasets import load_wine
# from sklearn.svm import SVC
# from sklearn.metrics import f1_score
# from sklearn.preprocessing import StandardScaler

# def preprocess_data(data):
#     scaler = StandardScaler()
#     X_train = scaler.fit_transform(data.data)
#     y_train = data.target
#     return X_train, y_train

# def train_svm(X_train, y_train):
#     clf = SVC(kernel='linear')
#     clf.fit(X_train, y_train)
#     return clf

# def evaluate_svm(clf, X_test, y_test):
#     y_pred = clf.predict(X_test)
#     f1 = f1_score(y_test, y_pred, average='micro')
#     return f1

# def main(file_name: str, max_k: int):
#     wine = load_wine()
#     X_train, y_train = preprocess_data(wine)
#     X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2)

#     clf = train_svm(X_train, y_train)
#     f1 = evaluate_svm(clf, X_test, y_test)
    
#     print(f"F1 Score: {f1}")

# if __name__ == "__main__":
#     file_name = "wine_dataset.csv"  # Replace with the actual path to your data file
#     max_k = 10  # Set the maximum value of k

#     main(file_name, max_k)











import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from sklearn.svm import SVC
from sklearn.metrics import f1_score
from sklearn.preprocessing import StandardScaler

def preprocess_data(df: pd.DataFrame):
    scaler = StandardScaler()
    X_train = scaler.fit_transform(df)
    y_train = df.target
    return X_train, y_train

def train_svm(X_train, y_train):
    clf = SVC(kernel='linear')
    clf.fit(X_train, y_train)
    return clf

def evaluate_svm(clf, X_test, y_test):
    y_pred = clf.predict(X_test)
    f1 = f1_score(y_test, y_pred, average='micro')
    return f1

def main(file_name: str):
#     wine = load_wine()
#     X_train, y_train = preprocess_data(wine)
#     X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2)
    df = preprocess_data(pd.read_csv(file_name))

    X_train, X_test, Y_train, Y_test = split_data(df)
    
    
    with mlflow.start_run():
        clf = train_svm(X_train, y_train)
        f1 = evaluate_svm(clf, X_test, y_test)
        
            # Log parameters and metrics with MLflow
        mlflow.log_param("file_name", file_name)
        mlflow.log_metric("f1_score", f1)

            # Save the trained model
        mlflow.sklearn.log_model(clf, "svm_model",registered_model_name="sklearn_svm")

        print(f"F1 Score: {f1}")
        print("Model saved with run_id:", mlflow.active_run().info.run_id)

if __name__ == "__main__":
    file_name = "wine_dataset.csv"  # Replace with the actual path to your data file
   
    

    main(file_name)
