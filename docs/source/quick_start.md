# User guide

## Parameters

To view command-line parameters type `miRge-build -h`:
```
    
usage: miRge-build [options]

miRge-build (Enables building small-RNA libraries for organism of choice to use in miRge3.0 pipeline)
optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit

Options:
  -g,     --genome             genome file in fasta format (.fna, .fasta or .fa) (Required)
  -mmf,   --mature-mir         mature miRNA file in fasta format (Required)
  -hmf,   --hpin-mir           hairpin miRNA file in fasta format (Required)
  -mtf,   --mature-trna        mature tRNA file in fasta format (Required)
  -ptf,   --pre-trna           precursor tRNA file in fasta format (Required)
  -snorf, --snorna             snoRNA file in fasta format (Required)
  -rrf,   --rrna               rRNA file in fasta format (Required)
  -ncof,  --ncrna-other        all other non-coding RNA in fasta format (Required)
  -mrf,   --mrna               mRNA file in fasta format (Required)
  -spnf,  --spike-in           user defined custom spike-in file in fasta format (Optional)
  -agff,  --ann-gff            miRNA annotation gff file (Required)
  -ngrs,  --gen-repeats        the genome repeats file with .gtf extension (Optional: output however enables novel miRNA prediction in the miRge pipeline)
  -db,    --mir-DB             name of the database to be used (Options: miRBase, miRGeneDB) (Required)
  -on,    --organism-name      name of the organism [Note: name should be one word and use "_" as separator if necessary] (Required)
  -cpu,   --threads            the number of processors to use for trimming, qc, and alignment (Default: 1)
  -pbwt,  --bowtie-path        path to system's directory containing bowtie binary (Required if bowtie is not in the environment path)
  
```

## File format options
Having the right file format is important before making miRge libraries. When dealing with new species which is not available in the set of miRge3.0 libraries, it is important to prioritize what is essential. In other words, general format options is straight forward and faster to build libraries. Novel miRNAs runs scipy cKDTree during library preparation and it consumes lot of computational resources and time. 

#### General format options ####

##### Example usage #####
Example command usage:
```
miRge-build -g genome.fasta -mmf nematode_mature_miRBase.fa -hmf hairpin_miR.fa -mtf mature_trna.fasta -ptf pre_trna.fasta -snorf snorna.fasta -rrf rrna.fasta -ncof ncrna_other.fasta -mrf mrna.fasta -agff nematode_miRBase.gff3 -db miRBase -on roundworm -cpu 10  -ngrs WBcel235_genome_repeats.GTF
```
Output command line:
```
bowtie version: 1.2.3

Library indexing in progress...

Building the kdTree of roundworm_genome_repeats.GTF....

Building the kdTree of roundworm_genome_repeats.GTFtakes: 1.4s
Transforming roundworm_genome.fa takes: 0.9s

miRge-build is complete in 108.2122 second(s)
```
Output directory structure: 
```
DB = '--mir-DB'; name of the database used (miRBase or miRGeneDB)

Organism
├── annotation.Libs
│   ├── organism_DB.gff3
│   ├── organism_genome_repeats.pckl (if `-ngrs` is opted)
│   ├── organism_miRNAs_in_repetitive_element_DB.csv (if `-ngrs` is opted)
│   └── organism_merges_DB.csv
├── fasta.Libs
│   ├── organism_genome.pckl (if `-ngrs` is opted) 
│   └── organism_merges_DB.fa
└── index.Libs
    ├── organism_genome*.ebwt
    ├── organism_hairpin_DB*.ebwt
    ├── organism_mirna_DB*.ebwt
    ├── organism_mature_trna*.ebwt
    ├── organism_pre_trna*.ebwt
    ├── organism_rrna*.ebwt
    ├── organism_snorna*.ebwt
    ├── organism_mrna*.ebwt
    ├── organism_ncrna_others*.ebwt
    ├── organism_mature_trna*.ebwt
    └── organism_spike-in*.ebwt (Optional)
```

