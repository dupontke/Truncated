#!/bin/bash 
#SBATCH --job-name=mut_3.trunc
#SBATCH --output=mut_3.trunc_prod.err
#SBATCH --time=48:00:00
#SBATCH --nodes=1
##SBATCH --exclusive

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/software/usr/gcc-4.9.2/lib64"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/software/usr/tcl-8.6.3/lib"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/software/usr/hpcx-v1.2.0-292-gcc-MLNX_OFED_LINUX-2.4-1.0.0-redhat6.6/ompi-mellanox-v1.8/lib"
export AMBERHOME="/mnt/lustre_fs/users/mjmcc/apps/amber16"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$AMBERHOME/lib"

cpptrajhome=$AMBERHOME/AmberTools/bin/
echo $cpptrajhome

time ./truncation.md.py mut_3 $cpptrajhome