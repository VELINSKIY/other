num1 = float(input("Number one pls "))
operator = input("Operator? ")
num2 = float(input("Number two pls "))

if operator == '+':
    addition = round((num1 + num2), 3)
    print(('{} + {} = '.format(num1, num2)), addition)
elif operator == '-':
    subtraction = round((num1 - num2), 3)
    print(('{} - {} = '.format(num1, num2)), subtraction)
elif operator == '*':
    multiplication = round((num1 * num2), 3)
    print(('{} * {} = '.format(num1, num2)), multiplication)
elif operator == '/':
    division = round((num1 / num2), 3)
    print(('{} / {} = '.format(num1, num2)), division)
else:
    print('Wront operator')