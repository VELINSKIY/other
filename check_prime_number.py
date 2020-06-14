number = int(input('Please enter a number '))

flag = 1
for i in range(2, number):
#check if number is exactly divisible by any number from 2 to number - 1
    if (number % i) == 0:
        print(number, 'is not a prime number')
        print(i, 'times', number // i, 'is', number)
        flag = 0
        break
if flag == 1:
    print(number, "is a prime number")