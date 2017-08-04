
# coding: utf-8

# # Non-Ideal Shock Tube Example
# ## Ignition delay time computations in a high-pressure reflected shock tube reactor
# 
# In this example we will illustrate how to setup and use a constant volume, adiabatic reactor to simulate reflected shock tube experiments. This reactor will then be used to compute the ignition delay of a gas at any temperature and pressure.  The example very explicitly follows the form set in batch_reactor_ignition_delay_NTC.pynb, which does very similar calculations, but with an IdealGasReactor.  All credit is due to the developer of that example.  This example generalizes that work to use a Reactor with no pre-assumed EoS.  One can also run ideal gas phases through this simulation, simply by specifying a cti file with that thermodynamic EoS.
# 
# The reactor (system) is simply an insulated box, and can technically be used for any number of equations of state and constant-volume, adiabatic reactors.  The example here demonstrates the calculations carried out by G. Kogekar, et al., "Impact of non-ideal behavior on ignition delay and chemical kinetics in high-pressure shock tube reactors," Combust. Flame., 2017.
# 
# Other than the typical Cantera dependencies, plotting functions require that you have matplotlib installed, and data storing and analysis requires pandas. See https://matplotlib.org/ and http://pandas.pydata.org/index.html, respectively, for additional info.

# In[1]:

from __future__ import division
from __future__ import print_function

import pandas as pd
import numpy as np

import time

import cantera as ct
print('Runnning Cantera version: ' + ct.__version__)


# Define the gas
# In this example we will choose a stoichiometric mixture of n-dodecane and air as the gas. For a representative kinetic model, we use that developed by Wang, Ra, Jia, and Reitz (https://www.erc.wisc.edu/chem_mech/nC12-PAH_mech.zip) by [H.Wang, Y.Ra, M.Jia, R.Reitz, Development of a reduced n-dodecane-PAH mechanism. and its application for n-dodecane soot predictions., Fuel 136 (2014) 25–36]

# In[2]:

gas = ct.Solution('../data/WangMechanismRK.cti')


# ### Define reactor conditions : temperature, pressure, fuel, stoichiometry

# In[3]:

# Define the reactor temperature and pressure:
reactorTemperature = 1000 #Kelvin
reactorPressure = 40.0*101325.0 #Pascals

# Set the state of the gas object:
gas.TP = reactorTemperature, reactorPressure

# Define the fuel, oxidizer and set the stoichiometry:
gas.set_equivalence_ratio(phi=1.0, fuel='c12h26', oxidizer={'o2':1.0, 'n2':3.76})

# Create a reactor object and add it to a reactor network
# In this example, this will be the only reactor in the network
r = ct.Reactor(contents=gas)
reactorNetwork = ct.ReactorNet([r])

# now compile a list of all variables for which we will store data
stateVariableNames = [r.component_name(item) for item in range(r.n_vars)]

# Use the above list to create a DataFrame
timeHistory = pd.DataFrame(columns=stateVariableNames)


# ### Define useful functions

# In[4]:

def ignitionDelay(df, species):
    """
    This function computes the ignition delay from the occurence of the
    peak in species' concentration.
    """
    return df[species].argmax()


# In[5]:

#Tic
t0 = time.time()

# This is a starting estimate. If you do not get an ignition within this time, increase it
estimatedIgnitionDelayTime = 0.005
t = 0

counter = 1;
while(t < estimatedIgnitionDelayTime):
    t = reactorNetwork.step()
    if (counter%20 == 0):
        # We will save only every 20th value. Otherwise, this takes too long
        # Note that the species concentrations are mass fractions
        timeHistory.loc[t] = reactorNetwork.get_state()
    counter+=1

# We will use the 'oh' species to compute the ignition delay
tau = ignitionDelay(timeHistory, 'oh')

#Toc
t1 = time.time()

print('Computed Ignition Delay: {:.3e} seconds. Took {:3.2f}s to compute'.format(tau, t1-t0))

# If you want to save all the data - molefractions, temperature, pressure, etc
# uncomment the next line
# timeHistory.to_csv("time_history.csv")


# ## Plot the result

# ### Import modules and set plotting defaults

# In[6]:"""

import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams['axes.labelsize'] = 16
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['figure.autolayout'] = True

# ### Figure illustrating the definition of ignition delay time (IDT).

