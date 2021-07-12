num_cows = int(input())
breed_IDs = str(input())

breed_list = breed_IDs.split()
breed_list = [int(x) for x in breed_list]
breed_list.sort()
evens = []
odds = []

for num in breed_list:
	if num % 2 == 0:
		evens.append(num)
	else:
		odds.append(num)
#print(evens)
#print(odds)
max_groups = 0
if len(odds) == len(evens):
	max_groups = len(odds) * 2
if len(odds) > len(evens):
	max_groups = len(evens) * 2 + int((len(odds) - len(evens))/2)
	if len(evens) % 2 == 1:
		max_groups += 1
if len(odds) < len(evens):
	max_groups = len(odds) * 2 + 1
if len(evens) == 0 and len(odds) <= 1:
	max_groups = 0

print(max_groups)

