# stl = ['Email:', 'SSN:','Address:','Home Phone:','Mobile Phone: ','DOB:','Date of Surgery:','Date of Service:','Facility of Service:','Clinic Number:','Employer:','Work Phone: ','Fax: ','Type:','IPA:','Health Plan:','ID #:','Claims Address:','Group #:','Claim # / PO #:','Phone:','Fax:','Contact','Adjuster Email','Util Review Phone','Util Review Fax','Doctor:','NPI #: ','Date of Injury: ','Body Parts:','Body Part Side:','Gender:','Diagnosis:','Diagnosis 2:','Procedure:']
# print(stl[0])
# print()
# print(stl[-1])

# stl = ['Email:', 'SSN:','Address:','Home Phone:','Mobile Phone: ','DOB:','Date of Surgery:','Date of Service:','Facility of Service:','Clinic Number:','Employer:','Work Phone: ','Fax: ','Type:','IPA:','Health Plan:','ID #:','Claims Address:','Group #:','Claim # / PO #:','Phone:','Fax:','Contact','Adjuster Email','Util Review Phone','Util Review Fax','Doctor:','NPI #: ','Date of Injury: ','Body Parts:','Body Part Side:','Gender:','Diagnosis:','Diagnosis 2:','Procedure:']
# print(stl[-2])

# import calendar
# yy = int(input())
# mm = int(input())
# print(calendar.month(yy, mm))

# n = int(input())
# print(n**(0.5))

# lst = [1, 1, 2, 1, 2, 2, 2, 2]
# max = 0
# for i in lst:
# 	count = lst.count(i)
# 	if max < count:
# 		max = count
# print(max)

# lst =  [25, 6, 72, 4]
# stl = ''
# for i in lst:
# 	i = str(i)
# 	stl += i 
# input(str(stl))	

# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
# 	399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527] 
# lst = []    
# a = numbers.index(217)
# for i in range(a, len(numbers)-1):
# 	if numbers[i] % 2 == 0:
# 		lst.append(numbers[i])
# print(lst)	

lst1 = [1, 2, 3, 5, 8, 13, 42, 5, 8]
lst2 = [5, 8, 13, 42]
count = 0
for i in range(0,len(lst1)):
	for j in range(i,len(lst1)-i)
		if lst2[j] == lst1[i]:
			count += 1
if count == len(lst2):
	print("True")
else:
	print('False')	
print('hello world')
