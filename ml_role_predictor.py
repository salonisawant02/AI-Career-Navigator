import pandas as pd
import os

from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder


def train_model():

    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    csv_path = os.path.join(
        current_dir,
        "data",
        "role_dataset.csv"
    )

    df = pd.read_csv(
        csv_path
    )

    X = df.drop(
        "role",
        axis=1
    )

    y = df["role"]

    encoder = LabelEncoder()

    y_encoded = encoder.fit_transform(
        y
    )

    model = DecisionTreeClassifier(
        random_state=42
    )

    model.fit(
        X,
        y_encoded
    )

    return model, encoder


def predict_role_ml(skills):

    model, encoder = train_model()

    features = {
        "python": 0,
        "sql": 0,
        "excel": 0,
        "power_bi": 0,
        "machine_learning": 0,
        "statistics": 0,
        "pandas": 0,
        "numpy": 0
    }

    for skill in skills:

        skill = skill.lower()

        if skill == "python":
            features["python"] = 1

        elif skill == "sql":
            features["sql"] = 1

        elif skill == "excel":
            features["excel"] = 1

        elif skill == "power bi":
            features["power_bi"] = 1

        elif skill == "machine learning":
            features["machine_learning"] = 1

        elif skill == "statistics":
            features["statistics"] = 1

        elif skill == "pandas":
            features["pandas"] = 1

        elif skill == "numpy":
            features["numpy"] = 1

    input_df = pd.DataFrame(
        [features]
    )

    prediction = model.predict(
        input_df
    )

    role = encoder.inverse_transform(
        prediction
    )[0]

    return role