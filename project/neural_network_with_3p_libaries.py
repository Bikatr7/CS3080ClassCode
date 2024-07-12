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

##Load the data into a DataFrame
data = pd.read_csv(data_path, header=None, names=column_names)

## Define features and labels
## x is about 57 features that measure attributes of the email
## y is the label, 1 if spam, 0 if not spam
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values   