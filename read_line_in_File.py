import os, sys

file_name = input('Insert the Filename: ')
f = open(file_name, '+r')
tmp_file_content = f.readlines()
total_lines_count = len(tmp_file_content)

lines = int(input('Enter number of lines to be displayed: '))

for i in range(total_lines_count, total_lines_count-lines, -1):
    print(i, 'th line would be:', tmp_file_content[i-1], end="")


#===== OUTPUT ======
#Insert the Filename: /tmp/file
#Enter number of lines to be displayed: 3        
#10 th line would be: line10
#9 th line would be: line9   
#8 th line would be: line8          


