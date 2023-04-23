# Phishing URL Detector Plugin API 
![image]()
![image]()

## Table of Content
  * [Introduction](#introduction)
  * [Installation](#installation)
  * [Directory Tree](#directory-tree)
  * [Result](#result)
  * [Conclusion](#conclusion)


## Introduction

# Phishing URL Detection

## Overview
This project is about detecting phishing URLs using machine learning algorithms. The project consists of three main parts: data loading and cleaning, feature extraction, and model training and evaluation. The project uses the Gradient Boosting Classifier to classify phishing URLs with an accuracy of over 96%.

## Installation

To run the project, you can follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/Phishing-URL-Detection.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Run the Flask application: `python app.py`

 To see project click [here]("/").


## Directory Tree 
```
├── db
│   ├── load_data.py
│   ├── save_data.py
│   ├── train_model.py
├── pickle
│   ├── model.pkl
├── joblib
│   ├── gbc_model.joblib
├── Phishing URL Detection.ipynb
├── README.md
├── app.py
├── database.db
├── feature.py
├── phishing.csv
├── requirements.txt
```


## Files
- `app.py`: Flask web application for testing the model
- `feature.py`: script for extracting features from URLs
- `database.db`: SQLite database for storing URLs and their labels
- `phishing.csv`: dataset containing URLs and their labels
- `pickle/model.pkl`: serialized model object
- `joblib/gbc_model.joblib`: serialized model object using joblib
- `db/load_data.py`: script for loading data into the database
- `db/save_data.py`: script for saving data to the database
- `db/train_model.py`: script for training and evaluating the model
- `Phishing URL Detection.ipynb`: Jupyter notebook containing the project code and documentation
- `README.md`: readme file explaining the project

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" width=200>](https://numpy.org/doc/) [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width=200>](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" width=100>](https://matplotlib.org/)
[<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 
[<img target="_blank" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScq-xocLctL07Jy0tpR_p9w0Q42_rK1aAkNfW6sm3ucjFKWML39aaJPgdhadyCnEiK7vw&usqp=CAU" width=200>](https://flask.palletsprojects.com/en/2.0.x/) 


# Model Comparison

| ML Model                        | Accuracy | F1 Score | Recall | Precision |
|--------------------------------|----------|----------|--------|-----------|
| Gradient Boosting Classifier   | 0.974    | 0.977    | 0.994  | 0.986     |
| Multi-layer Perceptron         | 0.971    | 0.974    | 0.990  | 0.991     |
| XGBoost Classifier             | 0.969    | 0.973    | 0.993  | 0.984     |
| Random Forest                  | 0.966    | 0.970    | 0.994  | 0.984     |
| Support Vector Machine         | 0.964    | 0.968    | 0.980  | 0.965     |
| Decision Tree                  | 0.958    | 0.962    | 0.991  | 0.993     |
| K-Nearest Neighbors            | 0.956    | 0.961    | 0.991  | 0.989     |
| Logistic Regression            | 0.934    | 0.941    | 0.943  | 0.927     |
| Naive Bayes Classifier         | 0.914    | 0.922    | 0.907  | 0.922     |

The table above shows the performance metrics of various machine learning models trained on the phishing URL dataset. The accuracy, F1 score, recall, and precision are reported for each model. The results show that the Gradient Boosting Classifier has the highest accuracy, F1 score, recall, and precision among all models, with an accuracy of 0.974, F1 score of 0.977, recall of 0.994, and precision of 0.986.```

Feature importance for Phishing URL Detection
<br><br>
<div style="background-color:white">

![image](https://user-images.githubusercontent.com/79131292/144603941-19044aae-7d7b-4e9a-88a8-6adfd8626f77.png)

</div>




## Conclusion

The present research work aimed to explore various machine learning models and perform exploratory data analysis on a phishing dataset to understand the features that affect the models' ability to detect whether a URL is safe or not. 

The research project involved the creation of a notebook, which provided a significant learning experience in the domain of phishing detection. The project's findings revealed that certain features, such as "HTTPS," "AnchorURL,""LinkInScriptTags,""PrefixSuffix," and "WebsiteTraffic," were crucial in classifying URLs as phishing URLs or not.

After testing various machine learning models, the Gradient Boosting Classifier emerged as the best-performing model, with an accuracy of 97.4%. This performance indicates a promising reduction in the likelihood of malicious attachments. 

Overall, this project showcases the significance of machine learning models in detecting phishing URLs and the importance of feature selection in the model's performance. Future research can extend this project to evaluate more advanced features and models, leading to even more accurate results. 


## Contributing

If you would like to contribute to the project, you can create a pull request with your changes. Please make sure to follow the project's coding conventions and include tests for any new functionality.