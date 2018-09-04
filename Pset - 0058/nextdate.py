import sys
print('Enter day month and year')
s = input()
i = 0
d = ''
m = ''
y = ''
a=s.split()
d = a[0]
m = a[1]
y = a[2]

if d[0] == 0:
	d = d[1:]

if m[0] == 0:
	m = m[1:]

d = int(d)

m = int(m)

y = int(y)

nd = d
nm = m
ny = y

if d > 31 or m > 12: #if a non existent date or month is entered
	print("Wrong date")

elif d > 29 and m == 2:
	print("Wrong date")

else:
	if d == 30 and (m == 4 or m == 6 or m == 9 or m == 11): #if the date is the last day of the 30 day months
		nd = 1
		nm = m + 1
	elif d == 31 and (m==1 or m == 3 or m == 5 or m== 7 or m == 8 or m == 10): #if the date is the last day of the 31 day months
		nd = 1
		nm = m + 1
	elif d == 31 and m == 12: #if the date is the last day of the year
		nd = 1
		nm = 1
		ny = y + 1
	elif d == 28 and m == 2: #if the date is the last day of February
		if y % 4 == 0: #if the year is divisible by 4 (is a leap year)
			if y % 100 == 0: #if the year is a century
				if y % 400 == 0: #if a century is divisible by 400, it is a leap year
					nd = 29 
				else: #if a century isn't divisible by 400, it is not a leap year
					nd = 1 
					nm = 3
			else: #if not a century but divisible by 4, it is a leap year
				nd = 29
				nm = 2
		else: #if not divisible by 4, it is not a leap year
			nd = 1
			nm = 3
	elif d == 29 and m == 2: #if the date is 29th of February
		if y % 4 == 0: #if the year is divisible by 4
			if y % 100 == 0: #if the year is a century
				if y % 400 == 0: #if a century is divisible by 400, it is a leap year
					nd = 1
					nm = 3
				else: #if not, 29th of February didn't occur that year
					print("Wrong date")
					sys.exit()
			else: #if not a century, and divisible by 4, it was a leap year
				nd = 1
				nm = 3
		else: #if not divisible by 4, it wasn't a leap year
			print("Wrong date")
			sys.exit()
	else: #for all other cases, the day increases by just one date
		nd = nd + 1
	print("Next date: "+str(nd)+"/"+str(nm)+"/"+str(ny)) #printing the new date, month and year


