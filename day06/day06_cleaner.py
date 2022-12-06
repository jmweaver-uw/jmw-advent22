def find_marker(signal, width):
    for i in range(width, len(signal)):
        marker = line[i-width:i]
        if len(set(marker)) != len(marker):  # has dupe
            continue
        else:
            return i


# load file
with open('input.txt') as f:
    line = f.readline()

print("Part 1 marker is ", find_marker(line, 4))
print("Part 2 marker is ", find_marker(line, 14))