import random

def read():
    object_file = open('randomnum.txt', 'r')
    count = 0
    print("list of random numbers:")
    for i in object_file.readlines():
        i = int(i)
        print(i)
        count += 1
    print(count)
    print("Random Number Count:",count)
    object_file.close()
read()