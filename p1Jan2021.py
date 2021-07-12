cowphabet = str(input())
john = str(input())

res_string = ""

curr_ind = 0
counter = 0

while True:
	for let in cowphabet:
		if curr_ind == len(john):
			break
		if let == john[curr_ind]:
			res_string += let
			curr_ind += 1
		else:
			continue
	counter += 1
	if res_string == john:
		break

print(counter)

