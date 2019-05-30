import math

dictionary = open('dictionary.words').read().splitlines()
newDictionary = []
words = []

for word in dictionary:
    sortedWord = ''.join(sorted(word.lower()))
    wordList = [sortedWord, word]
    newDictionary.append(wordList)
newDictionary.sort()

letters = input("What letters do you see?\n-(For 'Qu' type 'q' or 'Q')\n ")
letters = list(letters.lower())
if 'q' in letters:
    letters.append('qu')
    letters.remove('q')
sortedLetters = sorted(letters)

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
                tempList = target.copy()
                tempString = arr[index][0][:]
                count = 0
                for i in range(len(tempString)):
                    for j in range(len(tempList)):
                        if tempString[i] == tempList[j]:
                            count += 1
                            tempList.pop(j)
                            break
                        elif tempString[i] == 'q' and 'u' in tempString and 'qu' in tempList:
                            count += 2
                            tempList.remove('qu')
                            tempString.replace('u', '')
                            break
                if (count == len(arr[index][0])) and not(any(arr[index][1] in sublist[1] for sublist in words)):
                    points = 1
                    for letter in arr[index][0]:
                        if letter in ['c', 'f', 'h', 'l', 'm', 'p', 'v', 'w', 'y']:
                            points += 2
                        elif letter in ['j', 'k', 'q', 'x', 'z']:
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
