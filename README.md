Run fio under Slurm to test filesystem performance from a single node, with postprocessing to generate csv-format.

# fio.sh
An sbatch script. This installs the `fio` package on the node it lands on, so you need sudo rights on the nodes.
See top of script for how to run it - the `SECTION` refers to the section in the ini file you use (i.e. either `seqr` or `seqw`)

# process.py
Pass this a list of `*.json` files created by running fio.sh `repeatedly` to generate csv-format data on stdout. Requires python3.
