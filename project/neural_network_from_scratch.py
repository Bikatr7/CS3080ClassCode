## Kaden Bilyeu
## Alexis Liew
## Oleander Coyne
## CS 3080-001
## Final Project
## 2024-07-17
## neural_network_from_scratch.py

## Basically without keras or tensorflow

## third-party libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

##---------------------------------------------helper functions---------------------------------------------##

## Sigmoid is a function that maps any input to a value between 0 and 1
def sigmoid(x:np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))

## The derivative of the sigmoid function is used to calculate the gradient
def sigmoid_derivative(x:np.ndarray) -> np.ndarray:
    return x * (1 - x)

##---------------------------------------------main code---------------------------------------------##

## Load the data from "csv" files
data_path = r'data/spambase.data'
names_path = r'data/spambase.names'

## read the data, contains column names and some documentation
with open(names_path, 'r') as f:
    names = f.read().splitlines()

## Extract the actual column names (excluding comments and empty lines)
column_names = [line.split(':')[0] for line in names if line and not line.startswith('|')]

## Load the data into a DataFrame
data = pd.read_csv(data_path, header=None, names=column_names)

## Define features and labels
## x is about 57 features that measure attributes of the email
## y is the label, 1 if spam, 0 if not spam
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

## Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

## Standardize the data kinda?
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

## Convert labels to one-hot encoding (categorical data)
y_train = np.eye(2)[y_train]
y_test = np.eye(2)[y_test]

## Neural network parameters
input_size = X_train.shape[1]
hidden_size = 128
output_size = 2
learning_rate = 0.001 
epochs = 50
