#! /usr/bin/env python3

job_name = input('Write job name: ')
number_queue = input('Write the number of queue: ')
number_nodes = input('Type the number of nodes: ')
num_cores = input('Write the number of task per node: ')
wall_time = input('Write time per job format as Hr:Min:Sec: ')
mail_type = ('Write ALL: ')
email_uark = input('Write email_uark or an email: ')


print('!/bin/bash')

print('#SBATCH --job-name=',job_name)
print('#SBATCH --partition',number_queue)
print('#SBATCH --nodes=',number_nodes)
print('#SBATCH --tasks-per-node=',num_cores)
print('#SBATCH --time=',wall_time)
print('#SBATCH -o %',job_name,'.out')
print('#SBATCH -e %',job_name,'.err')
print('#SBATCH --mail-type=',mail_type)
print('#SBATCH --mail-user=',email_uark)

print('cd $SLURM_SUBMIT_DIR')
print('# job command')

# job command here

