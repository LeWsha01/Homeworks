import json
import csv
# import openpyxl


# 1
json_path = '/home/vlad/Documents/python/Homeworks/lesson6/file.json'
csv_path = '/home/vlad/Documents/python/Homeworks/lesson6/file_csv.csv'

with open(json_path, 'r') as json_file:
    lst = json.load(json_file)

result = []
for elements in lst:
    for key in elements:
        if key not in result:
            result.append(key)
        else:
            pass
# result = []
# for i in lst:
# 	for key in i:
# 		result.append(key)
# result = set(result)
# result =list(result)
# print(result)

with open(csv_path, 'w') as file_csv:
    writer = csv.writer(file_csv)
    writer = csv.DictWriter(file_csv, fieldnames=result)
    writer.writeheader()
    for dit in lst:
        writer.writerow(dit)

# 2

# wb = openpyxl.load_workbook(filename='table2.xlsx')
# sheet = wb['Лист1']
# ws = wb.active
# rows = sheet.max_row
# cols = sheet.max_column
# print(rows, cols)
# ws.insert_cols(0)
# for i in range(1, rows + 1):
#     sheet['B{}'.format(i)] = str(sheet['B{}'.format(i)].value) + \
#         ' ' + str(sheet['C{}'.format(i)].value)

#     print(sheet['B{}'.format(i)].value)

# for i in range(1, rows + 1):
#     ws.merge_cells('B{}:C{}'.format(i, i))
# marks = []
# for i in range(1, rows + 1):
#     for j in range(4, cols + 2):
#         c = ws.cell(i, j)
#         marks.append(c.value)

# marks = list(filter(None, marks))
# sum = 0
# n = 0
# print(marks)
# for i in range(0, len(marks) - 1):
#     if marks[i] != ' end':
#         n += 1
#         sum += marks[i]


def excel_change(file):

    wb = openpyxl.load_workbook(filename=file)

    sheet = wb.worksheets[0]  

    col = sheet.max_column  
    row = sheet.max_row  

    sheet.insert_cols(1)

    for j in range(1, row + 1):  
        sheet['B{}'.format(j)].value = str(sheet.cell(j, 2).value) + ' ' + str(sheet.cell(j, 3).value)
        sheet.merge_cells('B{}:C{}'.format(j, j))

    lists_marks = []

    for i in range(1, row + 1):  
        count = 0
        list = []
        for j in range(4, col + 1):
            if sheet.cell(i, j).value == 'end':
                break
            if sheet.cell(i, j).value is None:
                continue
            else:
                list.append(int(sheet.cell(i, j).value))
                count += 1
        sheet[f'A{i}'] = '=SUM(B{}:Z{})/{}'.format(i, i, count)
        lists_marks.append(list)

    inx = 0

    res = {}

    for row_index in range(1, row + 1):
        res[sheet.cell(row_index, 2).value] = {
                        'marks': lists_marks[inx],
                        'average_marks': sum(lists_marks[inx]) / len(lists_marks[inx])
                    }

        inx += 1

    result = {'students': res}

    return result


def from_excel_to_json(rs, p):
    with open(p, 'w') as json_file:
        json_str = json.dumps(rs, indent=1)
        json_file.write(json_str)


if __name__ == '__main__':
    path_excel = 'Student.xlsx'
    path_json = 'excel_json.json'
    re = excel_change(path_excel)
    from_excel_to_json(re, path_json)
#         print(sum, n)
#     elif marks[i] == ' end' :
#         sum == 0
#         n == 0
