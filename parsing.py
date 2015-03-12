import sys
import random

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
for i in range(1,nbindispo+1):
	indispos.append([int(lines[i].split()[0]),int(lines[i].split()[1])])

serveurs = []


mysomme = 0
for i in range(nbindispo+1,nbindispo+1+nbservers):
	serveurs.append([int(lines[i].split()[0]),int(lines[i].split()[1])])
	mysomme += int(lines[i].split()[0])

matrice = []
for i in range(nbranges):
	matrice.append([])
	for j in range(nbempla):
		matrice[i].append([True])


for i in range(nbindispo):
	serv = indispos[i]
	matrice[serv[0]][serv[1]] = False

print matrice





