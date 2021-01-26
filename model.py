#BLAPS.v2
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings("ignore")

#read dataset
train=pd.read_csv('train.csv')
test=pd.read_csv('test.csv')
print(train.head())

#drop unwanted columns
train.drop('Loan_ID',axis=1,inplace=True)
train.drop('Loan_Amount_Term',axis=1,inplace=True)
train.drop('Property_Area',axis=1,inplace=True)

test.drop('Loan_ID', axis=1, inplace=True)
test.drop('Loan_Amount_Term',axis=1,inplace=True)
test.drop('Property_Area',axis=1,inplace=True)

print(train.head())
print(test.head())

print(train.isnull().sum())

#DATA PREPARATION
#impute missing values 
train['Gender'].fillna(train['Gender'].mode()[0],inplace=True)
train['Married'].fillna(train['Married'].mode()[0],inplace=True)
train['Dependents'].fillna(train['Dependents'].mode()[0],inplace=True)
train['Self_Employed'].fillna(train['Self_Employed'].mode()[0],inplace=True)
train['LoanAmount'].fillna(train['LoanAmount'].mode()[0],inplace=True)
train['Credit_History'].fillna(train['Credit_History'].mode()[0],inplace=True)
print(train.isnull().sum())

print(train.dtypes)

# Convert all non-numeric values to number
cat=['Gender','Married','Dependents','Education','Self_Employed','Credit_History', 'Loan_Status']

for var in cat:
    le = preprocessing.LabelEncoder()
    train[var]=le.fit_transform(train[var].astype('str'))

print(train.dtypes)

#MODEL BUILDING

from sklearn.model_selection import train_test_split
X  = train.drop('Loan_Status', axis = 1)
y = train['Loan_Status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# fit the model
model = LogisticRegression()
model.fit(X_train, y_train)
# make prediction
y_pred = model.predict(X_test)
print("Accuracy: {0}".format(metrics.accuracy_score(y_test, y_pred)))
print("Recall/Sensitivity: {0}".format(metrics.recall_score(y_test, y_pred)))


import pickle
filename = "blaps.v2.pkl"

with open(filename, 'wb') as file:  
    pickle.dump(model, file)