# load file
with open('input.txt') as f:
    lines = f.readlines()

# PART 1
# init lists
x = [[], [], [], [], [], [], [], [], []]

instruction_start = 0
for i in range(len(lines)):
    line = list(lines[i][:-1])
    if line == [] or line[1] == '1':  # we don't need this shit
        continue
    elif line[0] == 'm':
        instruction_start = i
        break
    else:  # construct lists of elements

    # SO THIS IS DEFINITELY BAD: try to implement this??
    # locations = [i for i in range(len(line)) if line[i].isupper()]
    # for l in locations:
        # stacks[l].append(line[l])
        print(line)
        if len(line) > 1:  # first column
            if line[1] != ' ':
                x[0].append(line[1])
        if len(line) > 5:  # second column
            if line[5] != ' ':
                x[1].append(line[5])
        if len(line) > 9:  # third column
            if line[9] != ' ':
                x[2].append(line[9])
        if len(line) > 13:  # fourth column
            if line[13] != ' ':
                x[3].append(line[13])
        if len(line) > 17:  # fifth column
            if line[17] != ' ':
                x[4].append(line[17])
        if len(line) > 21:  # sixth column
            if line[21] != ' ':
                x[5].append(line[21])
        if len(line) > 25:  # seventh column
            if line[25] != ' ':
                x[6].append(line[25])
        if len(line) > 29:  # eighth column
            if line[29] != ' ':
                x[7].append(line[29])
        if len(line) > 33:  # ninth column
            if line[33] != ' ':
                x[8].append(line[33])

print('break')
for i in range(len(x)):
    x[i] = x[i][::-1]
    print(x[i])

print(' ')
for i in range(instruction_start,len(lines)):
    move_num = lines[i].split(' ')[1]
    source = lines[i].split(' ')[3]
    destination = lines[i].split(' ')[5]
    for idx in range(int(move_num)):
        #print(idx)
        temp = x[int(source)-1].pop()
        x[int(destination)-1].append(temp)

for i in range(len(x)):
    print(x[i])