from hpctools.utils import load_template, write_file, success, error, timestamp

def generate_slurm(
    account, partition, time, nodes, ntasks, cpus, exe, runs,
    use_template: bool = False,
    template_name: str = "slurm_default.sh",
) -> bool:
    """
    Generate a SLURM job script either from a template or from direct parameters.
    """
    try:
        if use_template:
            template = load_template(template_name)
            slurm = template.format(
                account=account,
                partition=partition,
                time=time,
                nodes=nodes,
                ntasks=ntasks,
                cpus=cpus,
                exe=exe,
                runs=runs,
                date=timestamp(),
            )
        else:
            # inline fallback version
            slurm = f"""#!/bin/bash
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
THREADS="1"
RUNS={runs}

mkdir -p results

for nt in $THREADS; do
    export OMP_NUM_THREADS=$nt
    echo "→ Running with $nt thread(s)"
    for run in $(seq 1 $RUNS); do
        RUN_DIR="results/${{DATE}}_${{nt}}t_run${{run}}"
        mkdir -p "$RUN_DIR"
        SCOREP_EXPERIMENT_DIRECTORY="${{RUN_DIR}}/scorep" \\
            perf stat -r 1 -e cycles,instructions,task-clock \\
            $EXEC > "${{RUN_DIR}}/output.log" 2> "${{RUN_DIR}}/perf.log"
    done
done
"""

        write_file("run_job.slurm", slurm)
        success("SLURM script successfully generated.")
        return True

    except Exception as e:
        error(f"Failed to create SLURM script: {e}")
        return False
