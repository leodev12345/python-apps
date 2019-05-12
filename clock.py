import datetime
time = datetime.datetime.now()
print("Current date:")
print(time.strftime("%d-%m-%Y"))
print("Current time:")
print(time.strftime("%H : %M"))
h = input("Date or time not correct? Try setting new date or time <Y/N> ")
if h=="Y":
	d = int(input("Type date: "))
	m = int(input("Type month: "))
	y = int(input("Type year: "))
	hour = int(input("Type hours: "))
	minute = int(input("Type minutes: "))
	print("Date set to:")
	print(d,"-",m,"-",y)
	print("Time set to:")
	print(hour,":",minute)
elif h=="N":
	print("Time is ok")
else:
	print("Invalid input")
	h = input("Date ro time not correct? Try setting new date or time <Y/N> ")
