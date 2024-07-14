## built-in libraries
import os

## This makes numerical results *more* consistent throughout runs by unf*cking the computation order at the slight cost of performance
## Before this observation we noticed deviations of up to +/- 3% in some runs regarding accuracy specifically
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

## third-party libraries
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from keras.src.models import Sequential
from keras.src.layers import Dense
from keras.src.utils import to_categorical

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

## Make the labels categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

## Create the thingy (model) (using sequential linear stacks)
model = Sequential()

model.add(Dense(64, input_dim=X_train.shape[1], activation='relu')) ## input layer (receives attributes as features)
model.add(Dense(32, activation='relu')) ## hidden layer (More ReLu nonsense)
model.add(Dense(2, activation='softmax'))  ## softmax binary classification output layer

## Overall compile using Adam with Categorical Cross Entropy method
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

## Okay now we can train the model
## epochs are database iterations (50 was default)
## batch_size (sample per gradient)
history = model.fit(X_train, y_train, epochs=25, batch_size=10, validation_data=(X_test, y_test))

## Base evaluate, with accuracy score
scores = model.evaluate(X_test, y_test)

print(f"Accuracy: {scores[1]}")

## notes that while testing
## 1 epoch gave 94.4& accuracy
## 15 epochs gave 94.3% accuracy
## 25 epochs gave 95.9% accuracy
## 50 epochs gave 95.4% accuracy 
## 75 epochs gave 94.5% accuracy
## 100 epochs gave 94.4% accuracy

## it appears that more/less database iteration leads to overfitting or underfitting. Sweet spot appears to be 25-50 epochs
## Despite fixing the scheduler, deviations of <- -/+ 1 can be observed but 25-50 maintains a 95% on average through many runs