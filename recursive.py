def factorial(num):
    if num > 1:
        return num * factorial(num -1)
    else:
        return num

for num in range(10):
    print(factorial(num))


def factorial1(num):
    if num <=1:
        return num
    return num * factorial1(num -1)

for num in range(10):
    print(factorial1(num))

def multiple(num):
    return_value = 1
    for index in range(1, num+1):
        return_value = return_value * index
    return return_value


def multiple1(num):
    if num <=1:
        return num
    return num * multiple1(num -1)
print(multiple(10))
print("multiple1",multiple1(10))


import random
data = random.sample(range(100), 10)
print(data)

def sum_list(data):
    if len(data) <=1:
        return data[0]
    return data[0] + sum_list(data[1:])
print("sum_list",sum_list(data))

