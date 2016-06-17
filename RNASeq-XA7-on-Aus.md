## RNASeq is to find Differentially Expressed (DE) genes using RNS-Seq reads data.

## Cultivars that are Xoo resistant
* CX134 IRBB7 Indica Note: [6] Xa7
* IRIS 313-10605 DV86 Aus/boro  Note: [2][4] Xa7;Xa5
* CX369 IRBB62 Indica Note: [5] Xa4;Xa7;Xa21
* CX126 IRBB60 Indica Note: [3][4] Xa4;xa5;xa13;Xa21
* CX44 IR58025B Indica Note: [3][4] Xa4;xa5;xa13;Xa21

# REFERENCE:
# [1] Schatz MC, et al. Whole genome de novo assemblies of three divergent strains of rice, Oryza sativa, document novel gene space of 
# aus and indica. Genome Biol. 2014;15(11):506.
# [2] Sakai H, et al. Construction of pseudomolecule sequences of the aus rice cultivar Kasalath for comparative genomics of 
# Asian cultivated rice. DNA Res. 2014 Aug;21(4):397-405.

## Agenda of haplovars application on finding Xa7 gene.
#### Xa7 Target region:
* 1. M5_M5-56K in rice japonica is chr6:27,965,437..28,022,337, Length=56,901 bp.
* 2. M5_M5-56K in rice japonica is redefined as chr6:27,965,001..28,023,000, Length=58,000 bp.
* 3. M5_M5-56K in rice indica is chr6:29,683,670..29,828,319, Length=144,650 bp.
* 4. M5_M5-56K in rice indica is redefined to chr6:29,683,001..29,829,000, Length=146,000 bp.
* 5. M5_M5-56K in rice indica, after removing the artifact insert, Length=66,477 bp.
* 6. M5_M5-56K in rice aus Kasalath is chr6:26,752,440..26,776,166..26,777,887..(27,007,090), Length=25,448 (or 254,651) bp.
* 7. M5_M5-56K in rice aus Kasalath is redefined to chr6:26,625,001..27,007,500, Length=382,500 bp.

* Seven protein-coding genes are included in this region. They will be used as anchors to clarify the shifting regions such as the 17kb region defined \
in LeftFlank and RightFlank.
* Seven genes are: OS06G0673700, OS06G0674000, OS06G0674100, OS06G0674400, OS06G0674800, OS06G0675200, OS06G0675300.
* Among them, there are two pairs of overlapping genes: "OS06G0673700, OS06G0674000", and "OS06G0675200, OS06G0675300".
* So we have total of five anchors in this 58Kb Xa7QTL.
* use 5 Kb and  more on left and right of M5..M5_56K for rfguided assembly; chr6:27960001..28023000, 63 Kb.
* Fine mapping of Xa7 by Dr. Bing Yang Lab at 01/20/2015 indicates the gene is within a 56 kb region between two markers M5 and M5-56k:

#### Xa7QTL was mapped to a genetic interval of 118.5 kb (0.21-cM) between SSR markers GDSSR02 and RM20593 [1]
* RM20593
  * Forward: 5’-AAGGTACACTTGCTCTGACGGTAGCIRGSP-1.0: 25 bp from chr06:28,082,317..28,082,341
  * Reverse: 5’-AGACCTCAGTGGCAAATCCTACGIRGSP-1.0: 23 bp from chr06:28,082,610..28,082,632
* GDSSR02
  * Forward: 5’-TGCCCACCGTCGAACTCGTGG, IRGSP-1.0: 21 bp from chr06:27,963,796..27,963,816
  * Reverse: 5’-AGCTAGCAATTCGCATGATTGCIRGSP-1.0: 22 bp from chr06:27,963,981..27,964,002
* GDSSR02 to RM20593: 118,836 bp from chr06:27,963,796.. 28,082,632
* [1] Shen Chen, et al. High-resolution mapping and gene prediction of Xanthomonas Oryzae pv. Oryzae resistance gene Xa7. Molecular Breeding;2008;22(3):433-441.
		
#### Xa7QTL was mapped to a genetic interval of 200-kb between SSR marker RM20576 and STS marker MY4 [2]
* RM20576 
  * Forward: 5’-CTGTTGCTAGCTTACACGAATTGCIRGSP-1.0: 24 bp from chr06:27,890,361..27,890,384
  * Reverse: 5’-CCGGTAGTACGTCAGCTACTATGCIRGSP-1.0: 24 bp from chr06:27,890,627..27,890,650
