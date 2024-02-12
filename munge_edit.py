# Place code below to do the munging part of this assignment.

# open file
f = open("data/GLB.Ts+dSST.txt", 'r')
   
# create new file which will be our csv
f_new = open("data/clean_data.csv", 'w')


# skipping first seven lines
for i in range(7):
    f.readline().strip()   

# HEADER LINE
header = f.readline().strip()
# split to get rid of spaces between names of columns + replace with commas
column_names = header.split()
# print(len(column_names)) # 20 COLUMNS
column_names_str = ','.join(column_names)
f_new.write(column_names_str +"\n")

# get rid of bottom seven lines of descriptors
all_lines = f.readlines()
for i in range(7):
    all_lines.pop()

# filter to turn into csv
for i in range(len(all_lines)):
    l_list = all_lines[i].split()
    l_str = ','.join(l_list)
    if l_str == column_names_str: # if repeated header
        continue
    elif l_list == []: # if line break
        continue
    elif i == len(all_lines):
        f_new.write(l_str) # to not add line break on last line
    else:
        f_new.write(l_str + "\n")
        '''
        for j in range(len(l_list)):
            if l_list[j] == "***":
                l_list[j] = float("NaN")
        '''

# close both files
f_new.close()
f.close()

'''
with open("GLB.Ts+dSST.txt", 'r') as input_file, open("clean_data.csv", 'w') as output_file:
    for i in range(7):
        f.readline().strip()   

    # header = f.readline().strip() # HEADER LINE
    for line in input_file:
        modified_line = ','.join(line.split())
        output_file.write(modified_line + '\n')


with open("GLB.Ts+dSST.txt", 'r') as input_file, open("clean_data.csv", 'w') as output_file:
    
    for line_number, line in enumerate(input_file, 1):
        # Skip the first 7 lines
        if line_number <= 7:
            continue
        # For lines after the first 7, split and join with commas
        modified_line = ','.join(line.split())
        # Write the modified line to the output file, adding a newline character
        output_file.write(modified_line + '\n')
'''