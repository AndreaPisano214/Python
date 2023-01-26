def get_seq(fastafile):
 f = open(fastafile)
 lines = f.readlines()
 f.close()
 lines = [row.strip() for row in lines]
 lines = [row.replace( '\n','') for row in lines if not row.startswith( '>')]
 return ''.join(lines)
print(get_seq('fastafile.fasta' ))