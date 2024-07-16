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

## Do some predictions
y_pred = model.predict(X_test)
y_pred_classes = y_pred.argmax(axis=1)
y_true = y_test.argmax(axis=1)

## Calculate final metrics
accuracy_nn = accuracy_score(y_true, y_pred_classes)
precision_nn = precision_score(y_true, y_pred_classes)
recall_nn = recall_score(y_true, y_pred_classes)
f1_nn = f1_score(y_true, y_pred_classes)

## show the thingies
print("Neural Network Model Evaluation:")
print(f"Accuracy: {accuracy_nn}")
print(f"Precision: {precision_nn}")
print(f"Recall: {recall_nn}")
print(f"F1-Score: {f1_nn}")

## Results can vary but generally this will lead to:

## Accuracy: 94%
## Precision: ~97%
## Recall: ~89%
## F1-Score: ~93%

## typically with a deviation of +/- .5% in some runs

## Notes:

## The model performed way above my expectations, compared to the naive-bayes model. That only had about 70% accuracy.

## A 94% accuracy is quite good in comparison, especially for a simple model like this one. That basically means that 94 out of 100 emails are classified correctly.
## 97% precision means that 97% of the emails classified as spam are actually spam, an impressive minimization of false positives.
## 89% recall means that 89% of the spam emails are correctly classified as spam, a good minimization of false negatives too.

## In my opinion, more emphasis should be put on minimizing false positives, as it is more annoying to have a non-spam email classified as spam than the other way around. 
## Which this model does quite well with a 97% precision.

## Overall this leads to a great F1-Score of 93%, which is a good balance between precision and recall.

## We can save the model for later use (but it doesn't really matter since we're not going to do anything with it)
time_stamp = pd.Timestamp.now().strftime('%Y-%m-%d_%H-%M-%S')

if(not os.path.exists('models')):
    os.mkdir('models')

model.save(f'models/neural_network_{time_stamp}.keras')