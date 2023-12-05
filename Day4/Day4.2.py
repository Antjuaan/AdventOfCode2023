import re

def line_occurrence(line):
    # Save the card number
    cardNum = int(re.search(r'\d+', line[:line.index(':')]).group())

    # Save the winning numbers 
    winning_numbers = line[line.index(':')+1:line.index('|')-1].split()

    # Save my numbers 
    my_numbers = line[line.index('|')+1:].strip().split()

    # Count the occurrence of my numbers in the winning numbers
    occurrence = 0
    for num in my_numbers:
        if num in winning_numbers:
            occurrence += 1
    return cardNum, occurrence


with open("Day4/Day4.txt", "r") as myfile:
    file = myfile.read().split('\n')
    cards = {}

    # Put in the dictionary the card number as key and a list of occurence and 1 as value
    for line in file:
        cardNum, occurrence = line_occurrence(line)
        cards[cardNum] = [occurrence, 1]
    
    # Add the occurrence of the copy of the cards to the value of the dictionary
    for cardNum in cards.keys():
        for e in range(cards[cardNum][1]):
            for i in range(cards[cardNum][0]):
                cards[cardNum+i+1][1] += 1
    
    # Sum the values of the dictionary
    sol = 0
    for value in cards.values():
        sol += value[1]
    print(sol)