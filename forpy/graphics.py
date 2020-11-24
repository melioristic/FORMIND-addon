#
# Created on Mon Nov 23 2020
#
# Copyright (c) 2020 Mohit Anand
#
# For any details contact itsmohitanand@gmail.com 
#


## The goal of this script is to create plots from the output of forest model with mininum dependencies. 


import pandas as pd
import matplotlib.pylab as plt
import numpy as np
def plot_climate_cflux(cflux_path: str, climate_path: str, plot_path:str=".")-> None:
    """The function plots the carbon flux with climatological data
    Args:
    	cflux_path (str): The path to cflux ouput file.
		climate_path (str): The path to climate data input file.
        plot_path (str): The path to the ouput graph.
		
	Returns:
		None: And plots in the specified folder
	"""

    cflux = pd.read_csv(cflux_path, delimiter="\t", skiprows=2)    
    time = cflux["Time"].values
    nee = cflux["NEE"].values
    
    # Read the climate file
    climate = read_climate(climate_path)
    
    rain = climate["rain[mm]"].values
    temp = climate["temperature[C]"].values
    irradiance = climate["irradiance[mumol/s/m2]"].values
    daylength = climate["day_length[h]"].values
    pet = climate["PET[mm]"].values

    av_rain = _average_annualy(rain)
    av_temp = _average_annualy(temp)
    av_irradiance = _average_annualy(irradiance)
    # av_daylength = _average_annualy(daylength)
    # av_pet = _average_annualy(pet)

    time_climate = np.zeros_like(av_rain)
    diff = time_climate.shape[0] - time.shape[0]

    av_rain = _average_annualy(rain)

    time_climate[diff:] = time[:]
    time_climate[:diff] = np.arange(-diff,0)
   
    #fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5,1, figsize=(12,8))
    
    fig, (ax1, ax3, ax4, ax5) = plt.subplots(4,1, figsize=(16,10))

    nee_extend = np.full_like(time_climate, np.nan)
    nee_extend[diff:] = nee

    ax1.plot(time_climate, av_irradiance, color = "darkorange")
    ax1.set_xlim(left = time_climate[0], right = time_climate[-1])
    ax1.set_ylabel("Solar Irradiance [$\mu mol$ $s^{-1}$ $m^{-2}$]")
    
    # ax2.plot(time_climate, av_pet)
    ax3.plot(time_climate, av_temp, color = "indianred")
    ax3.set_xlim(left = time_climate[0], right = time_climate[-1])
    ax3.set_ylabel(u'Temperature $[\u00B0C]$')
    

    ax4.bar(time_climate, av_rain, color = "mediumblue")
    ax4.set_xlim(left = time_climate[0], right = time_climate[-1])
    ax4.set_ylabel("Precipitation [$mm$ $d^{-1}$]")

    ax5.plot(time_climate, nee_extend, color = "k")
    nee_positive = np.where(nee_extend<0, 0, nee_extend)
    nee_negative = np.where(nee_extend>0, 0, nee_extend)
    ax5.fill_between(time_climate, nee_positive, color = "slateblue")
    ax5.fill_between(time_climate, nee_negative, color = "lightcoral")
    ax5.axhline(color = "k", linestyle = "--")
    ax5.set_ylabel("NEE [$t_C$ $ha^{-1}$ $a^{-1}$]")
    ax5.set_xlabel("Time [Years]")
    ax5.set_xlim(left = time_climate[0], right = time_climate[-1])
    plt.tight_layout()
    plt.show()    
    return cflux


def read_climate(climate_path: str)->pd.DataFrame:
    """  The climate data is read from the txt file
	Args:
		climate_path (str): The path to the climate text file.

	Returns:
		pd.DataFrame: pandas dataframe of climate data

	""" 

    climate = pd.read_csv(climate_path, delimiter="\t", skiprows=1, header=None)
    climate.columns = ["rain[mm]","temperature[C]","irradiance[mumol/s/m2]","day_length[h]","PET[mm]"]    
    
    return climate

def _average_annualy(data:np.array)->np.array:
    
    """ Annual average values is calculated from daily values.
        The year is of 365 days
	Args:
		data (np.array): 1-d np.array of values
	Returns:
		np.array: The annual average of the daily data

	""" 
    num_years = data.shape[0]//365
    data_avg = np.zeros((num_years))
    for i in range(num_years):
        data_avg[i] = np.mean(data[365*i:365*(i+1)]) 

    return data_avg

project_path = "Projects/Project_Tansania_Kilimanjaro/"
cflux_file = "results/KiLi_FLM3_PFT6.cflux"
climate_file = "formind_parameters/Climate/KiLi.climate.txt"

cflux_path = project_path+cflux_file
climate_path = project_path+climate_file

plot_climate_cflux(cflux_path, climate_path)