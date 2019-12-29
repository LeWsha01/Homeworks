# 1

# def qwe(*args):
#     lst = list(args)
#     lst.sort()
#     return lst[-2]

# print(qwe(1, 2, 4, 56, 12, 13))

# 2
# def fanction(a, b={'foo': 2, 'bar': 8}):
#     for i in b.values():
#         if i == a:
#             return True
#     return False


# print(fanction(5))

# 3
# from WordToNum.word_to_num import WordToNum


# def functin(*args):
#     lst2 = []
#     wtn = WordToNum()
#     lst = list(args)
#     for i in lst:
#         lst2.append(wtn.to_num(i))
#     return sum(lst2)

# print(functin("five", "six"))

#  4


# from WordToNum.word_to_num import WordToNum


# def functin(*args):
#     lst2 = []
#     wtn = WordToNum()
#     lst = list(args)
#     for i in lst:
#         lst2.append(wtn.to_num(i))
#     return sum(lst2)

# print(functin("five","six"))

# 5

# def functin(str):
#     upper = 0
#     lower = 0
#     punctuation = 0
#     for i in str:
#         if 'a' <= i <= 'z':
#             lower += 1
#         if 'A' <= i <= 'Z':
#             upper += 1
#         if i == '.' or i == ',' or i == '!' or i == '?':
#             punctuation += 1
#     space = str.count(' ')

#     return 'upper: %(upper)s, lower:%(lower)x, space: %(space)s, punctuation: %(punctuation)s.' % {'upper': upper, 'lower': lower, 'space': space, 'punctuation': punctuation}


# print(functin('Hello, World'))

# 6

# def functin(lst):
#     lst2 = set(lst)
#     lst3 = list(lst2)
#     lst3.sort(reverse = True)
#     return lst3

# lst = [19, 12, 4, 12, 7, 9, 5, 8, 3, 17, 8, 19, 12, 3, 6, 15, 15, 16, 11, 13, 19, 16, 11, 12, 20, 2, 16, 7, 15, 2, 6, 15, 17, 15, 19, 4, 13, 14, 6, 5, 12, 2, 20, 7, 19, 4, 15, 16, 7, 20]
# print(functin(lst))

# 7

# def func(n):
#     for i in range(2, n // 2):
#         if n % i == 0:
#             return False
#             exit()
#     return True


# print(func(21))

# 8

# def func(str):
#     c = str[::-1]
#     if str == c:
#         return True
#     else:
#         return False    


# print(func('adadda'))   

# 9


# 10


# def func(n):
#     if n == 0:
#         return 0
#     else:
#         return n + func(n - 1)        


# print(func(3))    


# 11
def multiply(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0]*multiply(lst[1:])


print(multiply([1, 2, 3, 3]))

