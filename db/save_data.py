from flask import Flask, request
import sqlite3
from feature import FeatureExtraction
import pandas as pd

def save_data(url,label):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM urls WHERE url=?", (url,))
    result = c.fetchone()
    if result is not None:
        # URL already exists, return message
        conn.close()
        return {"message": "URL already exists in the database"}
    
    obj = FeatureExtraction(url)
    features = obj.getFeaturesList()
    features.append(label)
    df = pd.read_sql_query("SELECT * FROM phishing", conn)
    index=df.shape[0]+1
    features.insert(0,index)
    c.execute("INSERT INTO phishing VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",features)
    conn.commit()
    # Insert URL into urls table
    c.execute("INSERT INTO urls (url) VALUES (?)", (url,))
    conn.commit()
    conn.close()
    return {"message": "Data added successfully"}
