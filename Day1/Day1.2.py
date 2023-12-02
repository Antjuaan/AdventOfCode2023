import re

# Open the file
file = open("Day1\Day1.txt", "r")
file = file.read().splitlines()

# Dictionary mapping words to their corresponding numeric values
numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

# Regular expression to match either a digit (\d) or any of the words in the 'numbers' dictionary
regex = r'\d|' + r"|".join(numbers)

# Regular expression to match either a digit (\d) or the reverse of any of the words in the 'numbers' dictionary
regex_reverse = r'\d|' + r"|".join(d[::-1] for d in numbers)


sum = 0
for line in file:
    # Find the first digit or word match in the 'line' based on the 'regex' pattern
    first_digit = re.search(regex, line)[0]

    # Reverse the 'line', find the last digit or word match based on the reversed 'regex_reverse' pattern, and then reverse the result to get the correct order
    last_digit = re.search(regex_reverse, line[::-1])[0][::-1]

    # Convert the words to their corresponding numeric values
    for num in numbers:
        if num == first_digit:
            first_digit = numbers[num]
        if num == last_digit:
            last_digit = numbers[num]

    # Now put together the two digits and sum them
    sum += int(str(first_digit) + str(last_digit))
print(sum)
