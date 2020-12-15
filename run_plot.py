from forpy import prep_climate_cflux, plot_climate_cflux


project_path = "Projects/Project_Madagascar_Betampona/"
climate_file = 'fractional-change_DID_frac_0.8_climate_400y.txt'

cflux_file = "madagascar_"+'_'.join(climate_file.split('_')[:4])+'.cflux'
cflux_path = project_path+'results/madagascar_fractional-change_DID_frac_0.8.cflux'
climate_path = project_path+'formind_parameters/Climate/'+climate_file

nee_arr, data_climate, time = prep_climate_cflux(cflux_path, climate_path, 10)
plot_climate_cflux(nee_arr, data_climate, time)