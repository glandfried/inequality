import os
name = os.path.basename(__file__).split(".py")[0]
import matplotlib.pyplot as plt
##########
import sys
import numpy as np
import pandas as pd
import  statistics
sys.path.append('..')
import nonergodic as ne
from importlib import reload  # Python 3.4+ only.
reload(ne)

#from importlib import reload  # Python 3.4+ only.
#reload(ergodicity)

if __name__ == "__main__":
    np.random.seed(99)
        
    history = np.matrix(ne.multiplicative_perturbed_history(n=100,iterations=50*12,rate=1.0025,dt=1/12,sigma=1.2))
    #plt.plot(np.log(history.T) )
    history_pd = pd.DataFrame(history)

    gdp = history_pd.apply(ne.gross_domestic_product_per_capita,0)
    ddp = history_pd.apply(ne.democratic_domestic_product_per_capita,0)  
    
    median_dp= history_pd.apply(statistics.median,0)  
    plt.plot(np.log(gdp),label="GDP per capita")
    plt.plot(np.log(ddp),label="DDP per capita")
    plt.plot(np.log(median_dp), label="Median")
    plt.legend(loc="upper left")
    
    plt.xticks(fontsize=12) # rotation=90
    plt.yticks(fontsize=12) # rotation=90

    plt.ylabel("Wealth", fontsize=16 )
    plt.xlabel("Months", fontsize=16 )
    plt.savefig(name+".pdf",pad_inches =0,transparent =True,frameon=True)
    plt.savefig(name+".png",pad_inches =0,transparent =True,frameon=True,dpi=90)
    
    
    
    bash_cmd = "pdfcrop --margins '0 0 0 0' {0}.pdf {0}.pdf".format(name)
    os.system(bash_cmd)
    
