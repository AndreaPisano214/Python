seq = get.seq('mitochondrion.fasta')  #problemi con underscore
import zlib
zseq = zlib.compress(seq)
len(seq)