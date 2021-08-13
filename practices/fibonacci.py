# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
#
# print(fibonacci(100))

# method 1
list = []
list.append(0)
list.append(1)


def fibonacci(n):
    if n == 2:
        return 1
    else:
        for nums in range(2, n+1):
            a = list[nums-1]+list[nums-2]
            list.append(a)
        return list[n]


print('请输入fibonacci数列上限')
x = int(input())
if x < 2:
    print('wrong input')
else:
    print(f'k={x} {fibonacci(x)}')
for i in reversed(range(x)):
    print(f'k={i}  {list[i]}')



# method 2
# def fibonacci(n):
#     a = 0
#     b = 1
#     if n == 2:
#         return 1
#     else:
#         for nums in range(1,n):
#             t = b
#             b = a + b
#             a = t
#         return b
#
#
# print('请输入fibonacci数列上限')
# x = int(input())
# if x < 2:
#     print('wrong input')
# else:
#     for num in range(x+1):
#         if num < 2:
#             continue
#         else:
#             print(f'k={num}  fibonacci={fibonacci(num)}')