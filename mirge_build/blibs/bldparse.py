import os 
import sys
import argparse
import subprocess

def bldParseArg():
    version = '3.0'
    parser = argparse.ArgumentParser(description='miRge-build (Enables building small-RNA libraries for organism of choice to use in miRge3.0 pipeline)',usage='miRge-build [options]',formatter_class=argparse.RawTextHelpFormatter,)
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    parser.add_argument('--version', action='version', version='%s'%(version))
    group = parser.add_argument_group("Options",description='''-g,     --genome             genome file in fasta format (.fna, .fasta or .fa) (Required)
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
-ngrs,  --gen-repeats        the genome repeats file with .gtf extension (Optional: output however enables novel miRNA prediction in the miRge3.0 pipeline) 
-db,    --mir-DB             name of the database to be used (Options: miRBase, miRGeneDB) (Required)
-on,    --organism-name      name of the organism [Note: name should be one word and use "_" as separator if necessary] (Required)
-cpu,   --threads            the number of processors to use for trimming, qc, and alignment (Default: 1)
-pbwt,  --bowtie-path        path to system's directory containing bowtie binary (Required if bowtie is not in the environment path) 
''')
    group.add_argument('-g',  '--genome', required=True, help=argparse.SUPPRESS)
    group.add_argument('-mmf','--mature-mir', required=True, help=argparse.SUPPRESS)
    group.add_argument('-hmf','--hpin-mir', required=True, help=argparse.SUPPRESS)
    group.add_argument('-mtf','--mature-trna', required=True, help=argparse.SUPPRESS)
    group.add_argument('-ptf','--pre-trna', required=True, help=argparse.SUPPRESS)
    group.add_argument('-snorf','--snorna', required=True, help=argparse.SUPPRESS)
    group.add_argument('-rrf','--rrna', required=True, help=argparse.SUPPRESS)
    group.add_argument('-ncof','--ncrna-other', required=True, help=argparse.SUPPRESS)
    group.add_argument('-mrf','--mrna', required=True, help=argparse.SUPPRESS)
    group.add_argument('-spnf','--spike-in', help=argparse.SUPPRESS)
    group.add_argument('-agff','--ann-gff', required=True, help=argparse.SUPPRESS)
    group.add_argument('-ngrs','--gen-repeats', help=argparse.SUPPRESS)
    group.add_argument('-db', '--mir-DB', default='miRBase', required=True, help=argparse.SUPPRESS)
    group.add_argument('-on','--organism-name', required=True, help=argparse.SUPPRESS)
    group.add_argument('-cpu', '--threads', type=int, default='0', help=argparse.SUPPRESS)
    group.add_argument('-pbwt', "--bowtie-path", default=False, help=argparse.SUPPRESS)
    return parser.parse_args()

