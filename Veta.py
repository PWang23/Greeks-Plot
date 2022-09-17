import pandas as pd
import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import norm
import sys
np.set_printoptions(threshold=sys.maxsize)

#delta plot
S = np.linspace(50,150,100)
T = np.linspace(50,400,100)
S,T=np.meshgrid(S,T)

#X=100 r=4% b=2% sigma=20%
X=100
r=0.04
b=0.02
sigma=0.2
t=T/365

d1 = (np.log(S/X)+(b+sigma**2/2)*t)/(sigma*t**0.5)
d2 = d1-sigma*t**0.5
Vega =S*np.exp((b-r)*t)*norm.pdf(d1,loc=0,scale=1)*t**0.5
Veta = Vega*(r-b+b*d1/(sigma*t**2)-(1+d1*d2)/(2*t))

#3D plot
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(S,T,Veta,cmap=plt.cm.coolwarm)
ax.set_xlabel('Asset Price')
ax.set_ylabel('Days to maturity')
ax.set_zlabel('Veta')
fig.colorbar(surf,shrink=0.5,aspect=5)
plt.show()