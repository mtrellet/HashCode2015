import sys
import random
import operator

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
	to_write = ["x" for i in xrange(len(serveurs))]
	for i in xrange(len(matrice)):
		for j in xrange(len(matrice[i])):
			if matrice[i][j]!= False and matrice[i][j] != True:
				myid = matrice[i][j]
				if roam_serveurs[myid]==False:
					roam_serveurs[myid] = True
					numgroup = listgroups[myid]
					#fich.write(str(myid)+" "+str(i)+" "+str(j)+" "+str(numgroup)+"\n")
					to_write[myid] = (i,j,numgroup)
	for i in to_write:
		if i =="x":
			fich.write("x\n")
		else:
			fich.write(str(i[0])+" "+str(i[1])+" "+str(i[2])+"\n")
	fich.close()

filename = "currentresult_intel.txt"
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

idserv = 0
for i in xrange(nbindispo+1,nbindispo+1+nbservers):
	serveurs.append([int(lines[i].split()[0]),int(lines[i].split()[1]),idserv])
	idserv+=1



matrice = []
for i in xrange(nbranges):
	matrice.append([])
	for j in xrange(nbempla):
		matrice[i].append(True)

for i in xrange(nbindispo):
	serv = indispos[i]
	matrice[serv[0]][serv[1]] = False

serveurs.sort(reverse=True)

# curid = 0
# flagstop = False
# for col in xrange(nbempla):
# 	if flagstop:
# 		break
# 	currangempla = 0
# 	while currangempla < nbranges and curid<nbservers:
# 		if curid == nbservers:
# 			flagstop = True
# 			break
# 		flag = True
# 		if matrice[currangempla][col]!=False:
# 			monserv = serveurs[curid]
# 			if currangempla + monserv[0] <= nbranges:
# 				flag = True
# 				for i in xrange(monserv[0]):
# 						if matrice[i+currangempla][col] == False:
# 							flag = False
# 							currangempla+=1
# 							break
# 				if flag:
# 					for i in xrange(monserv[0]):
# 						matrice[i+currangempla][col] = serveurs[curid][2]
# 					currangempla += monserv[0]
# 					curid+=1
# 			else:
# 				break
# 		else:
# 			currangempla+=1


listidserveurs = []
curid = 0
flagstop = False
for lig in xrange(nbranges):
	if flagstop:
		break
	curempla = 0
	while curempla < nbempla and curid<nbservers:
		if curid == nbservers:
			flagstop = True
			break
		flag = True
		if matrice[lig][curempla]!=False:
			monserv = serveurs[curid]
			if curempla + monserv[0] <= nbempla:
				flag = True
				for i in xrange(monserv[0]):
						if matrice[lig][i+curempla] == False:
							flag = False
							curempla+=1
							break
				#TO DO => loop over others !
				if flag:
					for i in xrange(monserv[0]):
						matrice[lig][i+curempla] = serveurs[curid][2]
					curempla += monserv[0]
					curid+=1
					listidserveurs.append(serveurs[curid][2])
			else:
				break
		else:
			curempla+=1

# listgroups = [-1 for i in xrange(nbservers)]
# for i in xrange(len(listidserveurs)):
# 	listgroups[listidserveurs[i]] = i%nbgroupes

mymin = -5
curmin = 0
while 1:
	listgroups =  []
	for i in range(nbservers):
		listgroups.append(random.randint(0,nbgroupes-1))

	curmin = get_min_capacity(matrice,serveurs,listgroups,nbgroupes)
	if curmin > mymin:
			mymin = curmin
			print "Current result = ",curmin
			dumpfile(filename,matrice,serveurs,listgroups)


