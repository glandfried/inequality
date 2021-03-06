import os
name = os.path.basename(__file__).split(".py")[0]
import matplotlib.pyplot as plt
##########
import sys
import numpy as np
import pandas as pd
sys.path.append('..')
import nonergodic as ne
from importlib import reload  # Python 3.4+ only.
reload(ne)

#from importlib import reload  # Python 3.4+ only.
#reload(ergodicity)

np.random.seed(99)
    
history = np.matrix(ne.multiplicative_perturbed_history(n=100,iterations=50*12,rate=1.0025,dt=1/12,sigma=1.2))
#plt.plot(np.log(history.T) )
history_pd = pd.DataFrame(history)

gdp = history_pd.apply(ne.gross_domestic_product_per_capita,0)
ddp = history_pd.apply(ne.democratic_domestic_product_per_capita,0)  

ginis = [ne.gini([ history[j,i] for j in range(len(history[:,i])) ])  for i in range(len(gdp))]

plt.plot(ginis)

plt.xticks(fontsize=12) # rotation=90
plt.yticks(fontsize=12) # rotation=90

plt.ylabel("Gini index", fontsize=16 )
plt.xlabel("Months", fontsize=16 )
plt.savefig(name+".pdf",pad_inches =0,transparent =True,frameon=True)
plt.savefig(name+".png",pad_inches =0,transparent =False,frameon=True,dpi=90)

bash_cmd = "pdfcrop --margins '0 0 0 0' {0}.pdf {0}.pdf".format(name)
os.system(bash_cmd)

