import os
import sys
from scipy.spatial import cKDTree
import time
import pickle
from Bio import SeqIO

def main(arg = sys.argv):
    if len(arg) != 4:
        print('usage:')
        print('miRge_pckls_build.py species PathOfGRCh38_genome_repeats.GTF PathOfHuman_genome.fa', file=sys.stderr)
        sys.exit(1)
    else:
        species = arg[1]
        PathOfGRCh38_genome_repeats = arg[2]
        PathOfHuman_genome = arg[3]
        time1 = time.time()
        os.system('sort -k1,1 -k4n,4 %s > %s'%(PathOfGRCh38_genome_repeats, os.path.splitext(PathOfGRCh38_genome_repeats)[0]+'_sorted.GTF'))
        repEleChrCoordinateDic ={}
        with open(os.path.splitext(PathOfGRCh38_genome_repeats)[0]+'_sorted.GTF',"r") as inf1:
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
        f = open(os.path.splitext(PathOfGRCh38_genome_repeats)[0]+'_sorted.pckl',"wb")
        pickle.dump(repEleChrCoordinateDic,f)
        f.close()
        time2 = time.time()
        os.system('rm %s'%(os.path.splitext(PathOfGRCh38_genome_repeats)[0]+'_sorted.pckl'))
        print("Building the kdTree of ***_genome_repeats. GTF takes: %.1fs"%(time2-time1))

        time3 = time.time()
        chrSeqDic ={}
        for record in SeqIO.parse(PathOfHuman_genome, "fasta"):
            chr, seq = record.id, str(record.seq)
            chrSeqDic.update({chr:seq})
        f = open(os.path.join(os.path.split(PathOfHuman_genome)[0], species+'_genome.pckl'), "wb")
        pickle.dump(chrSeqDic,f)
        f.close()
        time6 = time.time()
        print("Transforming %s_genome.fa takes: %.1fs"%(species, time6-time3))

if __name__ == '__main__':
    main()
