import numpy as np  
import matplotlib.pyplot as plt  
from sklearn import svm  
  
player = np.array([(50,130),(55,140),(75,150),(85,160),(100,160)])  
target = np.array(['footballer','footballer','footballer','wrestler','wrestler'])  
  
clf = svm.SVC()  
clf.fit(player,target)  
  
clf.predict([(80,170)]) 
