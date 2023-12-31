def factorial(n):  
    if n==1:  
        return 1  
    else:  
        return n*factorial(n-1)  
      
      
while True:  
    n = input('Enter a number to calculate factorial:')  
    n = int(n)  
    if n==0:  
        break  
          
    fact = factorial(n)  
    print('factorial of ',n, 'is :',fact)  
      
    print(len(str(fact)))  
  
  
#Numpy in Machin Learning and Artificial Intelligence  
#Numpy-> Multi-dimentional matrix in anaconda  
#Numpy is a library  
  
import numpy as np  
a = np.array( [ (1,3,5),(2,4,6),(8,6,7),(9,7,2) ] )  
print(a)  
dim = a.shape  
print(dim)  
row,col = a.shape  
print('Row:',row, 'Col:',col)  
  
b = np.array( [ (5,7,9),(9,8,6),(4,5,2) ] )  
print(b)  
  
#Matrix multiplication is called dot(.) product  
  
dot_product = np.dot(a,b)  
print('dot product of a,b:\n',dot_product)  
print('Dimensional of dot product:', dot_product.shape)  
  
#zero and ones in numpy  
  
zero_arr = np.zeros((4,3))  
print(zero_arr)  
dim = zero_arr.shape  
row = dim[0]  
col = dim[1]  
for i in range(0,col,1):  
    for j in range(0,col,1):  
        zero_arr[i][j]=i*j+1  
      
print(zero_arr)  
