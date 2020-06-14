n_terms = int(input('How many Fibonacci numbers do you want? '))

#first two terms
n1 = 0
n2 = 1
count = 0

print("Fibonacci Sequence upto", n_terms,":")
while count < n_terms:
    print(n1, end=', ')
    nth = n1 + n2

    #update values
    n1 = n2
    n2 = nth
    count += 1
print()