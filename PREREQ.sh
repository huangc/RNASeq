#!/bin/bash
source ./0SOURCE

## Prerequisite data:
# The soapdenovo2-assembled contigs of genomic samples.
# The reference sequence.
# The paired-TALEN (pTALEN) repeat variable diresidue (RVD).

## Prerequisite software:
# NCBI BLAST+
# blat/35 (The BLAST-Like Alignment Tool)
# TALE-NT2 Target Finder 

##--------------------------------------------
# Setup sub-directory for workflow
cd ${WORK_DIR}
mkdir -p ${WORK_DIR}/prereq
mkdir -p ${WORK_DIR}/doc
mkdir -p ${WORK_DIR}/bin
mkdir -p ${WORK_DIR}/src
mkdir -p ${WORK_DIR}/data
mkdir -p ${WORK_DIR}/run
mkdir -p ${WORK_DIR}/scratch


## Retrieve and index the reference genome
echo "
#!/bin/bash
#PBS -m abe
#PBS -l nodes=1:ppn=8,vmem=20gb,walltime=00:30:00
#PBS -N prereq-on-${REFSEQNAME}
#PBS -j oe

cd ${prereq_DIR}

# Retrieve and index the reference sequence for Blast
sh ${bin_DIR}/xgetseq
" > prereq-on-${REFSEQNAME}.qsub
qsub prereq-on-${REFSEQNAME}.qsub

