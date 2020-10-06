import os
from pathlib import Path
import sys
from scipy.spatial import cKDTree
import time
import pickle
from Bio import SeqIO

def bld_novelmir(args, ann_path, fasta_path):
    PathOfGRCh38_genome_repeats = str(Path(args.gen_repeats).resolve()) # .absolute()  
    PathOfHuman_genome = str(Path(args.genome).resolve())
    species = str(args.organism_name)
    kdkd = "Building the kdTree of " + species + "_genome_repeats.GTF"
    print(kdkd+".... \n")
    sortedRepeats_GTF = str(Path(PathOfGRCh38_genome_repeats).name).split(".")[0] + '_sorted.GTF'
    sortedRepeats_pckl = species +'_genome_repeats.pckl'
    destGTF = Path(ann_path)/sortedRepeats_GTF
    destPckl = Path(ann_path)/sortedRepeats_pckl
    time1 = time.time()
    os.system('sort -k1,1 -k4n,4 %s > %s'%(PathOfGRCh38_genome_repeats, destGTF))
    repEleChrCoordinateDic ={}
    with open(destGTF,"r") as inf1:
        for line1 in inf1:
            content = line1.strip().split("\t")
            chr = content[0]
            repSeqName = content[-1]
            startPos = int(content[3])
            endPos = int(content[4])
            if chr not in repEleChrCoordinateDic.keys():
                repEleChrCoordinateDic.update({chr:[[],[]]})
            else:
                pass
            repEleChrCoordinateDic[chr][0].append((startPos, 0))
            repEleChrCoordinateDic[chr][1].append((startPos, endPos, repSeqName))
    for chr in repEleChrCoordinateDic.keys():
        kd = cKDTree(repEleChrCoordinateDic[chr][0], leafsize=100)
        repEleChrCoordinateDic[chr][0] = []
        repEleChrCoordinateDic[chr][0].append(kd)
    f = open(destPckl,"wb")
    pickle.dump(repEleChrCoordinateDic,f)
    f.close()
    time2 = time.time()
    os.system('rm %s'%(destGTF))
    print(kdkd+"takes: %.1fs"%(time2-time1))

    time3 = time.time()
    chrSeqDic ={}
    for record in SeqIO.parse(PathOfHuman_genome, "fasta"):
        chr, seq = record.id, str(record.seq)
        chrSeqDic.update({chr:seq})
    gen_pcklName = species + "_genome.pckl"
    gen_pckl = Path(fasta_path)/gen_pcklName
    f = open(str(gen_pckl), "wb")
    pickle.dump(chrSeqDic,f)
    f.close()
    time6 = time.time()
    print("Transforming %s_genome.fa takes: %.1fs"%(species, time6-time3))
