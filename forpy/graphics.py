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

    ax1.plot(time_climate, av_irradiance)
    # ax2.plot(time_climate, av_pet)
    ax3.plot(time_climate, av_temp)
    ax4.plot(time_climate, av_rain)
    ax5.plot(time_climate, nee_extend)
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
    print(climate.values[0,0])
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