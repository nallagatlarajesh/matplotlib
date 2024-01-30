#user s can also specify the size of the figure using  figure() methode
#additionally users can pass values as tuples ,which make up the length of rows and columns to the argument fig
from matplotlib import pyplot as plt 
plt.plot ([1,2,3],[4,5,2])
plt.figure(figsize=(100,120))
plt.show()
