# def split_func(data):
#     medium = int(len(data)/2)
#     print(medium)
#     left = data[:medium]
#     right = data[medium:]
#     print(left, right)
#
# print(split_func([1,5,3,2,4]))


def mergeSplit(data):
    if len(data) <=1:
        return data
    medium = int(len(data) /2)
    left = mergeSplit(data[:medium])
    right = mergeSplit(data[medium:])
    return merge(left, right)


def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    # case1 - left/right 둘다 있을 때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point +=1
        else:
            merged.append(left[left_point])
            left_point +=1

    # case2 - left 데이터가 없을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point +=1

    # case3 - right 데이터가 없을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged

import random

data_list = random.sample(range(100), 10)
print(mergeSplit(data_list))
