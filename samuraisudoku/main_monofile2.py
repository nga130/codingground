import re


def get_sudoku(data_line):
    get_code = re.findall(r'width=35>(.+)<',data_line)
    return get_code


descrp = []
sudoku = []

input_file = open(r"filename.txt")

c = 0
temp_sud = []

for line in input_file:
    
    c += 1

    if c == 1:
        #print(line)
        get_des = re.findall(r'left;(.+)</td></tr>',line)
        #print(get_des)
    elif c == 2:
        get_sud = get_sudoku(line)
        #print(get_sud)
    elif c > 1 and c < 443:
        get_sud += get_sudoku(line)
        #print(get_sud)

    if c == 449:
        c = 0

        for d in get_des:
            descrp.append(str(d))

        for s in get_sud:
            temp_sud.append(str(s))
        code = "".join(temp_sud) 
        sudoku.append(code)

        temp_sud[:] = []
        #temp_sud.clear()

input_file.close()


output_file = open(r"samurai-sudoku.txt","a")

for i in range(len(descrp)):

    des = str(descrp[i])
    des = des.replace(r'</td><td style="text-align:right;">'," / ")
    #print(des)

    sud = sudoku[i]
    sud = sud.replace("&nbsp; ","0")
    #print(sud)

    sud1,sud2,sud3,sud4,sud5 = "","","","",""

    for j in range(0,9,1):        sud1 += sud[j]
    for j in range(9,18,1):        sud2 += sud[j]
    for j in range(18,27,1):        sud1 += sud[j]
    for j in range(27,36,1):        sud2 += sud[j]
    for j in range(36,45,1):        sud1 += sud[j]
    for j in range(45,54,1):        sud2 += sud[j]
    for j in range(54,63,1):        sud1 += sud[j]
    for j in range(63,72,1):        sud2 += sud[j]
    for j in range(72,81,1):        sud1 += sud[j]
    for j in range(81,90,1):        sud2 += sud[j]
    for j in range(90,99,1):        sud1 += sud[j]
    for j in range(99,108,1):        sud2 += sud[j]

    for j in range(108,117,1):        sud1 += sud[j]
    for j in range(114,123,1):        sud3 += sud[j]
    for j in range(120,129,1):        sud2 += sud[j]
    for j in range(129,138,1):        sud1 += sud[j]
    for j in range(135,144,1):        sud3 += sud[j]
    for j in range(141,150,1):        sud2 += sud[j]
    for j in range(150,159,1):        sud1 += sud[j]
    for j in range(156,165,1):        sud3 += sud[j]
    for j in range(162,171,1):        sud2 += sud[j]

    for j in range(171,180,1):        sud3 += sud[j]
    for j in range(180,189,1):        sud3 += sud[j]
    for j in range(189,198,1):        sud3 += sud[j]

    for j in range(198,207,1):        sud4 += sud[j]
    for j in range(204,213,1):        sud3 += sud[j]
    for j in range(210,219,1):        sud5 += sud[j]
    for j in range(219,228,1):        sud4 += sud[j]
    for j in range(225,234,1):        sud3 += sud[j]
    for j in range(231,240,1):        sud5 += sud[j]
    for j in range(240,249,1):        sud4 += sud[j]
    for j in range(246,255,1):        sud3 += sud[j]
    for j in range(252,261,1):        sud5 += sud[j]

    for j in range(261,270,1):        sud4 += sud[j]
    for j in range(270,279,1):        sud5 += sud[j]
    for j in range(279,288,1):        sud4 += sud[j]
    for j in range(288,297,1):        sud5 += sud[j]
    for j in range(297,306,1):        sud4 += sud[j]
    for j in range(306,315,1):        sud5 += sud[j]
    for j in range(315,324,1):        sud4 += sud[j]
    for j in range(324,333,1):        sud5 += sud[j]
    for j in range(333,342,1):        sud4 += sud[j]
    for j in range(342,351,1):        sud5 += sud[j]
    for j in range(351,360,1):        sud4 += sud[j]
    for j in range(360,369,1):        sud5 += sud[j]

    #print(sud1)
    #print(sud2)
    #print(sud3)
    #print(sud4)
    #print(sud5)
    output_file.write(des)
    output_file.write("\n")
    output_file.write(sud1)
    output_file.write("\n")
    output_file.write(sud2)
    output_file.write("\n")
    output_file.write(sud3)
    output_file.write("\n")
    output_file.write(sud4)
    output_file.write("\n")
    output_file.write(sud5)
    output_file.write("\n")
    output_file.write("\n")

output_file.close()
