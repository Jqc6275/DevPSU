inputSentence = input("Enter a phrase to convert to pig latin:  ")
inputArray = inputSentence.split(" ")
newSentence = ''

for word in inputArray:
    if word[0] in ('a','e','i','o','u','y'):
        word += "yay"
        newSentence += word
        newSentence += ' '
    elif (word[1] in ('a','e','i','o','u','y')) and (word[2] not in ('a','e','i','o','u','y')):
         vowel = word[0]
         vowel += 'ay'
         word = word[1:]
         word += vowel
         newSentence += word
         newSentence += ' '
    else:
        vowel = word[0:1]
        vowel += 'ay'
        word = word[2:]
        word += vowel
        newSentence += word
        newSentence += ' '
print(newSentence)