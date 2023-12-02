import re

# Open the file
file = open("Day2\Day2.txt", "r").read().splitlines()

# Split the file into lists where he find the \n
file = [x.split('\n') for x in file]

# Make regex to find colors
red = re.compile(r"(\d+) red")
green = re.compile(r"(\d+) green")
blue = re.compile(r"(\d+) blue")

# For every game, separate the colors
sol1 = sol2 = 0
for game in file:
    reds = re.findall(red, game[0])
    greens = re.findall(green, game[0])
    blues = re.findall(blue, game[0])

    # Take the level number
    match = re.search(r'Game (\d+):', game[0])
    level = match.group(1)

    # Cast the colors to integers and make a list
    reds = list(map(int, reds))
    greens = list(map(int, greens))
    blues = list(map(int, blues))
    
    # Check if only one element in red is bigger than 12, and so on...
    if not any(x > 12 for x in reds) and not any(x > 13 for x in greens) and not any(x > 14 for x in blues):
        #print(f'GAME: {level}')
        #print(f'reds: {reds}')
        #print(f'greens: {greens}')
        #print(f'blues: {blues}')
        sol1 += int(level)
    sol2 += (max(reds) * max(greens) * max(blues))

print("Solution 1: ", sol1)
print("Solution 2: ", sol2)