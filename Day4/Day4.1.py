import re

with open("Day4/Day4.txt", "r") as myfile:
    file = myfile.read().split('\n')


count = 0
for line in file:
    # Take the numbers from : to |
    winning_num = re.search(r':(.*?)\|', line).group(1).split()

    # Take the numbers from | to the end of the line
    my_num = re.search(r'\|(.*?)$', line).group(1).split()

    occurrence = 0
    for winNum in winning_num:
        if winNum in my_num:
            occurrence += 1
    if occurrence == 0:
        continue
    count += 2**(occurrence-1)
print(count)