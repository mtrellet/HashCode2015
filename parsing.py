import sys
import random

if len(sys.argv) != 2:
	print sys.argv[0]," inputfile.in"
	exit(0)

def get_min_capacity(matrice,serveurs,listgroups,nbgroupes):
	leaveoneoutmin = []
	for h in xrange(len(matrice)):
		minlist = [0 for i in xrange(nbgroupes)]
		roam_serveurs = [False for i in xrange(len(serveurs))]
		for i in xrange(len(matrice)):
			if i != h:
				for j in xrange(len(matrice[i])):
					if matrice[i][j]!= False and matrice[i][j] != True:
						myid = matrice[i][j]
						if roam_serveurs[myid]==False:
							numgroup = listgroups[myid]
							mycapa = serveurs[myid][1]
							minlist[numgroup]+=mycapa
							roam_serveurs[myid] = True
		leaveoneoutmin.append(min(minlist))
	return min(leaveoneoutmin)

def dumpfile(filename,matrice,serveurs,listgroups):
	fich = open(filename,"w")
	roam_serveurs = [False for i in xrange(len(serveurs))]
	for i in xrange(len(matrice)):
		for j in xrange(len(matrice[i])):
			if matrice[i][j]!= False and matrice[i][j] != True:
				myid = matrice[i][j]
				if roam_serveurs[myid]==False:
					roam_serveurs[myid] = True
					numgroup = listgroups[myid]
					fich.write(str(myid)+" "+str(i)+" "+str(j)+" "+str(numgroup)+"\n")
	fich.close()

filename = "currentresult.txt"
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
for i in xrange(1,nbindispo+1):
	indispos.append([int(lines[i].split()[0]),int(lines[i].split()[1])])

serveurs = []

for i in xrange(nbindispo+1,nbindispo+1+nbservers):
	serveurs.append([int(lines[i].split()[0]),int(lines[i].split()[1])])


matrice = []
for i in xrange(nbranges):
	matrice.append([])
	for j in xrange(nbempla):
		matrice[i].append(True)

for i in xrange(nbindispo):
	serv = indispos[i]
	matrice[serv[0]][serv[1]] = False



finalmin = 0

while True:
	#rdserveurs = serveurs[:]
	rdserveurs = range(len(serveurs))
	random.shuffle(rdserveurs)

	curid = 0
	for ran in xrange(nbranges):
		if curid == nbservers:
			break
		curposempla = 0
		while curposempla < nbempla and curid<nbservers:
			if matrice[ran][curposempla]!=False:
				if curposempla + serveurs[rdserveurs[curid]][0] < nbempla:
					flag = True
					for i in xrange(serveurs[rdserveurs[curid]][0]):
						if matrice[ran][curposempla+i] == False:
							flag = False
					if flag:
						for i in xrange(serveurs[rdserveurs[curid]][0]):
							matrice[ran][curposempla+i] = rdserveurs[curid]
						curposempla += serveurs[rdserveurs[curid]][0]
						curid+=1
					else:
						curposempla+=1
				else:
					break
			else:
				curposempla+=1
	print "Debut"
	for i in xrange(100):
		listgroups =  []
		for i in range(nbservers):
			listgroups.append(random.randint(0,nbgroupes-1))
		curmin = get_min_capacity(matrice,serveurs,listgroups,nbgroupes)
		if curmin > finalmin:
			finalmin = curmin
			print "Current result = ",curmin
			dumpfile(filename,matrice,rdserveurs,listgroups)
	print "Fin"

