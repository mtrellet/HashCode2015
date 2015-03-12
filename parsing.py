import sys


if len(sys.argv) != 2:
	print sys.argv[0]," inputfile.in"
	exit(0)

fich = open(sys.argv[1],"r")
lines = fich.readlines()
fich.close()

tmp = lines[0].split()
nbranges = int(tmp[0])
nbempla = int(tmp[1])
nbindispo = int(tmp[2])
nbgroupes = int(tmp[3])
nbservers = int(tmp[4])

indispos = []
for i in range(1,nbindispo):
	indispos.append([int(lines[i].split()[0]),int(lines[i].split()[1])])

serveurs = []

for i in range(nbindispo+1,nbindispo+1+nbservers):
	serveurs.append([int(lines[i].split()[0]),int(lines[i].split()[1])])

