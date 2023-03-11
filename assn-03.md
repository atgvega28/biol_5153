# Alexandra Vega 
# HW3
# BIOL 5153

1. ``` rsync -av mt_genomes atg002@hpc-portal2.hpc.uark.edu:/storage/atg002 ```

2. ``` scp unknown.fa atg002@hpc-portal2.hpc.uark.edu:/storage/atg002/mt_genomes/ ```
3. ```#!/bin/bash```
```#SBATCH --job-name=assign3batchun```
```#SBATCH --partition condo```
```#SBATCH --constraint 4a100&harris```
```#SBATCH --nodes=1```
```#SBATCH --qos comp```
```#SBATCH --tasks-per-node=1```
```#SBATCH --time=00:01:00```
```#SBATCH -o assig3batch_%j.out```
```#SBATCH -e assig3batch_%j.err```
```#SBATCH --mail-type=ALL```
```#SBATCH --mail-user=atg002@uark.edu```
```module purge```
```module load blast```
```cat /storage/atg002/mt_genomes/*.fasta > /storage/atg002/mt_genomes/genomes.fas```
```makeblastdb -in genomes.fas -dbtype nucl```
```blastn -query unknown.fa -db genomes.fas > unkown.vs.genomes.blastn```

4. ``` rsync -av atg002@hpc-portal2.hpc.uark.edu:/storage/atg002/mt_genomes/ . ```

5. *```0.060945 seconds.```
 *```none```



