import time
print('Alex Binns')

# Variable to store the start time so the program time can be calculated
startTime = time.time()

# Initiate dictionary for the words to be inserted
anagramDict = {}

# Precondition:
# I have a an input file of a list of words

# Loop Invariant:
# For each word that is processed the correct key has been found and it is put in the dictionary as either a new entry
# or if the key already exists then it is added to the list for that key. All words that have been processed are in the
# correct place in the dictionary

with open('words.txt') as inputFile:
    # Iterate over the words in the file
    for word in inputFile:
        # Each word is rearranged alphabetically and the new line character is removed
        alphabeticalWord = ''.join((sorted(word))).strip()
        # Check if key is in dictionary if so add word to existing key if not create new entry
        if alphabeticalWord in anagramDict:
            anagramDict[alphabeticalWord].append(word.strip())
        else:
            anagramDict[alphabeticalWord] = [word.strip()]

# Post condition:
# All the words have been read and are in the dictionary in the list associated with the correct key.

# Precondition:
# I have a correct dictionary

#Loop Invariant:
# For each key that is so far processed if there is more than one item in the list associated with that key then the
# list has been added to the new list.

# Initilize a list for the words that have another word that is an anagram
anagramList = []
# Iterate through all keys in the dictionary and check if the value list is longer than 1 word if so then it is added
# to the new list
for keys in anagramDict:
    if len(anagramDict[keys]) > 1:
        anagramList.append(anagramDict[keys])

# Pre condition:
# List of lists of anagrams

# Loop invariant:
# Used the built in function to sort the list in size of number of items in the list
anagramList.sort(key=len, reverse=True)

# Precondition:
# List of anagram classes sorted by length

# Loop Invariant:
# For each item that is processed then the list has been displayed
for item in anagramList:
    print(item)

# Post condition:
# All anagram classess have been printed in order

# Print the time the algorithm took to complete.
print("The program took {!s} seconds" .format(time.time() - startTime))