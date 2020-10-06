import os
from pathlib import Path
import sys
from scipy.spatial import cKDTree
import time
import pickle
from Bio import SeqIO
import re
import subprocess

def miRNA_miRge_format(hpin, mir):
    start, end = re.search(mir, hpin).span()
    prefix = hpin[:start][-2:]
    suffix = hpin[end:][:6]
    new_mir = prefix + mir + suffix
    return new_mir

def build_index(args, bwtCommand, infile, outfile):
    bwtBuildExec = str(bwtCommand) +" -f "+ str(infile) + " " + str(outfile) + " --threads " + str(args.threads)
    subprocess.run(str(bwtBuildExec), shell=True, check=True, stdout=subprocess.PIPE, text=True, stderr=subprocess.PIPE, universal_newlines=True)

def bld_bowtie_index(args, index_path, bwtCommand):
    organism = str(args.organism_name)
    dbname = str(args.mir_DB)
    hpin_mir_name ={}
    for record in SeqIO.parse(str(Path(args.hpin_mir).resolve()), "fasta"):
        chr, seq = record.id, str(record.seq)
        hpin_mir_name[chr] = seq
        #hpin_mir_name.update({chr:seq})

    mirFa = Path(index_path)/(organism + "_mirna_" + dbname + ".fa")
    fmir = open(str(mirFa), "a+")
    for mirnas in SeqIO.parse(str(Path(args.mature_mir).resolve()), "fasta"):
        name, sequence = mirnas.id, str(mirnas.seq)
        #.tostring()
        b = re.sub('[-|_]5p.*','', name)
        c = re.sub('[-|_]3p.*','', name)
        newSeq= ""
        if name in hpin_mir_name.keys():
            newSeq = miRNA_miRge_format(hpin_mir_name[name], sequence)
        elif b in hpin_mir_name.keys():
            newSeq = miRNA_miRge_format(hpin_mir_name[b], sequence)
        elif c in hpin_mir_name.keys(): 
            newSeq = miRNA_miRge_format(hpin_mir_name[c], sequence) 
        else:
            newSeq = sequence
        fmir.write(">" + name + "\n" + newSeq + "\n")
    fmir.close()

    hp_nme = '_hairpin_' + dbname
    mature_nme = '_mirna_' + dbname

    libList = [hp_nme, mature_nme, '_genome', '_mature_trna', '_mrna', '_ncrna_others', '_pre_trna', '_rrna', '_snorna']
    argList = [ str(Path(args.hpin_mir).resolve()), str(mirFa), str(Path(args.genome).resolve()), str(Path(args.mature_trna).resolve()), str(Path(args.mrna).resolve()), str(Path(args.ncrna_other).resolve()), str(Path(args.pre_trna).resolve()), str(Path(args.rrna).resolve()), str(Path(args.snorna).resolve())]

    for num, items in enumerate(libList):
        infile = argList[num]
        out = organism + items
        outfile = Path(index_path)/out
        build_index(args, bwtCommand, infile, outfile)

    if args.spike_in:
        outfile = organism + "_spike-in"
        build_index(args, bwtCommand, str(Path(args.spike_in).resolve()), outfile)
    
    os.system('rm %s'%(mirFa))

