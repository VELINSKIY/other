'''A leap year is exactly divisible by 4 except
for century years (years ending with 00). The
century year is a leap year only if it is 
perfectly divisible by 400'''

year = int(input('''This simple code checks the desired year whether it\'s a leap year or not. 
Please write the year you wish to check. '''))

if(year % 4) == 0:
    if(year % 100) == 0:
        if(year % 400) == 0:
            print(year, 'is a leap year')
        else:
            print(year, 'is not a leap year')
    else:
        print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')