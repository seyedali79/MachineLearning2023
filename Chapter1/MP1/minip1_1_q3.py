# -*- coding: utf-8 -*-
"""MiniP1_1_Q3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Md9B1uOY6-vjI5luHIvklttkqvP-2zyr

PART 3:

Q1:
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

#https://drive.google.com/file/d/1kYwlFgwVOVX-aGZO-rMltxuL_cjPrHQz/view?usp=sharing

!pip install --upgrade --no-cache-dir gdown
!gdown 1kYwlFgwVOVX-aGZO-rMltxuL_cjPrHQz

df = pd.read_csv('/content/heart_disease_health_indicators.csv')

"""Q2:"""

X = df.iloc[:,1:21].values
y = df[['HeartDiseaseorAttack']].values

X.shape, y.shape

# انتخاب نمونه‌های تصادفی از هر کلاس
samples_class_0 = df[df['HeartDiseaseorAttack'] == 0].sample(n=100, random_state=13)
samples_class_1 = df[df['HeartDiseaseorAttack'] == 1].sample(n=100, random_state=13)

# ادغام داده‌های انتخاب شده
df_sample = pd.concat([samples_class_0, samples_class_1])

# مخلوط کردن 200 داده ادغام شده
shuffled_df = df_sample.sample(frac=1, random_state=13).reset_index(drop=True)

samples_class_0.shape, samples_class_1.shape, df_sample.shape ,shuffled_df.shape

"""Q3:"""

from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import log_loss
from sklearn.metrics import log_loss

x_train, x_test, y_train, y_test = train_test_split(X, y,random_state=13, test_size = 0.2)

y_train_reshaped = np.ravel(y_train)
y_test_reshaped = np.ravel(y_test)

model1 = LogisticRegression(solver='sag', max_iter=300)
model1.fit(x_train, y_train_reshaped)
model1.predict(x_test)

print("Accuracy of test data: %", model1.score(x_test, y_test_reshaped)*100)
print("Accuracy of train data: %", model1.score(x_train, y_train_reshaped)*100)

model2 = SGDClassifier(loss='log_loss', random_state=13, max_iter=2000)
model2.fit(x_train, y_train_reshaped)
model2.predict(x_test)

print("Accuracy of test data: %", model2.score(x_test, y_test_reshaped)*100)
print("Accuracy of train data: %", model2.score(x_train, y_train_reshaped)*100)

"""Q4:"""

from sklearn.metrics import log_loss

model = SGDClassifier(loss='log', random_state=83)
losses = []
epochs = 300

for _ in range(epochs):

    model.partial_fit(x_train, y_train_reshaped, [0, 1])
    loss = log_loss(y_train , model.predict_proba(x_train))
    losses.append(loss)

plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss Curve')
plt.show()

"""Q5:"""

from sklearn.metrics import f1_score

model2 = SGDClassifier(loss='log_loss', random_state=13, max_iter=2000)
model2.fit(x_train, y_train_reshaped)
y_pred = model2.predict(x_test)

f1 = f1_score(y_test, y_pred)
print("F1-Score on test data: ", f1)