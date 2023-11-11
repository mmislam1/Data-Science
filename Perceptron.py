# perceptron Practice  
import matplotlib.pyplot as plt  
import numpy as np  
  
inputs=np.array ([-1,-2,-3,-4])  
weight=np.array ([.3,.4,-1.5,6])  
  
cal=inputs*weight  
  
print(cal)  
  
sums=np.sum(cal)  
print('Summation:',sums)  
  
if sums>=1:  
    print ('yes')  
elif sums<=0:  
    print ('Decision: ','No') 
