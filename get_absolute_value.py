def get_absolute(num):
    if num >= 0:
        return num
    else:
        return -num

print(get_absolute(int(input('Please write the number '))))