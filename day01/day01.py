# load file
with open('calories.txt') as f:
    lines = f.readlines()

# iterate through
cal_dict = {}  # initialize empty dictionary
elf_count = 1  # initialize elf count
cal_count = 0  # initialize calories
for i in range(len(lines)):
    if not lines[i].startswith('\n'):
        cal_count += int(lines[i])
        if i == len(lines)-1: # final loop
            cal_dict['Elf ' + str(elf_count)] = cal_count
            print('Elf ' + str(elf_count) + ' has ' + str(cal_count) + ' calories')
    else:
        cal_dict['Elf ' + str(elf_count)] = cal_count
        print('Elf ' + str(elf_count) + ' has ' + str(cal_count) + ' calories')
        elf_count += 1  # increment elf count
        cal_count = 0  # rest calorie count

most_cals = max(cal_dict.values())
who = max(cal_dict, key=cal_dict.get)
print(who + ' has the most calories with ' + str(most_cals))

