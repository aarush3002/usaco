"""
ID: aarush31
LANG: PYTHON3
TASK: transform
"""

fin = open('transform.in', 'r')
fout = open('transform.out', 'w')

bruh = fin.readlines()

new = []

for row in bruh:
    row = row.strip()
    temp = []
    for char in row:
        temp.append(char)
    new.append(temp)

dim = new.pop(0)
dim = int(''.join(dim))

print(dim)

first = new[0:dim]
last = new[dim::]

answer = 7

def generate():
    res = []
    for row in range(dim):
        col = []
        for item in range(dim):
            col.append('')
        res.append(col)
    return res

def ninety(lst):
    res = generate()
    for row in range(len(lst)):
        for item in range(len(lst[row])):
            r = item
            c = len(lst) - row - 1
            res[r][c] = lst[row][item]
    return res

def one_eighty(lst):
    res = generate()
    for row in range(len(lst)):
        for item in range(len(lst[row])):
            r = len(lst) - 1 - row
            c = len(lst) - 1 - item
            res[r][c] = lst[row][item]
    return res

def two_seventy(lst):
    res = generate()
    for row in range(len(lst)):
        for item in range(len(lst[row])):
            r = len(lst) - 1 - item
            c = row
            res[r][c] = lst[row][item]
    return res

def reflection(lst):
    res = generate()
    for row in range(len(lst)):
        for item in range(len(lst[row])):
            r = row
            c = len(lst) - 1 - item
            res[r][c] = lst[row][item]
    return res

def combination(lst):
    ref = reflection(lst)
    rezzes = [ninety(ref), one_eighty(ref), two_seventy(ref)]
    for x in rezzes:
        if x == last:
            return True
    return False

def no_change(lst):
    if lst == last:
        return True
    else:
        return False

all_transform = [ninety(first) == last, one_eighty(first) == last, two_seventy(first) == last, reflection(first) == last, combination(first), no_change(first)]
print(all_transform)

for trans in range(len(all_transform)):
    if all_transform[trans]:
        answer = trans + 1
        break

fout.write(str(answer) + "\n")
fin.close()
fout.close()