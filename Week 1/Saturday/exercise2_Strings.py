#Lowercase a String
string = "My name is Brendon"
lowercaseString = string.lower()
print lowercaseString

#Uppercase a String
string = "My name is Brendon"
uppercaseString = string.upper()
print uppercaseString

#Capitalize a String
string = "My name is Brendon"
capitalString = string.title()
print capitalString

#Reverse a String
string = "My name is Brendon"
reverseList = []
newString = ''
for x in range(len(string)-1, -1, -1):
    reverseList.append(string[x])
for index in range(len(reverseList)):
    newString = newString + reverseList[index]
print newString

#LeetSpeak
wordsToTranslate = raw_input("What do you want me to translate to LeetSpeak? ").upper()
leetTranslation = []
leetString = ''
for x in range(len(wordsToTranslate)):
    if wordsToTranslate[x] == 'A':
        leetTranslation.append('4')
    elif wordsToTranslate[x] == 'E':
        leetTranslation.append('3')
    elif wordsToTranslate[x] == 'G':
        leetTranslation.append('6')
    elif wordsToTranslate[x] == 'I':
        leetTranslation.append('1')
    elif wordsToTranslate[x] == 'O':
        leetTranslation.append('0')
    elif wordsToTranslate[x] == 'S':
        leetTranslation.append('5')
    elif wordsToTranslate[x] == 'T':
        leetTranslation.append('7')
    else:
        leetTranslation.append(wordsToTranslate[x])

for index in range(len(leetTranslation)):
    leetString = leetString + leetTranslation[index]
print leetString

#Long-long Vowels     
