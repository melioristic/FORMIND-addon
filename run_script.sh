#$ -binding linear:1
#$ -l h_rt=04:00:00
#$ -l h_vmem=8G

module load Anaconda3

source activate FORPY38

python /home/anand/github/FORMIND-addon/run_model.py