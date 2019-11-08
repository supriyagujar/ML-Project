# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:11:31 2019

@author: supriya
"""

import nltk 
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re
import seaborn as sns
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve,auc
from sklearn.model_selection import cross_val_score
messages=pd.read_csv("D:/sms-spam-collection-dataset/spam.csv",encoding='latin-1')
nltk.download('stopwords')
corpus=[]
Ps=PorterStemmer()
wordNet=WordNetLemmatizer()
for i in range(len(messages)):
    review=re.sub('[^a-zA-Z]',' ',messages['message'][i])
    review=review.lower()
    review=review.split()
    review=[wordNet.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review=' '.join(review)
    corpus.append(review)
from matplotlib import pyplot as plt
cv=CountVectorizer(max_features=1500)
x=cv.fit_transform(corpus).toarray()
y=pd.get_dummies(messages['class'])
y=y.iloc[:,1].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=42)
    
clf=MultinomialNB()
clf.fit(x_train,y_train)
clf.score(x_test,y_test)

pred=clf.predict(x_test)
bow_features=cv.get_feature_names()
feat_cnt=clf.feature_count_
print(feat_cnt.shape)

train_fpr, train_tpr, thresholds = roc_curve(y_train, clf.predict_proba(x_train)[:,1])
test_fpr, test_tpr, thresholds = roc_curve(y_test, clf.predict_proba(x_test)[:,1])

plt.plot(train_fpr, train_tpr, label="train AUC ="+str(auc(train_fpr, train_tpr)))
plt.plot(test_fpr, test_tpr, label="train AUC ="+str(auc(test_fpr, test_tpr)))
plt.legend()
plt.xlabel("alpha: hyperparameter")
plt.ylabel("AUC")
plt.title("ERROR PLOTS")
plt.show()

print("="*100)

conf=confusion_matrix(y_test,pred)
sns.heatmap(conf,annot=True,fmt="d")
plt.xlabel("predicted label")
plt.ylabel("true label")
plt.title('confusion matrix')
plt.show()
print("AUC of bag of word",round(auc(test_fpr, test_tpr),2))