##### Name of the database #####
miRge uses miRBase or miRGeneDB as the reference database.
 So, it is mandatory to use `-db` option to either `-db miRBase` or `-db miRGeneDB`. Reference miRNA database `-db` and annotation GFF `-agff` files can be found at [miRGeneDB](https://mirgenedb.org/) and [miRBase](http://www.mirbase.org/). 

##### Name of the organism #####
miRge-build creats and store all the libraries under the folder which is named after the organism. It is recommended to use a simple name and avoid any special character (use "_" if the name needs to be seperated by space). Example: ` -on human `; ` -on horse `; `-on donkey`; ` -on my_database ` etc.
    

##### Fasta format #####
Parameters with `-g`, `-mmf`, `-hmf`, `-mtf`, `-ptf`, `-snorf`, `-mrf`, `-spnf` should be in FASTA format as shown below. `-spnf ` or --spike-in is optional if the user is interested in adding additional database with spike-in reads. 

*FASTA Format:*

```
>Header or Identifier
NUCLEOTIDE SEQUENCE 
Ex:
  >hsa-let-7a-5p
  TGAGGTAGTAGGTTGTATAGTT
```

**NOTE:**
```
The Header ID of hairpin miRNA fasta should match mature miRNA fasta file. This is required for accurate isomiR annotation. 
miRge-build fetches 2bp upstream to 5p and 6bp downstream to 3p mature miRNA from the hairpin miRNA based on the matching ID. 
Exception: If the mature miRNA name contains XXXX-5p, XXXX-3p, XXXX-[5|3]p*,  XXXX_5p or XXXX_3p where XXXX matches the hairpin miRNA ID. 
Also, if this is not possible, miRge will not throw any errors, however, proceed with the user provided files.  
```

#### Novel miRNA options ####
Novel miRNA prediction requires genome file (which is provided in the general format) and genome repeats file in GTF format, `-ngrs`. As mentioned previously, novel miRNA analysis consumes lot of computational resources and time.


#### Custom annotation options ####
This is **optional**, that two files under the `annotation.Libs` subdirectory requires users input manually. 

##### \_merges\_ #####
This file structured as `organism_merges_database.csv` file allows users to define miRNA family for miRNA with similar sequence. 
Below is the guide to format the file, where `hsa-miR-376b-5p/376c-5p` is the name of the miRNA family seperated by `/` followed by the family members such as `hsa-miR-376b-5p` and `hsa-miR-376c-5p` all seperated by `,`. Next such miRNA family should begin in a new line. Here, four such example is shown below. 

```
hsa-miR-376b-5p/376c-5p,hsa-miR-376b-5p,hsa-miR-376c-5p
hsa-miR-518c-3p/518f-3p,hsa-miR-518c-3p,hsa-miR-518f-3p
hsa-miR-642a-3p/642b-3p,hsa-miR-642a-3p,hsa-miR-642b-3p
hsa-miR-3155a-3p/3155b,hsa-miR-3155a-3p,hsa-miR-3155b
hsa-miR-3689b-3p/3689c,hsa-miR-3689b-3p,hsa-miR-3689c
```

##### \_miRNAs\_in\_repetitive\_element\_ #####

This file structured as `organism_miRNAs_in_repetitive_element_database.csv` file allows users to define miRNA that overlap with repeate elements in the genome. This eliminates miRNA reads to be identified as novel miRNAs or identifying one as A-to-I editing, both of which might be misleading. 

Below is the guide to format the file, where miRNA name which overlaps with repeate elements are seperated by `,`. The `gene_id` and `transcript_id` of a repeate element should follow the miRNA name. See the example below: 

```
hsa-miR-28-5p,gene_id "L2c"; transcript_id "L2c_dup8856";
hsa-miR-28-3p,gene_id "L2c"; transcript_id "L2c_dup8856";
hsa-miR-95-5p,gene_id "L2c"; transcript_id "L2c_dup382";
hsa-miR-95-3p,gene_id "L2b"; transcript_id "L2b_dup437";
hsa-miR-181c-5p,gene_id "MamRTE1"; transcript_id "MamRTE1_dup11";
```

#### Resources ####
* The genome repeats can be obtained from [UCSC](https://genome-euro.ucsc.edu/cgi-bin/hgTables)
* The database sequences for other small RNA could be obtained from [UCSC](https://genome-euro.ucsc.edu/cgi-bin/hgTables) or [Ensembl](http://uswest.ensembl.org/Homo_sapiens/Info/Index)
* [Bowtie-v1.2.3](https://sourceforge.net/projects/bowtie-bio/files/bowtie/1.2.3) - please pick one based on your OS.

