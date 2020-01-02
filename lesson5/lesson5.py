import datetime
import re
# import string

# 1

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

# str = 'The plot was a string of anecdotes from the senseless shootings of friends that Brinsley knew.'
# pattern = r'\b[\w]{3}'
# match = re.findall(pattern, str)
# print(match)

# 3

# def func(lst):
#     lst2 = []
#     for mails in lst:
#         a = mails[mails.find('@'):mails.rfind('.')]
#         lst2.append(a)
#     return lst2


# lst = ['baveja@att.net', 'mhassel@comcast.net', 'heine@sbcglobal.net', 'gbacon@comcast.net', 'slaff@hotmail.com', 'seemant@yahoo.com',
#       'miltchev@verizon.net', 'ducasse@hotmail.com', 'chaikin@yahoo.ca', 'agolomsh@yahoo.ca', 'joehall@msn.com', 'ilikered@optonline.net']
# print(func(lst))
# # написать еще через регулярное выражение

# def func(lst):
#     lst2 = []
#     for mails in lst:
#     	result = re.findall(r'@\w+',mails)
#     	lst2 = lst2 + result
#     return lst2


# lst = ['baveja@att.net', 'mhassel@comcast.net', 'heine@sbcglobal.net', 'gbacon@comcast.net', 'slaff@hotmail.com', 'seemant@yahoo.com',
#        'miltchev@verizon.net', 'ducasse@hotmail.com', 'chaikin@yahoo.ca', 'agolomsh@yahoo.ca', 'joehall@msn.com', 'ilikered@optonline.net']
# print(func(lst))
# 4 не сделано обычным методом

# def func(str):
#     lst2 = []
#     lst = str.split()
#     for i in lst:
#         if i.isalpha() not True:
# 			if i.format("%d-%m-%Y"):
# 				lst2.append(i)
# 	return lst2

def func(str):
	result = []
	pattern = r'\d\d-\d\d-\d{4}'
	lst = re.findall(pattern, str)
	for date in lst:
		try:	
			true_date = datetime.datetime.strptime(date,'%m-%d-%Y')
			result.append(date)
		except ValueError:
  			print('Invalid date!')
	return result	


str = "Lorem ipsum dolor sit Amit 34-3456 12-06-2012 amet, consectetur adipiscing elit, sed do eiusmod tempor Amit 42-2216 31-06-2019 incididunt ut labore et dolore Amit 32-6782 03-12-2270 magna aliqua."
print(func(str))


# 5

# def swap_case(str):
# 	return str.swapcase()

# print(swap_case('Hello World'))

# 6

# def repalase_spaces(stroka):
#     return stroka.replace(' ', '-')


# stroka = 'Hello World'
# print(repalase_spaces(stroka))

# 7

# def replase_char(str, index, a):
#     return str[:index] + a + str[index + 1:]


# print(replase_char('Hello World', 3, 'a'))

# 8

# def check_palidrom(str):
#     a = str.replace(' ', '')
#     s = a.lower()
#     if s == s[::-1]:
#         return True
#     return False


# print(check_palidrom('Never odd or even'))

# 9

# def reverse_string(str):
# 	lst = str.split()
# 	lst.sort(reverse = True)
# 	str = ' '.join(lst)
# 	return str


# print(reverse_string('never give up'))

# 10

# def penultimate_len(str):
# 	first = str.rfind(' ')
# 	slice= str[:first]
# 	second = slice.rfind(' ')
# 	return first - second -1

# print(penultimate_len('In the end the winner is still the last man standing'))


# # 11


# def roman_to_int(str):
#     roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     result = 0
#     for key, values in enumerate(str):
#     	if key + 1 < len(str) and roman[str[key]] < roman[str[key+1]]:
#     		result -= roman[str[key]]
#     	else:
#     		result += roman[str[key]]
#     return result

# print(roman_to_int('XIV'))

# 12

# def calculate_chars(str):
# 	lst = list(str)
# 	for i in set(lst):
# 		print(i,': ',lst.count(i))


# calculate_chars('Hello')


# ver 2

# def calculate_chars(str):
# 	dit = {}
# 	for words in str:
# 		if words not in dit:
# 			dit[words] = 1
# 		else:
# 			dit[words] += 1
# 	return dit


# print(calculate_chars('hello'))
