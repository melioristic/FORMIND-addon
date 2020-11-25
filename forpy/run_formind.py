#
# Created on Tue Nov 24 2020
#
# Copyright (c) 2020 Mohit Anand
#
# For any details contact itsmohitanand@gmail.com 
######################

# This script is used to run multiple simulations for FORMIND model with different seeds and output names.

import os


def run_formind(cmd_path: str, num_simulation: int = 10) -> None:

	"""
	The function runs number of simulations of FORMIND model 
	Args:
		cmd_path (str): The path of the command file of FORMIND.
		num_simulation (:obj:`int`, optional): The number of simulation to be 	  genrated. The value defaults to 10.
			
	Returns:
		None: The function creates multiple cflux files

	"""
    
	for i in range(num_simulation):
		os.system('cmd run_formind.cmd')