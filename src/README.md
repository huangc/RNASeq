## Software Prerequisites
With a couple of exceptions (KmerGenie and Trimmomatic), all software prerequisites simply need to be placed in your `$PATH` for RNASeq to work properly.

### BioPython

See http://biopython.org/wiki/Main_Page.
Last update: December 7th, 2015.

If you have administrative privileges on the machine, use your [package manager](http://biopython.org/wiki/Download#Packages) for best results.
Otherwise, we recommend using virtualenv and pip.

```bash
pip install biopython
```

### BLAST

* See https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download.
* Last update: Dec. 2015

```bash
cd $TRegGA_DIR/local/src/
mkdir blast
cd blast
wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.3.0/ncbi-blast-2.3.0+-x64-linux.tar.gz
tar -xzf ncbi-blast-2.3.0+-x64-linux.tar.gz
export PATH=$PATH:$TRegGA_DIR/local/src/blast//ncbi-blast-2.3.0+/bin
```

### Bowtie

See http://bowtie-bio.sourceforge.net/index.shtml.
Last update: December 3, 2015

```bash
cd $TRegGA_DIR/local/src/
wget https://github.com/BenLangmead/bowtie/archive/v1.1.2.tar.gz
tar -xzf v1.1.2.tar.gz
cd bowtie-1.1.2/
make
make prefix=$TRegGA_DIR/local/ install
```

### Bowtie2

See http://bowtie-bio.sourceforge.net/bowtie2/index.shtml.
Last update: December 3, 2015

```bash
cd $TRegGA_DIR/local/src/
wget https://github.com/BenLangmead/bowtie2/archive/v2.2.5.tar.gz
tar -xzf v2.2.5.tar.gz
cd bowtie2-2.2.5/
make
cp bowtie2* $TRegGA_DIR/local/bin/
```

### BWA

See http://bio-bwa.sourceforge.net.
Last update: December 3, 2015.

```bash
cd $TRegGA_DIR/local/src/
wget https://github.com/lh3/bwa/archive/0.7.12.tar.gz
tar -xzf 0.7.12.tar.gz
cd bwa-0.7.12/
make
cp bwa $TRegGA_DIR/local/bin/
```

### EMBOSS

See http://emboss.open-bio.org.
Last update: December 3, 2015.

```bash
cd $TRegGA_DIR/local/src/
# Link is broken!
wget ftp://emboss.open-bio.org/pub/EMBOSS/EMBOSS-latest.tar.gz
tar -xzf EMBOSS-6.6.0.tar.gz
cd EMBOSS-6.6.0
./configure --prefix=$TRegGA_DIR/local/
make
make install
```

### FASTQC

See http://www.bioinformatics.babraham.ac.uk/projects/fastqc.
Last update: July 5, 2015.

```bash
cd $TRegGA_DIR/local/src/
wget http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.3.zip
unzip fastqc_v0.11.3.zip
chmod a+x FastQC/fastqc
ln -s $(pwd)/FastQC/fastqc $TRegGA_DIR/local/bin/fastqc
```


### R

For installation instructions, see https://www.r-project.org.

### Samtools

See http://www.htslib.org.
Last update: December 3, 2015.

```bash
cd $TRegGA_DIR/local/src/
wget https://github.com/samtools/samtools/releases/download/1.2/samtools-1.2.tar.bz2
tar -xjf samtools-1.2.tar.bz2
cd samtools-1.2/
make prefix=$TRegGA_DIR/local
make prefix=$TRegGA_DIR/local install
```

### RSEM
EBSeq (that is included in the RSEM-1.2.9 and above). 

### Trimmomatic

See http://www.usadellab.org/cms/index.php?page=trimmomatic.
Last update: July 5, 2015.

```bash
cd $TRegGA_DIR/local/src/
wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.33.zip
unzip Trimmomatic-0.33.zip
```

**Note**: Trimmomatic is distributed as a Java .jar file.
The path of the .jar file must be placed in the `$TRegGA_DIR/TRegGA.config` file.
