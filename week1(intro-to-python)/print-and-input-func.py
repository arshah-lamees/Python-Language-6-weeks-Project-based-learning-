# demonstrate the print functionality--------------

# print message
print("print simple message--------")
print("Hello, World!")

#print using variables
print("print using variables-------------")
name = "arshah"
age = 20
print("My name is", name, "and I am", age, "years old.") #notation 1
print(f"my name is {name} and I am {age} years old")#notation 2

#print using list
print("print using list-------------")
fruits = ["apple", "banana", "cherry"]
print("print the first element of the list:",fruits[0]) 
print(f"print entire list: {fruits}") 


#print multiple values
print("print multiple values-----------")
print(1,2,3,4,5) #notation 1
print("1 2 3 4 5") #notation 2
print("1", "2", "3", "4", "5") #notation 3
print("This", "is", "a", "using","sep","and","end", sep="-", end=".\n")


# demonstrate the input functionality-------------

# input message
print("input functionality--------------")
name = input("Enter your name: ")
print(f"My name is {name}. ") 

# input functionality with default value
print("input functionality with default value--------------")
age = input("Enter your age (default is 20): ")
if age == "":
    age = 20
    print(f"I am {age} years old.") 

# input functionality with multiple inputs
print("input functionality with multiple inputs------------")
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"My name is {name} and I am {age} years old") 





