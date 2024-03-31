# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
num = int(input("Enter first number"))
check = int(input("Enter second number"))

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)
