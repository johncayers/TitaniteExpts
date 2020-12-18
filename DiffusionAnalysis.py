# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:17:02 2020

@author: ayersj
"""
import pandas as pd
import numpy as np
from scipy.special import erfc
from scipy.optimize import curve_fit
# import matplotlib.pyplot as plt
# import os
# os.chdir = ('C:/Users/ayersj/OneDrive - Vanderbilt/Papers/SpheneSolubility/DataAnalysis/TitaniteExpts')
diff_prof=pd.read_csv('C:/Users/ayersj/OneDrive - Vanderbilt/Papers/SpheneSolubility/DataAnalysis/TitaniteExpts/DiffusionProfilesV3.csv')
linear_portion=pd.read_csv('C:/Users/ayersj/OneDrive - Vanderbilt/Papers/SpheneSolubility/DataAnalysis/TitaniteExpts/XrangeDiffusionProfiles.csv')
# The equation that need to be optimized is c=c0*erfc(m*x)
# Where c and x are found from the data. c0 and m needs to be optimized.
def diff_value(x,m,c0):
    return c0*erfc(m*x)
list_exp=[3,7,10,11,13,15,17,18,21]
list_oxides=["SiO2","Al2O3","Na2O","K2O","CaO","TiO2"]
df = pd.DataFrame( columns = ['Expt', 'Oxide',"Slope",'c0']) # Define the output dataframe

#Loops
for i in range(0,len(list_exp)):
    print("SpDis"+str(list_exp[i]))
    # Get max and min value of x to subset the linear for the experiment
    min_value=linear_portion[linear_portion["Expt."]==list_exp[i]]["Min x"].values
    max_value=linear_portion[linear_portion["Expt."]==list_exp[i]]["Max x"].values
    # Subset Experiment and linear portion for those epxeriments
    test_tio2=diff_prof[(diff_prof['Expt']=="SpDis"+str(list_exp[i])) & (diff_prof['x']<=float(max_value)) & (diff_prof['x']>=float(min_value))]
    for j in range(0,len(list_oxides)):

        xdata=np.asarray(test_tio2['x']) # get x
        ydata=np.asarray(test_tio2[list_oxides[j]]) #get c

        p0 = 0,np.mean(ydata) # define initial points of m and c0 for iteration

        params,extras = curve_fit(diff_value,xdata,ydata,p0) #fit the function
        print(list_oxides[j],params[1]) # Print parameters
        df=df.append({'Expt':str(list_exp[i]), 'Oxide':list_oxides[j],"Slope":params[0],'c0':params[1]}, ignore_index=True) #append the values to the final dataframe
        
df.to_csv('C:/Users/ayersj/OneDrive - Vanderbilt/Papers/SpheneSolubility/DataAnalysis/TitaniteExpts/py_optimized_values.csv')