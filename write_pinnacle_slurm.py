#! /usr/bin/env python3


# import modules
import argparse

# Creating ArgumentParser object
parser = argparse.ArgumentParser(description = "The script creates a .slurm file \
so it can be submitted to the cluster")

# add positional(required)arguments
parser.add_argument("job_name", help = "Name of job", type= str)

# Optional arguments
# The default for 'store_true' is . . . "False"
parser.add_argument('-q','--queue', help='Tells the queue to submit the job to(default=comp1)')
parser.add_argument('-n','--nodes', help='Tells the number of nodes to run on(default=1)')
parser.add_argument('-p','--processors', help='Tells the number of processors to use(default=1)')
parser.add_argument('-t','--walltime', help='Tells the allotted number of hours/job(default= 01)')

# parse the actual arguments
# Access the argument values via "args" variable
args = parser.parse_args()

#Creating a Slurm script

batch_script =open(args.job_name + '.slurm','w')
batch_script.write(#!/bin/bash\n\n)
#SBATCH --job-name='+args.job_name + '\n\
#SBATCH --partition')

if args.queue:
	batch_script.write(args.queue + '\n\')
else:
	batch_script.write('comp01'\n')

batch_script.write('#SBATCH --nodes=')
if args.nodes:
	batch_script.write('32\n')

batch_script('#SBATCH --tasks-per-node=')
if args.processors:
	batch_script.write(args.processors + '\n')
else:
	batch_script.write('1\n')

batch_script.write(#SBATCH--time=')
if args.walltime:
	batch_script.write(args.walltime + ':00:00\n')
else:
	batch_script.write('01:00:00\n')

batch_script.write('#SBATCH -o' + args.job_name + '%.out\n\
#SBATCH -e' + args.job_name + '%.err\n\
#SBATCH --mail-type=ALL\n\
#SBATCH --mail-user=atg002@uark.edu\n\n\

cd $SLURM_SUBMIT_DIR\n\
n\
# job command here:'
)

