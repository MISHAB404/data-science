#Basic Calculator
#Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Create a menu-driven list
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit \n")

i = 0
while i>=0:
    choice = int(input("\nEnter choice (1/2/3/4): "))
    if choice == 1:
        add = num1 + num2
        print("{:.0f} + {:.0f} = {:.0f}".format(num1, num2, add))
    elif choice == 2:
        sub = num1 - num2
        print("{:.0f} - {:.0f} = {:.0f}".format(num1, num2, sub))
    elif choice == 3:
        mul = num1 * num2
        print("{:.0f} * {:.0f} = {:.0f}".format(num1, num2, mul))
    elif choice == 4:
        if num2 == 0:
            print("Invalid (infinity)")
        else:
            div = num1 / num2
            print("{:.0f} / {:.0f} = {:.2f}".format(num1, num2, div))
    elif choice == 5:
        print("Exiting...")
        exit()
    else:
        print("Invalid input")