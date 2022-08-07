#Calculator
def restart():
    import sys

    import os
    os.execv(sys.executable, ['python'] + sys.argv)

def calculator():
    print(" ")
    print("Choose an operation: ")
    print(" ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print(" ")
    
calculator()

operation = input('Your Choice: ')
while operation not in ['1','2','3','4']:
    operation = input('This is an invalid choice. Try again: ')
    
choice = (int(operation))
number1 = input('Your first number: ')
number2 = input('Your second number: ')
num1 = (float(number1))
num2 = (float(number2))

if choice == 1:
    print('', num1, ' + ', num2, ' = ', num1 + num2)

elif choice == 2:
    print('', num1, ' - ', num2, ' = ', num1 - num2)

elif choice == 3:
    print('', num1, ' * ', num2, ' = ', num1 * num2 )

elif choice == 4:
    print('', num1, ' / ', num2, ' = ', num1 / num2 )

print("Would you like to exit the calculator?")
print("Y/N")
print(" ")
choice2 = input('')

if choice2 == 'Yes':
    exit()

elif choice2 == 'No':
    restart()

elif choice2 == 'Y':
    exit()

elif choice2 == 'N':
    restart()

elif choice2 == 'y':
    exit()

elif choice2 == 'n':
    restart()

elif choice2 == 'no':
    restart()

elif choice2 == 'yes':
    exit()
    
else:
    print("Not a valid answer.")
    exit()