* MY4
  * Forward: 5’-CTTCCTTTCCAGGCTTTC IRGSP-1.0: 18 bp from chr06:28,090,186..28,090,203
  * Reverse: 5’-TAGAATTTGCATCATCCCIRGSP-1.0: 18 bp from chr06:28,090,356..28,090,373
* RM20576 to MY4: 200,012  bp from chr06:27,890,361..28,090,373

* [1] Shen Chen, et al. High-resolution mapping and gene prediction of Xanthomonas Oryzae pv. Oryzae resistance gene Xa7. Molecular Breeding;2008;22(3):433-441.
* [2] Zhang, Yuchen, et al. Identification and molecular mapping of the rice bacterial blight resistance gene allelic to Xa7 from an elite restorer line Zhenhui 084. Eur J Plant Pathol;2009;125:235–244. 

# Blastn against rice databases
mkdir -p ${TRegGA_DIR}/run/blastn_Xa7MarkerDNA/
cd ${TRegGA_DIR}/run/blastn_Xa7MarkerDNA/
\cp ${TRegGA_DIR}/doc/M5_56K/XA7MarkerDNA.fa .
BLASTDB=${TRegGA_DIR}/reference/rice_japonica/OsjDNA
DB_REFSEQ=OsjDNA
BLASTDB=${TRegGA_DIR}/reference/rice_indica/OsiDNA
DB_REFSEQ=OsiDNA
BLASTDB=${TRegGA_DIR}/reference/rice_aus/OsaDNA
DB_REFSEQ=OsaDNA
BLASTDB=${TRegGA_DIR}/reference/rice_DJ123/OsdDNA
DB_REFSEQ=OsdDNA

# Blastn against rice subject sequences
SUBJECT=OsaXA7.fa
SUBJECTNAME=OsaXA7
SUBJECT=DJ123_scaffold10.fa
SUBJECTNAME=DJ123_scaffold10
SUBJECT=IRBB7-DJ123_scaffold10.fa
SUBJECTNAME=IRBB7-DJ123_scaffold10
SUBJECT=DV86-DJ123_scaffold10.fa
SUBJECTNAME=DV86-DJ123_scaffold10
SUBJECT=IRBB62-DJ123_scaffold10.fa
SUBJECTNAME=IRBB62-DJ123_scaffold10

# Blastn query sequences 
QUERY=Xa7MarkerDNA.fa
QUERYNAME=Xa7Marker
QUERYSHORT=Xa7Markershort.fa
QUERYNAMESHORT=Xa7Markershort
QUERY=${TRegGA_DIR}/doc/BY_p53P5L2_IRBB7_Xa7.fa
QUERYNAME=p53P5L2_irbb7

# Blastn parameters
OUTFMT='6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore gaps qcovs qcovhsp'
OUTFMT=6
# Use this when query=Xa7Markers
EVALUE="1e-100"
PERC_IDENTITY=92
# Use this when query=Xa7Markershort
EVALUE_SHORT="10"
PERC_IDENTITY_SHORT=100

