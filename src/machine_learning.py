import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Conv1D, MaxPooling1D, Flatten
from tensorflow.keras.utils import to_categorical

# Directory Path containing subject-wise CSVs
DATA_DIR = "d:/emg_micro/data/processed/"

# Load all CSV files
all_data = []
for file in os.listdir(DATA_DIR):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(DATA_DIR, file))
        all_data.append(df)

df = pd.concat(all_data, ignore_index=True)

# Features and labels
features = [f's{i}' for i in range(1, 9)]
X = df[features].values
y = LabelEncoder().fit_transform(df['emotion_label'])
y_cat = to_categorical(y)

# Normalize
X_scaled = StandardScaler().fit_transform(X)
X_reshaped = X_scaled.reshape(X_scaled.shape[0], X_scaled.shape[1], 1)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
X_train_seq, X_test_seq, y_train_cat, y_test_cat = train_test_split(X_reshaped, y_cat, test_size=0.2, random_state=42)

# Model Builders
def create_cnn():
    model = Sequential([
        Conv1D(64, 2, activation='relu', input_shape=(8, 1)),
        MaxPooling1D(2),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(y_cat.shape[1], activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def create_lstm():
    model = Sequential([
        LSTM(64, input_shape=(8, 1)),
        Dense(64, activation='relu'),
        Dense(y_cat.shape[1], activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Sklearn Evaluation
def evaluate_sklearn_model(model, name):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"\n{name} Results:")
    print("Precision:", precision_score(y_test, y_pred, average='weighted'))
    print("Recall:", recall_score(y_test, y_pred, average='weighted'))
    print("F1-score:", f1_score(y_test, y_pred, average='weighted'))
    print("Accuracy: {:.2f}%".format(accuracy_score(y_test, y_pred) * 100))

# Keras Evaluation
def evaluate_keras_model(model_fn, name):
    model = model_fn()
    model.fit(X_train_seq, y_train_cat, epochs=10, batch_size=32, verbose=0)
    y_pred = model.predict(X_test_seq)
    y_pred_classes = np.argmax(y_pred, axis=1)
    y_true = np.argmax(y_test_cat, axis=1)
    print(f"\n{name} Results:")
    print("Precision:", precision_score(y_true, y_pred_classes, average='weighted'))
    print("Recall:", recall_score(y_true, y_pred_classes, average='weighted'))
    print("F1-score:", f1_score(y_true, y_pred_classes, average='weighted'))
    print("Accuracy: {:.2f}%".format(accuracy_score(y_true, y_pred_classes) * 100))

# Evaluate models
evaluate_sklearn_model(SVC(), "SVM")
evaluate_sklearn_model(DecisionTreeClassifier(), "Decision Tree")
evaluate_sklearn_model(RandomForestClassifier(), "Random Forest")
evaluate_sklearn_model(KNeighborsClassifier(), "KNN")
evaluate_keras_model(create_cnn, "CNN")
evaluate_keras_model(create_lstm, "LSTM")
