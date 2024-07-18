## Kaden Bilyeu
## Alexis Liew
## Oleander Coyne
## CS 3080-001
## Final Project
## 2024-07-17
## neural_network_from_scratch.py

## Basically without keras or tensorflow, numpy, pandas, and scikit-learn are used for data structures, data manipulation, and evaluation metrics. But the neural network is built from scratch.

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
epochs = 25

## Randomly initialize the weights
np.random.seed(42)
weights_input_hidden = np.random.rand(input_size, hidden_size) - 0.5
weights_hidden_output = np.random.rand(hidden_size, output_size) - 0.5

## Training the neural network by hand
for epoch in range(epochs):
    ## Forward pass (input -> output)
    hidden_input = np.dot(X_train, weights_input_hidden)
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, weights_hidden_output)
    final_output = sigmoid(final_input)

    ## Calculate error (difference between predicted and actual)
    error = y_train - final_output
    if(epoch + 1) % 5 == 0:
        print(f'Epoch {epoch + 1}/{epochs}, Error: {np.mean(np.abs(error))}')

    ## Perform Backpropagation (output -> input) basically a backwards pass
    delta_output = error * sigmoid_derivative(final_output)
    error_hidden_layer = delta_output.dot(weights_hidden_output.T)
    delta_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_output)

    ## Update the weights using gradient descent
    weights_hidden_output += hidden_output.T.dot(delta_output) * learning_rate
    weights_input_hidden += X_train.T.dot(delta_hidden_layer) * learning_rate

## We have trained the model, now we can evaluate it 
hidden_input = np.dot(X_test, weights_input_hidden) # type: ignore
hidden_output = sigmoid(hidden_input)

final_input = np.dot(hidden_output, weights_hidden_output)
final_output = sigmoid(final_input)

## Predict the class labels
y_pred = np.argmax(final_output, axis=1)
y_true = np.argmax(y_test, axis=1)

## Calculate the evaluation metrics
accuracy_nn = accuracy_score(y_true, y_pred)
precision_nn = precision_score(y_true, y_pred)
recall_nn = recall_score(y_true, y_pred)
f1_nn = f1_score(y_true, y_pred)

## Show the evaluation metrics
print("Neural Network Model Evaluation:")
print(f"Accuracy: {accuracy_nn}")
print(f"Precision: {precision_nn}")
print(f"Recall: {recall_nn}")
print(f"F1-Score: {f1_nn}")

## notes that while testing
## 1 epoch gave 69.1% accuracy
## 15 epochs gave 88.0% accuracy
## 25 epochs gave 90.7% accuracy
## 50 epochs gave 92.8% accuracy
## 75 epochs gave 93.2% accuracy
## 100 epochs gave 93.5% accuracy
## 150 epochs gave 93.8% accuracy

## it appears that less database iteration leads to underfitting. Sweet spot appears to be 25-50 epochs once again
## Deviations of <- -/+ 2% can be observed likely due ot the nature of the neural network being built from scratch

## Unlike the keras model, the neural network from scratch is less accurate but still performs well. Something of note is that overfitting doesn't appear to happen. As epochs increase, the accuracy and F1-Score increase as well.
## However if I had to guess this probably still a symptom of overfitting, and would perform poorly on new data.
## 25 epochs should work well for this model.

## Results can vary for 25 epochs but generally this will lead to:

## Accuracy: 90%
## Precision: ~92%
## Recall: ~85%
## F1-Score: ~88%

## typically with a deviation of +/- 1% in some runs

## Notes:

## The from scratch neural network is quite a bit less accurate than the keras model, but still performs well.

## An accuracy of 90% is still quite good, but the keras model is more accurate. The same applies to the precision, recall, and F1-Score.

## The same conclusions can be drawn from the from scratch model as the keras model. The sweet spot for epochs is 25-50, and the model is likely overfitting as epochs increase.