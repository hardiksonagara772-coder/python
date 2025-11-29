print("Enter 1 for even or odd")
print("Enter 2 for Positive or Negative")
print("Enter 3 for voting system  ")
print("Enter 4 for merrige system ")
print("Enter 5 for Gender ")
print("Enter 6 for Invaild ")
option=int(input("Enter option =>"))
if option == 1:
    x = int(input("Enter no =>"))
    if x > 0:
        print("x, is Even")
    else:
        print("x, is Odd")
elif option == 2:
    x = int(input("Enter no =>"))
    if x % 2 == 0:
        print("x, is Positive")
    else:
        print("x, is Nagative")
if option== 3:
	x=int(input("Enter your Age=>"))
	if x>20:
		print("You are eligible for voting ")
	else:
		print("You are not eligible for voting")
if option==4:
	age=int(input("Your Age =>"))
	if age>21:
			print("Your are eligible for Marriage")
	else:
		print("Your are eligible for Marriage")
if option == 5:
    gender = input("Enter Your (M/F) => ").upper()   # keep it as string
    if gender == "M":
        print("You are Male")
    elif gender == "F":
        print("You are Female")
if option==6:
	print("Think you for visiting...")
	#break	