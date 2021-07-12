"""
ID: aarush31
LANG: PYTHON3
TASK: friday
"""

fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')


start_yr = 1900
thing = fin.readlines()
end_yr = start_yr + int(thing[0]) - 1

yrs = []

for yr in range(start_yr, end_yr + 1):
	yrs.append(yr)

months = {'jan':31, 'feb':28, 'mar':31, 'apr':30, 'may':31, 'jun':30, 'jul':31, 'aug':31, 'sep':30, 'oct':31, 'nov':30, 'dec':31}
counts = {'mon':0, 'tues':0, 'wed':0, 'thurs':0, 'fri':0, 'sat':0, 'sun':0}
mos = list(counts.keys())

def leap_year(yr):
	if yr % 100 == 0:
		if yr % 400 == 0:
			return True
		else:
			return False
	elif yr % 4 == 0:
		return True
	else:
		return False

def calc_day(lst):
	curr_day = 0
	for yr in lst:
		print(yr)
		if leap_year(yr):
			months['feb'] = 29
		else:
			months['feb'] = 28
		for month,total in months.items():
			curr_day += 13
			curr_day = curr_day % 7
			if curr_day == 0:
				curr_day = 6
			else:
				curr_day -= 1
			day = mos[curr_day]
			if curr_day == 6:
				curr_day = 0
			else:
				curr_day += 1
			print(day)
			counts[day] += 1
			curr_day += total - 13

calc_day(yrs)

final_list = [counts['sat'], counts['sun'], counts['mon'], counts['tues'], counts['wed'], counts['thurs'], counts['fri']]
fout.write(str(final_list[0]) + " " + str(final_list[1]) + " " + str(final_list[2]) + " " + str(final_list[3]) + " " + str(final_list[4]) + " " + str(final_list[5]) + " " + str(final_list[6]) + "\n")
fout.close()
fin.close()
