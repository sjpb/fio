#!/usr/bin/env bash
# Run fio to test fileysystem performance
# Usage:
#   sbatch -p PARTITION -J JOBNAME fio.sh FIOCONFIG SECTION DIRECTORY
# e.g.:
#   sbatch -p hpc -J azf-4k-seqw fio.sh fio-4k.ini seqw /mnt/azfiles/$USER/

#SBATCH -N 1
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.out
#SBATCH --exclusive

echo SLURMD_NODENAME: $SLURMD_NODENAME
echo SLURM_NODELIST: $SLURM_NODELIST
echo FIOCONFIG: $1
echo SECTION: $2
echo DIRECTORY: $3


sudo yum install -y fio

fio --output-format=json+ --section=$2 --directory=$3 --output=${SLURM_JOB_NAME}.${SLURM_JOB_ID}.json $1
