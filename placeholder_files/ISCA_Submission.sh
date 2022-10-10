#!/bin/bash
#SBATCH --export=ALL # export all environment variables to the batch job
#SBATCH -D . # set working directory to .
#SBATCH -p pq # submit to the parallel queue
#SBATCH --time=00:50:00 # maximum walltime for the job
#SBATCH -A Research_Project-CEMPS-00006 # research project to submit under
#SBATCH --nodes=1 # specify number of nodes
#SBATCH --ntasks-per-node=$1 # specify number of processors per node
#SBATCH --mem=16GB # specify bytes memory to reserve
#SBATCH --mail-type=END # send email at job completion
#SBATCH --mail-user=wb342@exeter.ac.uk # email address
#Commands you wish to run must go here, after the SLURM directives


module load DEDALUS/2.2006-foss-2020a 
# module load gmpich/2017.08
module load FFmpeg/4.2.2-GCCcore-9.3.0 

printf "Simulation begin"
time mpirun -np $1 python3 "Hight_Normalisation_(KHH).py"
printf "Merge begin"
time python3 merge.py snapshots
printf "Plot begin"
time python3 Plot_Disc.py
printf "Render begin"
time ffmpeg -framerate 25 -i plots/plot%04d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p Animation.mp4
printf "End"
