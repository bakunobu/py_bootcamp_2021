file_1_cont = []
file_2_cont = []


with open('day_twenty_six/file1.txt') as f:
    lines = f.readlines()
    for line in lines:
        file_1_cont.append(int(line[:-1]))


with open('day_twenty_six/file2.txt') as f:
    lines = f.readlines()
    for line in lines:
        file_2_cont.append(int(line[:-1]))


file_1_set = set(file_1_cont)
file_2_set = set(file_2_cont)

common = file_1_set.intersection(file_2_set)
print(sorted(list(common)))