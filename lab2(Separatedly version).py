##1
file = open('D:\\学习资料\\课程资料\\2021-2022第一学期\\EE308软件工程\\labs\\code.cpp','r',encoding='utf-8')

keywords = ["auto", "break", "case", "char", "const",	"continue","default","do",
            "double","else","enum","extern","float","for","goto","if",
            "int",	"long"	,"register", "return", "short", "signed", "sizeof", "static",
            "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"]


total_counter = 0

for lines in file.readlines():

    for keyword in keywords:
        if lines.find(keyword) != -1:
            if keyword == "do":
                if lines.find("double") != -1:
                    continue
            total_counter += 1

print("total num:", total_counter)
file.close()


##2

total_switch = 0
total_case = 0
case_num = []

file1 = open('D:\\学习资料\\课程资料\\2021-2022第一学期\\EE308软件工程\\labs\\code.cpp','r',encoding='utf-8')

for line in file1.readlines():

    if line.find("switch") != -1:
        total_switch = total_switch + 1
        case_num.append(total_case)
        total_case = 0

    if line.find("case") != -1:
        total_case += 1

case_num.append(total_case)


print("switch num:", total_switch)

print("case num: {} {}".format(case_num[1],case_num[2]))

file1.close()

##3

file2 = open('D:\\学习资料\\课程资料\\2021-2022第一学期\\EE308软件工程\\labs\\code.cpp','r',encoding='utf-8')

if_else_num = 0

for line1 in file2.readlines():
    if line1.find("if") != -1 and line1.find("else if") == -1:
        x = 0
        if_else_num += 1
    if line1.find("else if") != -1:
        x += 1
        continue
    if line1.find("else") != -1 and line1.find("else if") == -1:
        if x != 0:
            if_else_num -= 1

print("if-else num:", if_else_num)

file2.close()

##4

file3 = open('D:\\学习资料\\课程资料\\2021-2022第一学期\\EE308软件工程\\labs\\code.cpp','r',encoding='utf-8')

if_elseif_else = 0

for line2 in file3.readlines():
    if line2.find("if") != -1 and line2.find("else if") == -1:
        y = 0
        if_elseif_else += 1
    if line2.find("else if") != -1:
        y += 1
        continue
    if line2.find("else") != -1 and line2.find("else if") == -1:
        if y == 0:
            if_elseif_else -= 1

print("if-elseif-else num:", if_elseif_else)

file3.close()