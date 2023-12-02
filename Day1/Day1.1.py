# Open the file
file = open("Day1\Day1.txt", "r")

# Save in a list each line of the file
lines = file.readlines()
all_numbers = []

# For each line, save the numbers in a list
for line in lines:
    temp = []
    for c in line:
        if c.isdigit():
            #Add the number to the list
            temp.append(c)
    all_numbers.append(temp)

# For each list, if there is only one number, add another one of the same
for list in all_numbers:
    if len(list) == 1:
        list.append(list[0])

# Now put all the numbers in the list together
final_list = []
for list in all_numbers:
    final_list.append(int(''.join(list)))

# For every number in the list, keep only the first and the last digit, exept for the list where there are only two numbers
for i in range(len(final_list)):
    if len(all_numbers[i]) > 2:
        final_list[i] = int(all_numbers[i][0] + all_numbers[i][-1])

# Sum all the numbers
sum = 0
for number in final_list:
    sum += number

print(sum)
