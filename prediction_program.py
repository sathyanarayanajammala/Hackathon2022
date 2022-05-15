# -*- coding: utf-8 -*-
"""
Created on Tue May  3 11:37:50 2022

@author: jamal
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn import metrics

input_data = pd.read_excel('C:\Hackathon\Personal_load_prediction-master\Personal_load_prediction-master\Target_Customer_Prediction.xlsx')

input_data.head()
input_data.shape

x = input_data.drop(['Offer_acceptance'], axis=1)
y = input_data['Offer_acceptance']

x.head()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3 )

from sklearn import tree 
ctree = tree.DecisionTreeClassifier()
ctree.fit(x_train, y_train)
y_pred = ctree.predict(x_test)

from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred))



from sklearn import tree 
ctree = tree.DecisionTreeClassifier()
ctree.fit(x_train, y_train)
y_pred = ctree.predict(x_test)

from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred))

comp_df = pd.DataFrame()
comp_df['Class_actual'] = y_test
comp_df['Class_predicted'] = y_pred
comp_df.head(5)

y_test.value_counts(normalize=True)

ctree.feature_importances_

temp_imp = pd.DataFrame()
temp_imp['col'] = x.columns
temp_imp['imp'] = ctree.feature_importances_*100

temp_imp

temp_imp.sort_values('imp', ascending=False)