#!/bin/bash
#SBATCH --export=ALL # export all environment variables to the batch job
#SBATCH -D . # set working directory to .
#SBATCH -p pq # submit to the parallel queue
#SBATCH --time=00:01:00 # maximum walltime for the job
#SBATCH -A Research_Project-T119422 # research project to submit under
#SBATCH --nodes=1 # specify number of nodes
#SBATCH --ntasks-per-node=2 # specify number of processors per node
#SBATCH --mem=1G # specify bytes memory to reserve
#SBATCH --mail-type=END # send email at job completion
#SBATCH --mail-user=arb233@exeter.ac.uk # email address
#Commands you wish to run must go here, after the SLURM directives

python hello.py

