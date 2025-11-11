#!/bin/bash
# ================================
#   HPC Tools - Default SLURM Job
# ================================

#SBATCH -A {account}
#SBATCH -p {partition}
#SBATCH -t {time}
#SBATCH --nodes={nodes}
#SBATCH --ntasks={ntasks}
#SBATCH --cpus-per-task={cpus}
#SBATCH --output=run_out.o%j
#SBATCH --error=run_err.e%j

module purge
module load GCC/13.3.0
module load Score-P/8.0

DATE=$(date +"%Y-%m-%d_%H-%M")
EXEC={exe}
RUNS={runs}
THREADS="1"

mkdir -p results

for nt in $THREADS; do
    export OMP_NUM_THREADS=$nt
    echo "→ Running with $nt thread(s)"

    for run in $(seq 1 $RUNS); do
        RUN_DIR="results/${{DATE}}_${{nt}}t_run${{run}}"
        mkdir -p "$RUN_DIR"

        SCOREP_EXPERIMENT_DIRECTORY="${{RUN_DIR}}/scorep" \
            perf stat -r 1 -e cycles,instructions,task-clock \
            $EXEC > "${{RUN_DIR}}/output.log" 2> "${{RUN_DIR}}/perf.log"
    done
done
