import math

dictionary = open('dictionary.words').read().splitlines()
newDictionary = []
words = []
indexes = []

for word in dictionary:
    sortedWord = ''.join(sorted(word.lower()))
    wordList = [sortedWord, word]
    newDictionary.append(wordList)
newDictionary.sort()

letters = input("Letters: ")
sortedLetters = ''.join(sorted(set(letters.lower())))

def search(arr, l, r, target):
    while l <= r:
        mid = int((l+r) / 2)
        if arr[mid][0][0] == target[0]:
            index = mid
            while arr[index][0][0] == target[0]:
                index -= 1
                if index < 0:
                    break
            index += 1
            while arr[index][0][0] == target[0] and arr[index][0][1] <= target[len(target)-1]:
                tempString = target[:]
                count = 0
                for i in range(len(arr[index][0])):
                    for j in range(len(tempString)):
                        if arr[index][0][i] == tempString[j]:
                            count += 1
                            tempString = tempString[:j] + tempString[j+1:]
                            break
                if count == len(arr[index][0]) and arr[index][1] not in words:
                    points = 0
                    for letter in arr[index][0]:
                        if letter in ['c', 'f', 'h', 'l', 'm', 'p', 'v', 'w', 'y']:
                            points += 2
                        if letter in ['j', 'k', 'q', 'x', 'z']:
                            points += 3
                        else:
                            points += 1
                    points *= points
                    words.append([points, arr[index][1]])
                index += 1
                if index >= len(arr):
                    break
            return index
        elif arr[mid][0][0] < target[0]:
            l = mid + 1
        else:
            r = mid - 1
    return -1

newLetters = sortedLetters

while len(newLetters) >= 3:
    result = search(newDictionary, 0, len(newDictionary)-1, newLetters)
    newLetters = newLetters[1:] 

if words != []:
    words.sort(reverse = True)
    print("Best Five: ")
    for index in range(5):
        print(str(words[index][0]) + " points -  " + words[index][1])
else:
    print("No words found")
