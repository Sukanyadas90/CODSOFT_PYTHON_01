print("Welcome to the Simple Calculator!")
print("\nSelect an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Exit")
option = int(input("choose an option:"))

if(option in [1,2,3,4]):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
   


    if (option == 1):
        result = a + b
        print(f"\n a + b = {result}")
    elif (option == 2):
        result = a - b
        print(f"\n a - b = {result}")
    elif (option == 3):
        result = a * b
        print(f"\n a * b = {result}")
    elif (option == 4):
        if b != 0:
            result = a / b
            print(f"\n a / b = {result}")
        else:
            print("\nError: Division by zero is not allowed.")
elif (option == 5):
        print("\nExiting the calculator.Thank You!")
        
else:
        print("\nInvalid option choice. Please try again.")

print()
