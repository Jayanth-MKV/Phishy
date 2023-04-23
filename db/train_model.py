import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
import sqlite3
import pickle

db_path = 'database.db'
model_path = './pickle/model.pkl'
csv_path = 'phishing.csv'

def train_model():
    # Load the data from the database
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM phishing", conn)
    conn.close()

    # Save the DataFrame to a CSV file
    df.to_csv(csv_path, index=False)

    # Split the data into features (X) and labels (y)
    X = df.drop(columns=['class','Index']).values
    y = df['class'].values

    # Train the model on the data
    model = GradientBoostingClassifier(max_depth=4,learning_rate=0.7)
    model.fit(X, y)

    # Save the trained model to disk
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

train_model()