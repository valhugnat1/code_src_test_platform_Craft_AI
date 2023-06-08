from io import BytesIO

import joblib
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from craft_ai_sdk import CraftAiSdk


def train(
    train_val_prop: float,
    model_parameters: dict,
    dataset_p: str,
):

    sdk = CraftAiSdk()

    f = BytesIO()
    sdk.download_data_store_object(
        object_path_in_datastore=dataset_p, filepath_or_buffer=f
    )
    dataset_df = pd.read_parquet(f)

    X = dataset_df.loc[:, dataset_df.columns != "target"].values
    y = dataset_df.loc[:, "target"].values

    np.random.seed(0)
    indices = np.random.permutation(len(X))

    n_train_samples = int(train_val_prop * len(X))
    train_indices = indices[:n_train_samples]
    val_indices = indices[n_train_samples:]

    X_train = X[train_indices]
    y_train = y[train_indices]
    X_val = X[val_indices]
    y_val = y[val_indices]

    knn = KNeighborsClassifier(**model_parameters)
    knn.fit(X_train, y_train)

    mean_accuracy = knn.score(X_val, y_val)
    metrics_dict = {"accuracy": mean_accuracy}

    joblib.dump(knn, 'model.pkl', compress=9)

    # sdk.upload_data_store_object(model_buffer, model_output)

    return {"metrics": metrics_dict,
            "model_output" : {"path": "model.pkl"}}