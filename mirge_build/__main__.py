from pathlib import Path
import time
import sys
import os 
import multiprocessing
import re
import subprocess
from mirge_build.blibs.bldparse import bldParseArg
from mirge_build.blibs.miRge_pckls_build import bld_novelmir
from mirge_build.blibs.miRge_bowtie_build import bld_bowtie_index

def main():
    globalstart = time.perf_counter()
    args = bldParseArg()
    # Checking bowtie version #
    bwtCommand = Path(args.bowtie_path)/"bowtie --version" if args.bowtie_path else "bowtie --version"
    bowtie = subprocess.run(str(bwtCommand), shell=True, capture_output=True, text=True)
    bwtver = ["1.2.1", "1.2.2", "1.2.3"]
    if bowtie.returncode==0:
        if not (bowtie.stdout.split('\n')[0].split(' ')[2]) in bwtver:
            print("bowtie error!: incorrect version. Require - bowtie (1.2.1, 1.2.2 or 1.2.3) \nUse argument -pbwt <name of the directory>")
            exit()
        else:
            print("\nbowtie version: "+ str(bowtie.stdout.split('\n')[0].split(' ')[2]))
    else:
        print("bowtie error!: bowtie, command not found \nUse argument -pbwt <name of the directory>")
        outlog.write("bowtie error!: bowtie, command not found \nUse argument -pbwt <name of the directory>\n")
        exit()
   
    organism = str(args.organism_name)
    workDir = Path.cwd()/organism
    Path(workDir).mkdir(exist_ok=True, parents=True)

    ann_path = Path(workDir)/"annotation.Libs"
    fasta_path = Path(workDir)/"fasta.Libs"
    index_path = Path(workDir)/"index.Libs"

    Path(ann_path).mkdir(exist_ok=True, parents=True)
    Path(fasta_path).mkdir(exist_ok=True, parents=True)
    Path(index_path).mkdir(exist_ok=True, parents=True)

    mergesFile = organism + "_merges_" + str(args.mir_DB) + ".csv"
    repeatElementFile = organism + "_miRNAs_in_repetitive_element_" + str(args.mir_DB) + ".csv"
    
    Path(Path(ann_path)/mergesFile).touch()
    Path(Path(ann_path)/repeatElementFile).touch()

    # Bowtie build step 
    print("\nLibrary indexing in progress... \n")
    bwtCommand2 = Path(args.bowtie_path)/"bowtie-build " if args.bowtie_path else "bowtie-build "
    bld_bowtie_index(args, str(index_path), str(bwtCommand2))

    temp_name = organism + "_mature_" + str(args.mir_DB)+".fa"
    temp_name_gff = organism + "_" +str(args.mir_DB)+".gff3"
    dest_mirFasta = str(Path(fasta_path)/temp_name)
    destGFF = str(Path(ann_path)/temp_name_gff)
    os.system('cp %s %s'%(str(Path(args.mature_mir).resolve()), dest_mirFasta))
    os.system('cp %s %s'%(str(Path(args.ann_gff).resolve()), destGFF))

    # Creating files relevant for novel miRNA prediction (Optional)
    if args.gen_repeats:
        bld_novelmir(args, str(ann_path), str(fasta_path))

    globalend_time = time.perf_counter()
    print(f'\nmiRge3.0-build is complete in {round(globalend_time-globalstart, 4)} second(s)\n')


if __name__ == '__main__':
    main()
