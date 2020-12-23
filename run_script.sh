#$ -binding linear:1
#$ -l h_rt=20:00:00
#$ -l h_vmem=4G

module load Anaconda3

source activate FORPY38

python ~/github/FORMIND-addon/download_data.py