import re

filenames = []
get_name = open(r"filename_list.txt")
for line in get_name:
    #print(line)
    filenames.append(line.strip())
get_name.close() 

output = open(r"all.txt","a")
for f in filenames:
    get_data = open(f)
    c = 0
    for line in get_data:
        c += 1
        if c == 712:
            output.write(line)
        elif c > 1177 and c < 2458:
                output.write(line)
    get_data.close()
output.close()