# In[7]:

plt.figure()
plt.plot(timeHistory.index, timeHistory['oh'],'-o',color='b',markersize=4)
plt.xlabel('Time (s)',fontname='Times New Roman')
plt.ylabel('$\mathdefault{OH\, mass\, fraction,}\,  Y_{OH}}$',fontname='Times New Roman')

# Figure formatting:
plt.xlim([0,0.00075])
ax = plt.gca()
font = plt.matplotlib.font_manager.FontProperties(family='Times New Roman',size=14)
ax.annotate("",xy=(tau,0.005), xytext=(0,0.005),arrowprops=dict(arrowstyle="<|-|>",color='r',linewidth=2.0),fontsize=14,)
plt.annotate('Ignition Delay Time (IDT)', xy=(0,0), xytext=(0.00004, 0.00525), family='Times New Roman',fontsize=16);

for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(12)
    tick.label1.set_fontname('Times New Roman')
for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontsize(12)
    tick.label1.set_fontname('Times New Roman')


# ## Illustration : NTC behavior
# In the paper by Kogekar, et al., the reactor model is used to demonstrate the impacts of non-ideal behavior on IDTs in the **N**egative **T**emperature **C**oefficient region, where observed IDTs, counter to intuition, increase with increasing temperature.

# ### Define the temperatures for which we will run the simulations

# In[8]:

# Make a list of all the temperatures we would like to run simulations at
T = [1800, 1600, 1400, 1200, 1100, 1075, 1050, 1025, 1000, 975, 950, 925, 900, 850, 825, 800,
     750, 700]

estimatedIgnitionDelayTimes = np.ones(len(T))

estimatedIgnitionDelayTimes[:] = 0.005

# Now create a dataFrame out of these
ignitionDelays = pd.DataFrame(data={'T':T})
ignitionDelays['ignDelay'] = np.nan


# Now, what we will do is simply run the code above the plots for each temperature.

# In[9]:

for i, temperature in enumerate(T):
    # Setup the gas and reactor
    reactorTemperature = temperature
    reactorPressure = 40.0*101325.0
    gas.TP = reactorTemperature, reactorPressure
    gas.set_equivalence_ratio(phi=1.0, fuel='c12h26', oxidizer={'o2':1.0, 'n2':3.76})
    r = ct.Reactor(contents=gas)
    reactorNetwork = ct.ReactorNet([r])

    # Create and empty data frame
    timeHistory = pd.DataFrame(columns=timeHistory.columns)

    t0 = time.time()

    t = 0
    counter = 0
    while t < estimatedIgnitionDelayTimes[i]:
        t = reactorNetwork.step()
        if not counter % 20:
            timeHistory.loc[t] = r.get_state()
        counter += 1

    tau = ignitionDelay(timeHistory, 'oh')
    t1 = time.time()

    print('Computed Ignition Delay: {:.3e} seconds for T={}K. Took {:3.2f}s to compute'.format(tau, temperature, t1-t0))

    ignitionDelays.set_value(index=i, col='ignDelay', value=tau)


# ### Figure: ignition delay ($\tau$) vs. the inverse of temperature ($\frac{1000}{T}$). 

# In[10]:

fig = plt.figure()
ax = fig.add_subplot(111)
ax.semilogy(1000/ignitionDelays['T'], ignitionDelays['ignDelay'],'o-',color='b')
ax.set_ylabel('Ignition Delay (s)',fontname='Times New Roman',fontsize=16)
ax.set_xlabel(r'$\mathdefault{1000/T\, (K^{-1})}$', fontsize=16,fontname='Times New Roman')

# Add a second axis on top to plot the temperature for better readability
ax2 = ax.twiny()
ticks = ax.get_xticks()
ax2.set_xticks(ticks)
ax2.set_xticklabels((1000/ticks).round(1))
ax2.set_xlim(ax.get_xlim())
ax2.set_xlabel('Temperature (K)',fontname='Times New Roman',fontsize=16);

for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(12)
    tick.label1.set_fontname('Times New Roman')
for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontsize(12)
    tick.label1.set_fontname('Times New Roman')
for tick in ax2.xaxis.get_major_ticks():
    tick.label1.set_fontsize(12)
    tick.label1.set_fontname('Times New Roman')


plt.show()
# In[ ]:



