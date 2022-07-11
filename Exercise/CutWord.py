# The first input asks for number of words
# Every next input should be a word which contains only letters
# Output will give us word back, but if it contains at least 2 same letters in a row, it will return letter and it's count

# For example:
# Input:
# 3
# word
# wooordddd
# hooolooogram

# Output:
# word
# wo3rd4
# ho3lo3gram

def cutWord (word):
    
    count = 1
    charlist = list(word)
    newString = str(charlist[0])
    
    for i in range(1,(len(charlist))):
        
        if (charlist[i] == charlist[i-1] ):
            count = count + 1
        
        else:                       #Jeżeli nie
            
            if (count == 1):
                newString = newString + str(charlist[i])
            
            else:
                newString = newString + str(count)
                newString = newString + str(charlist[i])
                count = 1
    if (count != 1):
        newString = newString + str(count)
    return str(newString)


a = input('How many words? - ')
a = int(a)

StringArray = []

for i in range(0,a):
    b = input("Insert "+str(i+1)+ " word: ")
    StringArray.append(b)

for i in range(0,a):
    print(cutWord(str(StringArray[i])))
#    
