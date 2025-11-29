# Voting, Marriage, Even/Odd, Positive/Negative, Gender checking system
# Created as a combined menu-based program

print("===== MULTI PURPOSE SYSTEM =====")
print("1. Voting System")
print("2. Marriage Eligibility System")
print("3. Even or Odd Check")
print("4. Positive or Negative Check")
print("5. Gender Check")
print("================================")

choice = int(input("Enter your choice (1-5): "))

# ----------------------------------------
# 1. Voting System
# ----------------------------------------
if choice == 1:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are NOT eligible to vote.")

# ----------------------------------------
# 2. Marriage System
# ----------------------------------------
elif choice == 2:
    gender = input("Enter your gender (male/female): ").lower()
    age = int(input("Enter your age: "))

    if gender == "male":
        if age >= 21:
            print("You are eligible for marriage.")
        else:
            print("You are NOT eligible for marriage.")
    elif gender == "female":
        if age >= 18:
            print("You are eligible for marriage.")
        else:
            print("You are NOT eligible for marriage.")
    else:
        print("Invalid gender input!")

# ----------------------------------------
# 3. Even or Odd
# ----------------------------------------
elif choice == 3:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("The number is EVEN.")
    else:
        print("The number is ODD.")

# ----------------------------------------
# 4. Positive or Negative
# ----------------------------------------
elif choice == 4:
    num = int(input("Enter a number: "))
    if num > 0:
        print("The number is POSITIVE.")
    elif num < 0:
        print("The number is NEGATIVE.")
    else:
        print("The number is ZERO.")

# ----------------------------------------
# 5. Gender Check
# ----------------------------------------
elif choice == 5:
    gender = input("Enter gender (male/female): ").lower()
    if gender == "male":
        print("Gender: MALE")
    elif gender == "female":
        print("Gender: FEMALE")
    else:
        print("Invalid gender!")

# ----------------------------------------
# Invalid Option
# ----------------------------------------
else:
    print("Invalid choice! Please enter between 1-5.")
1. Voting
2. Marriage
3. Even/Odd
4. Positive/Negative
5. Gender check
age >= 18 → eligible
num % 2 == 0 → Even
else → Odd
> 0 → Positive
< 0 → Negative
== 0 → Zero

