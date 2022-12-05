# load file
with open('input.txt') as f:
    lines = f.readlines()

# PART 1
count = 0
for i in range(len(lines)):
    line = lines[i].strip()
    as1 = line.split(',')[0]
    as2 = line.split(',')[1]

    if ((int(as1.split('-')[0]) >= int(as2.split('-')[0])) and (int(as1.split('-')[1]) <= int(as2.split('-')[1]))) or \
            ((int(as2.split('-')[0]) >= int(as1.split('-')[0])) and (int(as2.split('-')[1]) <= int(as1.split('-')[1]))):
        count += 1

print(count)

# PART 2
count = 0
for i in range(len(lines)):
    line = lines[i].strip()
    as1 = line.split(',')[0]
    as2 = line.split(',')[1]

    # check if assignment 1 is always lower than assignment 2
    if int(as1.split('-')[1]) < int(as2.split('-')[0]):
        count += 1
    elif int(as2.split('-')[1]) < int(as1.split('-')[0]):
        count += 1

        # old 749, too low

print(len(lines)-count)
