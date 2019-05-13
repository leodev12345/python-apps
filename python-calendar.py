import calendar
import datetime
now = datetime.datetime.now()
m = int(now.strftime("%m"))
y = int(now.strftime("%Y"))
cal = calendar.month(y,m)
print(cal)
print("Commands:")
print("!SetMonth = set month to be displayed")
print("!SetYear =set whole year calendar to be printed")
print("!PrintCurYear = print current year calendar")
print("!PrintCurMonth = print current month")
print("!Quit = quit program")
cmd = input("Type command: ")
if cmd=="!SetMonth":
	m = int(input("Month to be displayed: "))
	print(calendar.month(y,m))
elif cmd=="!SetYear":
	y=int(input("Year to be displayed: "))
	print(calendar.calendar(y))
elif cmd=="!PrintCurYear":
	print(calendar.calendar(y))
elif cmd=="!PrintCurMonth":
	print(cal)
elif cmd=="!Quit":
	print("")
else:
	print("Invalid command!")
