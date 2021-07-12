"""
ID: aarush31
LANG: PYTHON3
TASK: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

gifts = {}
lst = list(fin.readlines())
l = [i.strip() for i in lst]

for p in range(1, int(l[0])+1):
	gifts.update({l[p]: 0})


curr = 1 + int(l[0])
for val in range(int(l[0])):
	if (curr + 1 == len(l)):
		break
	temp = l[curr + 1].split(' ')
	tot = int(temp[0])
	ppl = int(temp[1])
	if (tot == 0):
		curr = curr + ppl + 2
		continue
	add = tot // ppl
	for pers in range(curr + 2, curr + 2 + ppl):
		gifts[l[pers]] += add
	gifts[l[curr]] += tot % ppl
	gifts[l[curr]] -= tot
	curr = curr + ppl +2
	print(gifts)

seq = []

for key,value in gifts.items():
	seq.append(str(key) + " " + str(value) + "\n")

fout = open ('gift1.out', 'w')
fout.writelines(seq)
fout.close()
fin.close()