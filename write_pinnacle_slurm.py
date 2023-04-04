#! /usr/bin/env python3


# import modules
import argparse

# Creating ArgumentParser object
parser = argparse.ArgumentParser(description = "The script creates a \
SlURM file that can be submitted to the cluster")

# add positional(required)arguments
parser.add_argument("job_name", help = "Name of job", type = str)

#  Adding optional arguments
parser.add_argument("-q","--queue", help="Tells the queue to submit \
	(comp01,comp06,comp72)",default='comp72',type=str)
parser.add_argument("-n","--nodes", help="Tells the number of nodes,\
	to run", default='1',type= int)
parser.add_argument("-p","-num_processors", help="Tells the number of \
	processors to request", default='24',type= int)
parser.add_argument("-t","--walltime", help="Tells the length of,\ 
	job", default='72', type=int)

# Parse the actual arguments
# Access argument values via 'args' variable 
args = parser.parse_args()

# print()
#print SBATCH commands
print('#SBATCH --job-name=' + args.job_name)
print('#SBATCH --partition', args.queue)
print('#SBATCH --nodes=' + str(args.num_nodes))
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=' + str(args.num_processors))
print('#SBATCH --time=' + str(args.walltime) + ':00:00')
print('#SBATCH -o atg002_%.out')
print('#SBATCH -e atg002_%.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=atg002@uark.edu')


print()

#purge all the modules
print('module purge')

print()

#cd into the submit directory
print('cd $SLURM_SUBMIT_DIR')

print()

print('# job command here')

