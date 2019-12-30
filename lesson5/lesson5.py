# 1
import string
import re


# def func(str):
#     split = str.split()
#     for i in range(len(split)):
#         if split[i].isalpha():
#             return split[i]
#             break


# # str = "hello world, hello qqwe qadasd."

# first_word = re.findall(r'^\w+', "hello world, hello qqwe qadasd.")

# print(first_word)
# print(func(str))

# 2

# def func(str):
# 	lst1 = []
# 	lst = str.split()
# 	for words in lst:
# 		if len(words) >= 3:
# 			lst1.append(words)
# 		else:
# 			while len(words) < 3:
# 				words = words + ' '
# 			lst1.append(words)
# 	return lst1


# str = 'The plot was a string of anecdotes from the 
#        senseless shootings of friends that Brinsley knew.'
# print(func(str))
# print(func(str))
# написать еще через регулярное выражение

# 3

def func(lst):
	lst2 = []
	for mails in lst:
		a = mails[mails.find('@'):mails.rfind('.')]
		lst2.append(a)
	return lst2

lst = ['baveja@att.net', 'mhassel@comcast.net', 'heine@sbcglobal.net', 'gbacon@comcast.net', 'slaff@hotmail.com', 'seemant@yahoo.com',
       'miltchev@verizon.net', 'ducasse@hotmail.com', 'chaikin@yahoo.ca', 'agolomsh@yahoo.ca', 'joehall@msn.com', 'ilikered@optonline.net']
print(func(lst))
# написать еще через регулярное выражение

# 3


