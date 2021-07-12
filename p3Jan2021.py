n = int(input())
a = str(input())
a = a.split()
a = [int(x) for x in a]
a.sort()
b = str(input())
b = b.split()
b = [int(x) for x in b]
b.sort()

poss = []
for horse in range(len(a)):
	curr_poss = []
	for stall in range(len(b)):
		if a[horse] <= b[stall]:
			curr_poss.append(stall)
	poss.append(curr_poss)

poss.reverse()
total_poss = 1
for curr_horse in range(len(poss)):
	total_poss *= len(poss[curr_horse])
	for next_horse in range(curr_horse, len(poss)):
		if len(poss[curr_horse]) == 0:
			total_poss = 1
			break
		poss[next_horse].remove(poss[curr_horse][-1])

print(total_poss)

