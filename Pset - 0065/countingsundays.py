d = 1
m = 1
y = 1900
i = 1
cnt = 0
flag = False

def checksun(dd,yy):
	print(d)
	print(m)
	print(y)
	if dd == 1 and yy != 1900:
		return True

while(d<=31 and m <= 12 and y<=2000):
	if d == 30 and (m == 4 or m == 6 or m == 9 or m == 11): #if the date is the last day of the 30 day months
		if i == 7:
			flag = checksun(d,y)
			if flag:
				cnt = cnt + 1
			i = 1
		else:
			i = i + 1
		
		d = 1
		m = m + 1
		

	elif d == 31 and (m==1 or m == 3 or m == 5 or m== 7 or m == 8 or m == 10): #if the date is the last day of the 31 day months
		if i == 7:
			flag = checksun(d,y)
			if flag:
				cnt = cnt + 1
			i = 1
		else: 
			i = i + 1
		d = 1
		m = m + 1
		#i = i + 1
		
		

	elif d == 31 and m == 12: #if the date is the last day of the year
		if i == 7:
			flag = checksun(d,y)
			if flag:
				cnt = cnt + 1
			i = 1
		else:
			i = i + 1
		d = 1
		m = 1
		y = y + 1
		#i = i + 1
		
		

	elif d == 28 and m == 2: #if the date is the last day of February
		if y % 4 == 0: #if the year is divisible by 4 (is a leap year)
			if y % 100 == 0: #if the year is a century
				if y % 400 == 0: #if a century is divisible by 400, it is a leap year
					if i == 7:
						flag = checksun(d,y)
						if flag:
							cnt = cnt + 1
						i = 1
					else:
						i = i + 1

					d = 29 
					#i = i + 1
					
				else: #if a century isn't divisible by 400, it is not a leap year
					if i == 7:
						flag = checksun(d,y)
						if flag:
							cnt = cnt + 1
						i = 1
					else: 
						i = i + 1
					d = 1 
					m = 3
					#i = i + 1
					
					
			else: #if not a century but divisible by 4, it is a leap year
				if i == 7:
					flag = checksun(d,y)
					if flag:
						cnt = cnt + 1
					i = 1
				else:
					i = i + 1
				d = 29
				m = 2
				#i = i + 1
				
				
		else: #if not divisible by 4, it is not a leap year
			if i == 7:
				flag = checksun(d,y)
				if flag:
					cnt = cnt + 1
				i = 1
			else:
				i = i + 1
		
			d = 1
			m = 3
			#i = i + 1
			
				

	elif d == 29 and m == 2: #if the date is 29th of February
		if y % 4 == 0: #if the year is divisible by 4
			if y % 100 == 0: #if the year is a century
				if y % 400 == 0: #if a century is divisible by 400, it is a leap year
					if i == 7:
						flag = checksun(d,y)
						if flag:
							cnt = cnt + 1
						i = 1
					else:
						i = i + 1
					d = 1
					m = 3
					#i = i + 1
					

			else: #if not a century, and divisible by 4, it was a leap year
				if i == 7:
					flag = checksun(d,y)
					if flag:
						cnt = cnt + 1
					i = 1
				else:
					i = i + 1
				d = 1
				m = 3
				#i = i + 1
				
	
	else: #for all other cases, the day increases by just one date
		if i == 7:
			flag = checksun(d,y)
			if flag:
				cnt = cnt + 1
			i = 1
		else:
			 i = i + 1
		d = d + 1
		#i = i + 1
		



print(cnt)