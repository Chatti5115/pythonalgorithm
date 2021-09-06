# a = list(map(int, input().split(' ')))
# ascending = True
# descending = True
# for i in range(1,8):
#     if a[i] > a[i-1]:
#         descending = False
#     elif a[i] < a[i-1]:
#         ascending = False
# if ascending:
#     print('ascending')
# elif descending:
#     print('descending')
# else:
#     print('mixed')

n,m = list(map(int, input().split(' ')))
data = list(map(int, input().split(' ')))

result = 0
length = len(data)

count = 0
for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m :
                result = max(result, sum_value)
print(result)