# Blastn prep
cd ${TRegGA_DIR}/run
mkdir blastn_p53P5L2
cd blastn_p53P5L2
cp /home/huangcy/MYWORK/Xa7QTL/Oryza_sativa_indica_IRBB7_Xa7QTL_p53P5L2/BY_p53P5L2_IRBB7_Xa7.fa .
\cp ${TRegGA_DIR}/run/talen_avrXA7_on_DJ123_scaffold10/*.fa .
\cp ${TRegGA_DIR}/run/talen_avrXA7_on_DJ123_scaffold10/*.embl .

# Blastn against database -db ${BLASTDB}
blastn -db ${BLASTDB} -query ${QUERY} -evalue ${EVALUE} -perc_identity=${PERC_IDENTITY} >\
 blastn.${QUERYNAME}-on-${DB_REFSEQ}.aln
blastn -db ${BLASTDB} -query ${QUERY} -evalue ${EVALUE} -perc_identity=${PERC_IDENTITY} -outfmt "${OUTFMT}" >\
 blastn.${QUERYNAME}-on-${DB_REFSEQ}.table
blastn -db ${BLASTDB} -query ${QUERYSHORT} -task "blastn-short" -word_size 11 -evalue ${EVALUE_SHORT} \
 -perc_identity=${PERC_IDENTITY_SHORT} -outfmt "${OUTFMT}" > blastn.${QUERYNAMESHORT}-on-${DB_REFSEQ}.table
grep "Chr6" blastn.${QUERYNAMESHORT}-on-${DB_REFSEQ}.table > blastn.${QUERYNAMESHORT}-on-${DB_REFSEQ}_Chr6.table

# Blastn against subject sequence -subject ${SUBJECT}
blastn -query ${QUERY} -subject ${SUBJECT} -evalue ${EVALUE} -perc_identity=${PERC_IDENTITY} -outfmt "${OUTFMT}" >\
 blastn.${QUERYNAME}-on-${SUBJECTNAME}.table
blastn -query ${QUERY} -subject ${SUBJECT} -evalue ${EVALUE} -perc_identity=${PERC_IDENTITY} >\
 blastn.${QUERYNAME}-on-${SUBJECTNAME}.aln
blastn -query ${QUERYSHORT} -subject ${SUBJECT} -task "blastn-short" -word_size 11 -evalue ${EVALUE_SHORT} \
 -perc_identity=${PERC_IDENTITY_SHORT} -outfmt "${OUTFMT}" > blastn.${QUERYNAMESHORT}-on-${SUBJECTNAME}.table
blastn -query ${QUERYSHORT} -subject ${SUBJECT} -task "blastn-short" -word_size 11 -evalue ${EVALUE_SHORT} \
 -perc_identity=${PERC_IDENTITY_SHORT} > blastn.${QUERYNAMESHORT}-on-${SUBJECTNAME}.aln
 
## Xa7Markers on OsaXa7 (aus Kasalath)
# Xa7Marker on OsaDNA_Chr6
M5_Xa7QTL_BY    OsaChr6 94.35   336     18      1       152     486     26752440        26752775        6e-144    514   1       36      27
M5_Xa7QTL_BY    OsaChr6 93.44   259     15      1       245     503     27007346        27007090        2e-104    383   2       36      21
M5_56k_Xa7QTL_BY        OsaChr6 97.25   1746    23      13      1       1745    26776166        26777887        0.0      2935   25      100     100
RM20593F_Xa7QTL-118R    OsaChr6 100.00  25      0       0       1       25      26841939        26841963        3e-06   50.1    0       100     100
RM20576F_Xa7QTL-200L    OsaChr6 100.00  24      0       0       1       24      26625287        26625310        1e-05   48.1    0       100     100
RM20576R_Xa7QTL-200L    OsaChr6 100.00  24      0       0       1       24      26625576        26625553        1e-05   48.1    0       100     100
MY4F_Xa7QTL-200R        OsaChr6 100.00  18      0       0       1       18      26849409        26849426        0.016   36.2    0       100     100
MY4R_Xa7QTL-200R        OsaChr6 100.00  18      0       0       1       18      26849561        26849544        0.016   36.2    0       100     100

# Xa7Marker on OsaXa7
M5_Xa7QTL_BY    OsaXA7  94.35   336     18      1       152     486     127439  127774  6e-147    514
M5_Xa7QTL_BY    OsaXA7  93.44   259     15      1       245     503     382345  382089  2e-107    383
M5_56k_Xa7QTL_BY        OsaXA7  97.25   1746    23      13      1       1745    151165  152886  0.0      2935
RM20593F_Xa7QTL-118R    OsaXA7  100.00  25      0       0       1       25      216938  216962  5e-09   50.1
RM20593R_Xa7QTL-118R    OsaXA7  100.00  23      0       0       1       23      217249  217227  6e-08   46.1
GDSSR02R_Xa7QTL-118L    OsaXA7  100.00  11      0       0       10      20      752     762     0.82    22.3
RM20576F_Xa7QTL-200L    OsaXA7  100.00  24      0       0       1       24      286     309     2e-08   48.1
RM20576R_Xa7QTL-200L    OsaXA7  100.00  24      0       0       1       24      575     552     2e-08   48.1
MY4F_Xa7QTL-200R        OsaXA7  100.00  18      0       0       1       18      224408  224425  3e-05   36.2
MY4R_Xa7QTL-200R        OsaXA7  100.00  18      0       0       1       18      224560  224543  3e-05   36.2

# Xa7Marker on IRBB7-OsaXA7
M5_56k_Xa7QTL_BY        IRBB7-OsaXA7    99.14   813     5       1       1       813     157840  158650  0.0      1461   2       81      47
M5_56k_Xa7QTL_BY        IRBB7-OsaXA7    95.64   596     11      3       816     1410    158705  159286  0.0       942   15      81      34
RM20593F_Xa7QTL-118R    IRBB7-OsaXA7    100.00  25      0       0       1       25      228388  228412  5e-09   50.1    0       100     100
RM20576F_Xa7QTL-200L    IRBB7-OsaXA7    100.00  24      0       0       1       24      603     626     2e-08   48.1    0       100     100
RM20576R_Xa7QTL-200L    IRBB7-OsaXA7    100.00  24      0       0       1       24      995     972     2e-08   48.1    0       100     100
MY4F_Xa7QTL-200R        IRBB7-OsaXA7    100.00  18      0       0       1       18      236314  236331  4e-05   36.2    0       100     100
MY4R_Xa7QTL-200R        IRBB7-OsaXA7    100.00  18      0       0       1       18      236501  236484  4e-05   36.2    0       100     100

# Xa7Marker on DV86-OsaXA7
M5_56k_Xa7QTL_BY        DV86-OsaXA7     98.96   673     5       1       1       673     156895  157565  0.0      1203   2       58      39
M5_56k_Xa7QTL_BY        DV86-OsaXA7     97.62   336     7       1       1038    1372    158018  158353  4e-165    575   1       58      19
RM20593F_Xa7QTL-118R    DV86-OsaXA7     100.00  25      0       0       1       25      223389  223413  5e-09   50.1    0       100     100
RM20576F_Xa7QTL-200L    DV86-OsaXA7     100.00  24      0       0       1       24      580     603     2e-08   48.1    0       100     100
MY4F_Xa7QTL-200R        DV86-OsaXA7     100.00  18      0       0       1       18      231077  231094  4e-05   36.2    0       100     100

# Xa7Marker on IRBB62-OsaXA7
M5_56k_Xa7QTL_BY        IRBB62-OsaXA7   99.12   1025    7       1       1       1025    159837  160859  0.0      1842   2       59      59
RM20593F_Xa7QTL-118R    IRBB62-OsaXA7   100.00  25      0       0       1       25      230287  230311  5e-09   50.1    0       100     100
RM20576F_Xa7QTL-200L    IRBB62-OsaXA7   100.00  24      0       0       1       24      559     582     2e-08   48.1    0       100     100
MY4R_Xa7QTL-200R        IRBB62-OsaXA7   100.00  18      0       0       1       18      238209  238192  4e-05   36.2    0       100     100

## Xa7Markers on OsdDNA aus DJ123_scaffold10
# Xa7Marker on DJ123_scaffold10
M5_56k_Xa7QTL_BY        DJ123_scaffold10        98.00   1052    12      7       1       1052    197410  198452  0.0      1818   9       99      60
M5_56k_Xa7QTL_BY        DJ123_scaffold10        96.38   691     13      4       1056    1745    198539  199218  0.0      1127   12      99      40
RM20593F_Xa7QTL-118R    DJ123_scaffold10        100.00  25      0       0       1       25      258179  258203  1e-08   50.1    0       100     100
GDSSR02R_Xa7QTL-118L    DJ123_scaffold10        100.00  12      0       0       11      22      131339  131328  0.62    24.3    0       100     55
RM20576F_Xa7QTL-200L    DJ123_scaffold10        100.00  12      0       0       2       13      803509  803520  0.74    24.3    0       100     50
MY4F_Xa7QTL-200R        DJ123_scaffold10        100.00  18      0       0       1       18      265655  265672  1e-04   36.2    0       100     100
MY4R_Xa7QTL-200R        DJ123_scaffold10        100.00  18      0       0       1       18      265807  265790  1e-04   36.2    0       100     100

# Xa7Marker on IRBB7-DJ123_scaffold10
M5_Xa7QTL_BY    IRBB7-DJ123_scaffold10  93.44   320     18      3       172     489     134920  135238  1e-133    472   3       26      26
M5_56k_Xa7QTL_BY        IRBB7-DJ123_scaffold10  99.14   813     5       1       1       813     213574  214384  0.0      1461   2       80      47
M5_56k_Xa7QTL_BY        IRBB7-DJ123_scaffold10  97.59   373     8       1       1039    1410    214755  215127  0.0       638   1       80      21
M5_56k_Xa7QTL_BY        IRBB7-DJ123_scaffold10  99.03   206     2       0       816     1021    214439  214644  7e-103    370   0       80      12
RM20593F_Xa7QTL-118R    IRBB7-DJ123_scaffold10  100.00  25      0       0       1       25      275500  275524  1e-08   50.1    0       100     100
RM20593R_Xa7QTL-118R    IRBB7-DJ123_scaffold10  100.00  23      0       0       1       23      275815  275793  2e-07   46.1    0       100     100
GDSSR02R_Xa7QTL-118L    IRBB7-DJ123_scaffold10  100.00  12      0       0       11      22      144818  144807  0.66    24.3    0       100     55
RM20576F_Xa7QTL-200L    IRBB7-DJ123_scaffold10  100.00  12      0       0       2       13      839776  839787  0.79    24.3    0       63      50
MY4F_Xa7QTL-200R        IRBB7-DJ123_scaffold10  100.00  18      0       0       1       18      283608  283625  1e-04   36.2    0       100     100
MY4R_Xa7QTL-200R        IRBB7-DJ123_scaffold10  100.00  18      0       0       1       18      283795  283778  1e-04   36.2    0       100     100

# Xa7Marker on DV86-DJ123_scaffold10
M5_56k_Xa7QTL_BY        DV86-DJ123_scaffold10   98.96   673     5       1       1       673     216247  216917  0.0      1203   2       58      39
M5_56k_Xa7QTL_BY        DV86-DJ123_scaffold10   97.63   338     7       1       1036    1372    217482  217819  1e-165    579   1       58      19
RM20593F_Xa7QTL-118R    DV86-DJ123_scaffold10   100.00  25      0       0       1       25      277769  277793  2e-08   50.1    0       100     100
RM20593R_Xa7QTL-118R    DV86-DJ123_scaffold10   100.00  23      0       0       1       23      278084  278062  2e-07   46.1    0       100     100
GDSSR02R_Xa7QTL-118L    DV86-DJ123_scaffold10   100.00  12      0       0       11      22      146899  146888  0.66    24.3    0       100     55
RM20576F_Xa7QTL-200L    DV86-DJ123_scaffold10   100.00  11      0       0       7       17      1430    1420    3.1     22.3    0       71      46
MY4F_Xa7QTL-200R        DV86-DJ123_scaffold10   100.00  18      0       0       1       18      285629  285646  1e-04   36.2    0       100     100
MY4R_Xa7QTL-200R        DV86-DJ123_scaffold10   100.00  18      0       0       1       18      285816  285799  1e-04   36.2    0       100     100

# Xa7Marker on IRBB62-DJ123_scaffold10
M5_56k_Xa7QTL_BY        IRBB62-DJ123_scaffold10 99.12   1025    7       1       1       1025    212943  213965  0.0      1842   2       59      59
RM20593F_Xa7QTL-118R    IRBB62-DJ123_scaffold10 100.00  25      0       0       1       25      277448  277472  2e-08   50.1    0       100     100
GDSSR02R_Xa7QTL-118L    IRBB62-DJ123_scaffold10 100.00  12      0       0       11      22      143542  143531  0.68    24.3    0       95      55
RM20576F_Xa7QTL-200L    IRBB62-DJ123_scaffold10 100.00  12      0       0       2       13      854982  854993  0.81    24.3    0       63      50
MY4F_Xa7QTL-200R        IRBB62-DJ123_scaffold10 100.00  18      0       0       1       18      285203  285220  1e-04   36.2    0       100     100
MY4R_Xa7QTL-200R        IRBB62-DJ123_scaffold10 100.00  18      0       0       1       18      285420  285403  1e-04   36.2    0       100     100

##------------------------------------
## DJ123 scaffold_10 has VERY good coverage on the Xa7QTL region
## Transfer annotaion from rice aus reference Kasalath to rice aus DJ123 scaffold_10:197,410..199,218 
# DJ123 scaffold_10 full length is 1,279,957 bp
# BY_p53P5L2_IRBB7_Xa7 aligned 59,812bp (out of 62,882 bp, or 95.12%) with DJ123_scaffold10.
# BY_p53P5L2_IRBB7_Xa7 aligned 50,087bp (out of 62,882 bp, or 79.65%) with IRBB7-DJ123_scaffold10. 
##-------------------------------------


