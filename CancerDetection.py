import numpy as np  
import matplotlib.pyplot as plt  
from sklearn import svm  
from sklearn import datasets  
  
cancer = datasets.load_breast_cancer()  
  
  
from sklearn.model_selection import train_test_split  
  
X_train,X_test,y_train,y_test = train_test_split(cancer.data,cancer.target,test_size=.7,random_state=42)  
  
clf = svm.SVC(kernel='linear')  
  
clf.fit(X_train,y_train)  
  
y_predict = clf.predict(X_test)  
  
#print (y_predict)  
  
from sklearn import metrics  
  
print('Accuracy:',metrics.accuracy_score(y_test,y_predict)*100)  
print('Precision:',metrics.precision_score(y_test,y_predict)*100)  
print('Recall:',metrics.recall_score(y_test,y_predict)*100) 
