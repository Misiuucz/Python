# First input is a count of words
# Every next input will be a word from the list

# Example input:
# 3
# AAEEEOOO
# AEO
# ELOOO
# Output:
# A2E3O3
# AEO
# ELO3

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


a = input('Podaj liczbe słów: ')
a = int(a)

StringArray = []

for i in range(0,a):
    b = input("Insert "+str(i+1)+ " word: ")
    StringArray.append(b)

for i in range(0,a):
    print(cutWord(str(StringArray[i])))
#    
