#!/home/huangcy/src/anaconda3/bin/python3.5
# author: huangcy
# -*- coding: utf-8 -*-

"""
Last update 6/14/2016
Author: Huang, Chun-Yuan

# this takes inputs of:
1. sequence file, single fasta sequence.
2. start position (winStart) for slidingWindow process,
3. window size (winSize) of bases for splitting,
4. step size (stepSize) for stepping through the sliding windows (default to be the same as the winSize so no overlapping in the annotation.
    For RNASeq DE gene analysis, there should be no overlapping in the annotation to avoid complication in interpreting the mapped read counts),
5. gff output file name
Usage: python annotation_by_sliding_window.py myseq.fa 1 1000 1000 myseq.gff

The GFF (General Feature Format) format consists of one line per feature, each containing 9 columns of data, plus optional track definition lines.
Fields must be tab-separated. Also, all but the final field in each feature line must contain a value; "empty" columns should be denoted with a '.'
Important note: the seqname must be one used within Ensembl, i.e. a standard chromosome name or an Ensembl identifier
 such as a scaffold ID, without any additional content such as species or assembly.

1. seqname - name of the chromosome or scaffold;
2. source - name of the program that generated this feature, or the data source (database or project name)
3. feature - feature type name, e.g. Gene, Variation, Similarity
4. start - Start position of the feature, with sequence numbering starting at 1.
5. end - End position of the feature, with sequence numbering starting at 1.
6. score - A floating point value.
7. strand - defined as + (forward) or - (reverse).
8. frame - One of '0', '1' or '2'. '0' indicates that the first base of the feature is the first base of a codon, '1' that the second base is the first bas\
e of a codon, and so on..
9. attribute - A semicolon-separated list of tag-value pairs, providing additional information about each feature.

GTF example:
p53_P5L2_sequence AUGUSTUS exon 1 1000 1 + 0 "transcript_id ""g1.t1""; gene_id ""g1"";"
p53_P5L2_sequence AUGUSTUS exon 1001 2000 1 + 0 "transcript_id ""g2.t1""; gene_id ""g2"";"
p53_P5L2_sequence AUGUSTUS exon 2001 3000 1 + 0 "transcript_id ""g3.t1""; gene_id ""g3"";"

"""

def slidingWindow(sequence, winStart, winSize, stepSize, outfile):
    from Bio import SeqIO
    SeqRecord = SeqIO.read(sequence, "fasta")
    seqLen = len(SeqRecord.seq)
    # Pre-compute number of steps to emit
    stepNum = (seqLen - winStart - winSize) / stepSize
    winRemainder = seqLen % winSize
    if winRemainder > 0:
        stepNum = stepNum + 1

    # Do the work
    output_file = open(outfile,"a")
    SEQNAME = sequence
    SOURCE = "slidingWindow"
    FEATURE = "exon"
    SCORE = 1
    STRAND = "+"
    FRAME = 0
    GENE_COUNT = 0
    for i in range(winStart, (winStart + stepNum * stepSize), stepSize):
        GENE_COUNT = GENE_COUNT + 1
        START = i
        END = i + winSize -1
        GENE_ID = '"' + "gene" + str(GENE_COUNT) + '"' + ";"
        TRANSCRIPT_ID = '"' + "gene" + str(GENE_COUNT) + ".t1" + '"' + "; "
        ATTRIBUTE = 'transcript_id ' + TRANSCRIPT_ID + 'gene_id ' + GENE_ID
        seq_gtf = SEQNAME+"\t"+SOURCE+"\t"+FEATURE+"\t"+str(START)+"\t"+str(END)+"\t"+str(SCORE)+"\t"+STRAND+"\t"+str(FRAME)+"\t"+ATTRIBUTE+"\n"
        output_file.write(seq_gtf)
    output_file.close()
    
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("infile", type=str, help="input file with single fasta entry")
parser.add_argument("winStart", type=int, default=1, help="sliding window start position")
parser.add_argument("winSize", type=int, default=1000, help="sliding window size")
parser.add_argument("stepSize", type=int, default=1000, help="sliding window step size") 
parser.add_argument("outfile", type=str, help="output file")

if __name__ == '__main__':
    args = parser.parse_args()
    slidingWindow(args.infile, args.winStart, args.winSize, args.stepSize, args.outfile)


