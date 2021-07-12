"""
ID: aarush31
LANG: PYTHON3
TASK: milk2
"""

fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')

da_data = fin.readlines()
for x in da_data:
    x = x.strip()

num_farm = int(da_data.pop(0))

test = []
for x in da_data:
    test.append(x.split())

for x in test:
    if x == []:
        test.remove(x)

test = [list(map(int,i)) for i in test]
test = sorted(test,key=lambda l:l[0])
org = test
milk_times = []
curr_ind = 0
max_milk = 0
max_idle = 0

def myfunc(curr_ind, test):
    for time in range(curr_ind, len(test)):
        if time > len(test) - 1:
            milk_times.append([start, end])
            break
        start = test[time][0]
        end = test[time][1]
        for other in test[(curr_ind+1)::]:
            other_start = other[0]
            other_end = other[1]
            if end >= other_start and end <= other_end:
                end = other_end
                print("end >= other_start and end <= other_end")
                print([start, end])
                test.remove(other)
            elif end > other_end:
                print("end > other_end")
                test.remove(other)
                continue
            elif end < other_start:
                milk_times.append([start, end])
                print("end < other_start")
                curr_ind += 1
                break
    return milk_times

def calc(milk_times, max_milk, max_idle):
    if len(milk_times) == 1:
        max_milk = milk_times[0][1] - milk_times[0][0]
        max_idle = 0
        print("exited early")
        return [max_milk, max_idle]
            
    for x in range(len(milk_times)):
        if milk_times[x][1] - milk_times[x][0] > max_milk:
            max_milk = milk_times[x][1]-milk_times[x][0]
        if x != len(milk_times) - 1:
            if milk_times[x][1] - milk_times[x+1][0] < max_idle:
                max_idle = milk_times[x][1] - milk_times[x+1][0]
        else:
            break
    return [max_milk, -(max_idle)]

if len(test) == 1:
    milk_times = test
else:
    milk_times = myfunc(curr_ind, test)

print(milk_times)
results = calc(milk_times, max_milk, max_idle)
max_milk = results[0]
max_idle = results[1]

print(max_milk, max_idle)
fout.write(str(max_milk) + " " + str(max_idle) + "\n")

fin.close()
fout.close()