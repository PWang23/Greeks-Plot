import pandas as pd
import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import norm

#delta plot
S = np.linspace(80,120,250)
T = np.linspace(1,200,250)
S,T=np.meshgrid(S,T)

#X=100 r=4% b=2% sigma=20%
X=100
r=0.04
b=0.02
sigma=0.2
t=T/365

d1 = (np.log(S/X)+(b+sigma**2/2)*t)/(sigma*t**0.5)
d2 = d1-sigma*t**0.5
GammaP =np.exp((b-r)*t)*norm.pdf(d1,loc=0,scale=1)/(sigma*100*t**0.5)
ColorP = GammaP*(r-b+b*d1/(sigma*t**0.5)+(1-d1*d2)/(2*t))

#3D plot
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(S,T,ColorP,cmap=plt.cm.coolwarm)
ax.set_xlabel('Asset Price')
ax.set_ylabel('Days to maturity')
ax.set_zlabel('ColorP')
fig.colorbar(surf,shrink=0.5,aspect=5)
plt.show()