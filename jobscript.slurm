#!/bin/bash -l
#SBATCH --account=lp_h_ds_2023_2024
#SBATCH --nodes=1                            
#SBATCH --time=02:00:00                      
#SBATCH --cluster=wice                       
#SBATCH --job-name=bloom_benchmark           
#SBATCH --output=Benchmark_AUG_output.txt  
#SBATCH --error=Benchmark_AUG_error.txt    
#SBATCH --ntasks=1                           
#SBATCH --mail-user=abdelrahmanadelahmed.elreweny@student.uhasselt.be
#SBATCH --mail-type=BEGIN,END,FAIL

workdir=$SLURM_SUBMIT_DIR
cd $workdir

export PATH="${VSC_DATA}/miniconda3/bin:${PATH}"
source activate science

python Benchmark_AUG.py &> output.out

