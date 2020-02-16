# 1
# import datetime
# now = datetime.datetime.now()
# date = datetime.datetime(2019, 11, 29, 13, 25, 45)
# delta = now - date
# print(delta.days)
# print(delta.seconds // 3600)
# print((delta.seconds % 3600) // 60)

# 2
# import itertools
# lst = [2, 5, 8]
# data = list(itertools.combinations(lst, 2))
# print(data)

# 3
# from collections import defaultdict
# from collections import Counter
# super_dict = {}
# dicts = []
# sum = Counter()
# lst = ['qrqwqw', 'efwreb', 'u,ugkf', 'oipierpot', 'pk;l//',
#        'bdmbd.', 'oicpvoic', 'qj;q;q', 'nzcz.xco', 'lrtky;rt;']
# for i in lst:
#     dict = {c: i.count(c) for c in i}
#     dicts.append(dict)
# for d in lst:
#     sum.update(d)
# print(sum)    



a = [i for i in range(1001) if i % 7 == 0]
print(a)

# 5
# sum = 0
# for i in range(0, 2001):
#     if i > 99:
#         sum += i
# print(sum)

# 6(недоделана)
# import re
# a = open('/home/vlad/Documents/1112.txt')
# text = a.read().lower()
# text_ad = re.sub(r'[?|.|,|!|]', r'', text)
# lst = text_ad.split(' ')
# a = [i for i in lst if i != [ '']]
# print(a)

# # 7
# import random
# import string
# lst = []
# a = int(input())
# sum = ''
# for i in range(26):
# 	sum = ''
# 	for j in range(a):
# 		x = random.choice(string.ascii_letters)
# 		sum += x
# 	lst.append(sum)
# print(lst)
# 8
# недоделано
# import string

# lst = ['HT', 'rv', 'UL', 'mD', 'ad', 'Qw', 'ad', 'EX', 'Kn', 'kD', 'MI', 'ti', 'HB', 'Xk', 'ET',
#        'xO', 'lh', 'pg', 'VN', 'su', 'kc', 'iF', 'Bm', 'vK', 'Vd', 'wF', 'zh', 'Ph', 'KY', 'Go']
# for i in lst:
# 	i.splitlines()
# print(lst)

# 9
# import random
# a = [random.randint(0, 99) for i in range(5)]
# print(a)
# for i in range(5):
#     element = random.randint(0, 99)
#     a.append(element)
#     a.sort()
#     print(a)

# 10
# lst = [[3, 5, 8], [5, 8, 10], [1, 2], [2, 13, 9]]
# lst = sorted(lst, key=lambda x: sum(x), reverse=True)
# print(lst)

# 11


# 12
