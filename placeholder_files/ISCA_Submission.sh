#!/bin/bash
#SBATCH --export=ALL # export all environment variables to the batch job
#SBATCH -D . # set working directory to .
#SBATCH -p pq # submit to the parallel queue
#SBATCH --time=6:00:00 # maximum walltime for the job
#SBATCH -A Reseach_Project-CEMPS-00006 # research project to submit under
#SBATCH --nodes=1 # specify number of nodes
#SBATCH --ntasks-per-node=$1 # specify number of processors per node
#SBATCH --mem=40GB # specify bytes memory to reserve
#SBATCH --mail-type=END # send email at job completion
#SBATCH --mail-user=wb342@exeter.ac.uk # email address
#Commands you wish to run must go here, after the SLURM directives


module load DEDALUS/2.2006-foss-2020a 
# module load gmpich/2017.08
# module load 

mpirun -np $1 python3 "Hight_Normalisation_(KHH).py"
python3 merge.py snapshots
python3 plot.py
ffmpeg -framerate 25 -i plot%04d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p Animation.mp4
