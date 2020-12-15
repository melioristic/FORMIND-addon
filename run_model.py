from forpy import Formind

model_path = ''	
par_file_name='madagascar'
project_path='Projects/Project_Madagascar_Betampona/'
num_sim = 10
climate_file_ori = 'climate_400y.txt'




scenario = 'percentage-change'
climate_file = 'percentage-change_DUU_perc_80_climate_400y.txt'
sim_id = climate_file.split('.')[0]
model = Formind(model_path, project_path, par_file_name)
#model.generate_scenario_climate(climate_file_ori, scenario, perc=80)
model.run(sim_id=sim_id, num_sim=num_sim)