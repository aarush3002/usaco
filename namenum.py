"""
ID: aarush31
LANG: PYTHON3
TASK: namenum
"""

fin = open('namenum.in', 'r')
fout = open('namenum.out', 'w')
dictin = open('dict.txt', 'r')

namedict = dictin.readlines()
names = []
for x in namedict:
    names.append(str(x.strip()))

numdict = {2:['A','B','C'], 3:['D','E','F'], 4:['G','H','I'], 5:['J','K','L'], 6:['M','N','O'], 7:['P','R','S'], 8:['T','U','V'], 9:['W','X','Y']}

serial_num = int(fin.readlines()[0].strip())

valid_names = []

for n in namedict:
	n=n.strip()
	if len(n) != len(str(serial_num)):
		continue
	else:
		my_flag = True
		for ind in range(len(n)):
			if n[ind] in numdict[int(str(serial_num)[ind])]:
				continue
			else:
				my_flag=False
		if my_flag==True:
			valid_names.append(n)

print(valid_names)
'''
for x in poss_names:
	if x in names:
		valid_names.append(x)
'''

if len(valid_names) == 0:
	fout.write("NONE" + "\n")
else:
	for n in valid_names:
		fout.write(n + "\n")

fin.close()
fout.close()