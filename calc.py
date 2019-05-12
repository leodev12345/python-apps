o = int(input("Select operation: 1=*, 2=/, 3=+, 4=- "))
a = int(input("Type first number: "))
b = int(input("Type second number: "))
if o>4 or o<1:
	print("Invalid input!")
if o==1:
	print(a*b)
elif o==2:
	print(a//b)
elif o==3:
	print(a+b)
elif o==4:
	print(a-b)
