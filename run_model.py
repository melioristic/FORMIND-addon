from forpy import Formind

model_path = ''	
par_file_name='madagascar'
project_path='Projects/Project_Madagascar_Betampona/'
num_sim = 1
climate_file_ori = 'climate_400y.txt'




scenario = 'fractional-change'
climate_file = 'fractional-change_DID_frac_0.5_climate_400y.txt'
sim_id = '_'.join(climate_file.split('_')[:4])

model = Formind(model_path, project_path, par_file_name)
# model.generate_scenario_climate(climate_file_ori, scenario, frac=0.5)
model.run(sim_id=sim_id, num_sim=num_sim)