'''
ML Crashcourse Tutorial
Based on https://www.youtube.com/watch?v=SW0YGA9d8y8

'tested.csv' is a csv file containing the status of the passengers of the Titanic

this is meant to be a heavily documented file I can point to later when I'm having trouble with scikit-learn
also to teach myself how to use skl
'''
import os
import pandas as pd
import numpy as np

# ML imports
from sklearn.model_selection import train_test_split # allows us to create a training set and a testing set

from sklearn.model_selection import GridSearchCV # allows us to test multiple scenarios to find the best performance

from sklearn.preprocessing import MinMaxScaler # cleans data for the model, converts data to a number between 0-1

from sklearn.neighbors import KNeighborsClassifier # the model we're using

from sklearn.metrics import accuracy_score, confusion_matrix # 

# Visualization imports
import matplotlib.pyplot as plt
import seaborn as sns


# Handling Data

data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'titanic.csv'))


def normalize_columns(df):
    work = df.copy()

    rename_map = {}
    for col in work.columns:
        col_lower = col.strip().lower()

        if col_lower == "passengerid":
            rename_map[col] = "PassengerId"
        elif col_lower == "sibsp":
            rename_map[col] = "SibSp"
        elif col_lower in {"survived", "2urvived"}:
            rename_map[col] = "Survived"
        elif col_lower == "parch":
            rename_map[col] = "Parch"
        elif col_lower == "pclass":
            rename_map[col] = "Pclass"
        elif col_lower == "sex":
            rename_map[col] = "Sex"
        elif col_lower == "age":
            rename_map[col] = "Age"
        elif col_lower == "fare":
            rename_map[col] = "Fare"
        elif col_lower == "embarked":
            rename_map[col] = "Embarked"

    work = work.rename(columns=rename_map)

    # Drop known filler columns from this dataset variant.
    zero_cols = [c for c in work.columns if c.strip().lower().startswith("zero")]
    work = work.drop(columns=zero_cols, errors="ignore")

    # Keep only features this script can process.
    allowed_cols = {"PassengerId", "Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"}
    drop_extra = [c for c in work.columns if c not in allowed_cols]
    work = work.drop(columns=drop_extra, errors="ignore")

    if "Survived" not in work.columns:
        raise ValueError("Target column not found. Expected 'Survived' or '2urvived' in titanic.csv.")

    return work


# Guardrail: identify suspiciously deterministic labels.
def check_dataset_for_target_shortcuts(df):
    if {"Sex", "Survived"}.issubset(df.columns):
        if df["Sex"].dtype == object:
            sex_numeric = df["Sex"].map({"male": 1, "female": 0})
        else:
            sex_numeric = df["Sex"]
        sex_numeric = pd.to_numeric(sex_numeric, errors="coerce")
        survived_numeric = pd.to_numeric(df["Survived"], errors="coerce")
        valid = sex_numeric.notnull() & survived_numeric.notnull()
        if valid.any():
            sex_rule_acc = max(
                (sex_numeric[valid] == survived_numeric[valid]).mean(),
                (sex_numeric[valid] != survived_numeric[valid]).mean(),
            )
            if sex_rule_acc == 1.0:
                print("WARNING: Survived is perfectly determined by Sex in this dataset (100% match).")
                print("This can produce a perfect confusion matrix even without leakage.")


# Fit preprocessing values only on training data.
def fit_preprocessor(train_df):
    work = train_df.copy()

    pclass_age_medians = work.groupby("Pclass")["Age"].median().to_dict()
    global_age_median = work["Age"].median()
    fare_median = work["Fare"].median() if "Fare" in work.columns else None

    fare_bins = None
    if "Fare" in work.columns:
        fare_q = work["Fare"].fillna(fare_median).quantile([0.25, 0.50, 0.75]).tolist()
        # Use training-only quantiles so test data does not influence bin edges.
        fare_bins = [-np.inf] + fare_q + [np.inf]

    return {
        "pclass_age_medians": pclass_age_medians,
        "global_age_median": global_age_median,
        "fare_median": fare_median,
        "fare_bins": fare_bins,
    }


# Apply preprocessing with values learned from training data.
def transform_data(df, prep):
    work = df.copy()
    work.drop(columns=["PassengerId", "Name", "Ticket", "Cabin", "Embarked"], inplace=True, errors="ignore")

    age_map = prep["pclass_age_medians"]
    global_age = prep["global_age_median"]
    work["Age"] = work.apply(
        lambda row: age_map.get(row["Pclass"], global_age) if pd.isnull(row["Age"]) else row["Age"],
        axis=1,
    )
    work["Age"] = work["Age"].fillna(global_age)

    if work["Sex"].dtype == object:
        work["Sex"] = work["Sex"].map({"male": 1, "female": 0})
    work["Sex"] = pd.to_numeric(work["Sex"], errors="coerce").fillna(-1).astype(int)

    work["FamilySize"] = work["SibSp"] + work["Parch"]
    work["IsAlone"] = np.where(work["FamilySize"] == 0, 1, 0)

    if "Fare" in work.columns:
        work["Fare"] = work["Fare"].fillna(prep["fare_median"])
        work["FareBin"] = pd.cut(work["Fare"], bins=prep["fare_bins"], labels=False, include_lowest=True)
        work["FareBin"] = work["FareBin"].fillna(0).astype(int)

    work["AgeBin"] = pd.cut(
        work["Age"], bins=[0, 12, 20, 40, 60, np.inf], labels=False, include_lowest=True
    )
    work["AgeBin"] = work["AgeBin"].fillna(0).astype(int)

    return work


data = normalize_columns(data)
check_dataset_for_target_shortcuts(data)

# create features / target variables
X_raw = data.drop(columns=["Survived"])
y = data["Survived"]

X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    X_raw, y, test_size=0.25, random_state=42, stratify=y
)

prep = fit_preprocessor(X_train_raw)
X_train = transform_data(X_train_raw, prep)
X_test = transform_data(X_test_raw, prep)

X_train.info()
print(X_train.isnull().sum())


# ML Preprocessing, turning everything into numbers for the model

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# Hyperparameter Tuning - KNN Model

def tune_model(X_train, y_train):
    param_grid = {
        'n_neighbors': range(1,21),
        'metric': ['euclidean', 'manhattan', 'minkowski'],
        'weights': ['uniform', 'distance']
    }

    model = KNeighborsClassifier()
    grid_search = GridSearchCV(model, param_grid, cv=5, n_jobs=-1)
    grid_search.fit(X_train, y_train) # finds best model
    return grid_search.best_estimator_

best_model = tune_model(X_train, y_train) # boom model


# Predictions and evaluate

def evaluate_model(model, X_test, y_test):
    prediction = model.predict(X_test)
    accuracy = accuracy_score(y_test, prediction)
    matrix = confusion_matrix(y_test, prediction)
    return accuracy, matrix

accuracy, matrix = evaluate_model(best_model, X_test, y_test)

print(f'Accuracy: {accuracy * 100:.2f}%')
print(f'Confusion Matrix:')
print(matrix)


# Plotting

def plot_model(matrix):
    plt.figure(figsize=(10,7))
    sns.heatmap(matrix, annot=True, fmt='d', xticklabels=['Not survived', 'Survived'], 
                yticklabels=['Not survived', 'Survived'])
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted Value')
    plt.ylabel('True Values')
    plt.show()

print(X_train.shape)

plot_model(matrix)
