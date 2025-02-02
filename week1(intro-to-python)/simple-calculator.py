#simple calculator program
print("hello !\n")
print("welcome to my simple calculator program !\n")
print("you can perform the following operations: \n")
print("1. addition \n")
print("2. subtraction \n")
print("3. multiplication \n")
print("4. division \n")
print("5. modulous \n")
print("6. exponentiation \n")

#asking user for input

choice = input("enter your choice (1/2/3/4): ")
if choice=='1':#addition
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    print("result is: ", num1 + num2)
elif choice=='2':#subtraction
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    print("result is: ", num1 - num2)
elif choice=='3':#ultiplication
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    print("result is: ", num1 * num2)
elif choice=='4':#division
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    if num2 != 0:
       print("result is: ", num1 / num2)
    else:
       print("error! division by zero is not allowed")
elif choice=='5':#omdulous
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    if num2 != 0:
       print("result is: ", num1 % num2)
    else:
       print("error! division by zero is not allowed, so modulous is not possible ")
elif choice=='6':#exponentiation
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    print("result is: ", num1 ** num2)

print("thank you for using my simple calculator :) \n")



