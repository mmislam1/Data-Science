import numpy as np  
import matplotlib.pyplot as plt  
  
  
def sigmoid_function(x):  
    x1 = -x  
    x2 = np.exp(x1)  
    x3 = 1+x2  
    x4 = 1/x3  
      
    return x4  
  
x = np.array([(1,1,1,1,1,1),(1,2,5,101,1023,1),(1,3,7,10007,1000007,1),(1,19,11,31,97,1),(1,13,17,61,29,1),(1,1,1,1,1,1)])  
  
sigmoid_output = x  
  
for i in range (0,9):  
    sigmoid_output = sigmoid_function(sigmoid_output)  
print(sigmoid_output)  
  
plt.plot(x,sigmoid_output)  
plt.show() 
