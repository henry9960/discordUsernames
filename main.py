import random

chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '_', 'a', 'b', 'c', 'd',
         'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z']

fileOutput = open('usernamesDiscord.txt', 'w')
# Outputs a file containing the randomised usernames in the same directory as the script.

for x in range(1000):  # Adjust the range for the amount of usernames to print.
    print('h', random.choice(chars), random.choice(chars), file=fileOutput)
    # Adjust the print for a specific char in a specific spot.
