# Program to make a simple calculator

#Defining a function for addition.
def add(x, y):
    return x + y

#Defining a function for substraction.
def subtract(x, y):
    return x - y

#Defining a function for multiplication.
def multiply(x, y):
    return x * y

#Defining a function for division.
def divide(x, y):
    return x / y

#Knowing the choice of the user.
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide12")

while True:
    
    choice = input("Enter choice(+/-/*//): ")

    if choice in ('1', '2', '3', '4'):
        #Taking the input from user.
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
