import numpy as np
import matplotlib.pyplot as plt


s = 0.1 # sigma square
               

rho = np.arange(-1, 1, 0.005)
n = len(rho)
var11 = np.zeros( n )
var12 = np.zeros( n )

for j in range(0,n):    
    r = rho[j]
    var12[j] = 2*s*(s+ 1  - r*r)/( s*s +2*s + 1 - r*r)
    var11[j] = 2 - 2*(1+r*r)/(s + 2)


curve12  = plt.plot(rho, var12, label = "measure at different points")
curve11  = plt.plot(rho, var11, label = "measure at same point twice")

plt.setp( curve11, 'linewidth', 3.0, 'color', 'r', 'alpha', .5 )
plt.setp( curve12, 'linewidth', 3.0, 'color', 'b', 'alpha', .5 )
plt.title("Total Posterior  Variance.  $\sigma^2 = $" +str(s))
plt.legend(loc=1 , prop={'size':7})    
plt.xlabel("rho", fontsize=9)
plt.ylabel('Posterior Variance', fontsize=9)
plt.show()
