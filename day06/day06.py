# load file
with open('input.txt') as f:
    lines = f.readlines()

# PART 1
line = lines[0]
for i in range(4, len(line)):
    marker = line[i-4:i]
    if len(set(marker)) != len(marker):  # has dupe
        continue
    else:
        print(i)
        print(marker)
        break

# PART 2
line = lines[0]
for i in range(14, len(line)):
    marker = line[i-14:i]
    if len(set(marker)) != len(marker):  # has dupe
        continue
    else:
        print(i)
        print(marker)
        break
