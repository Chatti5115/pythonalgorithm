# def factorial(n):
#     fac =1
#     for index in range(2, n+1):
#         # 2,3
#         fac = fac * index
#     return fac

def factorial(n):
    if n >1:
        return n * factorial(n-1)
    else :
        return 1

print(factorial(3))