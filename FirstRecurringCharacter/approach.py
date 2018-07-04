from collections import Counter


def approach_1(inputString):
    # Loop over the characters in the string and have an automatic counter
    # The counter start at 0
    for i, char in enumerate(inputString):
        # The recurring character is found when
        # another similar character is found in the list
        if char in inputString[i + 1:]: #[i+1:] : from i+1 to the end of list
            print("The first recurring character is",char)
            break
    # If no recurring character is found
    else:
        print("No recurring character!")


def approach_2(inputString):
    # Count objects in the string
    # by using subclass of dictionary
    charCounter = Counter(inputString)
    # Loop over the characters in the string and have an automatic counter
    # The counter start at 0
    for i, char in enumerate(inputString):
        # The recurring character is found when the count is bigger than 1
        if charCounter[char] > 1:
            print("The first recurring character is",char)
            break
    # If no recurring character is found
    else:
        print("No recurring character!")


def approach_3(inputString):
    sampleSet = set() #Create a set
    # Loop over the characters in the string and have an automatic counter
    # The counter start at 0
    for i, char in enumerate(inputString):
        # The recurring character is found when
        # there is another similar character in the set
        if char in sampleSet:
            print("The first recurring character is",char)
            break
        # The character is stored into the set
        # when there is no any instances of the character
        # to use for checking the recurring character
        else:
            sampleSet.add(char)
    # If no recurring character is found
    else:
        print("No recurring character!")