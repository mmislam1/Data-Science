import numpy as np  
from math import sqrt  
import matplotlib.pyplot as plt  
import warnings  
from matplotlib import style  
from collections import Counter  
style.use('fivethirtyeight')  
  
get_ipython().run_line_magic('matplotlib', 'inline')  
#for show the graph  upper line  
  
dataset = {'k':[[50,110],[65,130],[70,140]],  
           'r':[[90,145,],[110,150],[100,140]]}  
  
print(dataset)  
  
def plot_scat(new_feat):  
    [ [plt.scatter(ii[0],ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]  
    plt.scatter(new_feat[0],new_feat[1],color='b')  
    plt.show()  
      
  
def k_nearest_neighbor(data,predict,k=3):  
      
    distances = []  
    for group in data:  
        for features in data[group]:  
            euclidian_distances =np.linalg.norm(np.array(features)-np.array(predict))  
            distances.append([euclidian_distances,group])  
              
          
    votes =[i [1] for i in sorted(distances)[:k]]  
    print( Counter(votes).most_common(1))  
    vote_result = Counter(votes).most_common(1)[0][0]  
    return vote_result  
  
while True:  
    print('Enter new pattern[Weight,Heihgt]:')  
    new_feat = [int(x) for x in input().split()]  
    if new_feat==[0,0]:  
        break  
    else:  
        plot_scat(new_feat)  
          
        result = k_nearest_neighbor(dataset,new_feat,k=3)  
        if result=='k':  
            print('Footballer')  
        else:  
            print('Wrestler')  
