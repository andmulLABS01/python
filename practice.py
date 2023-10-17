print("Hello World")

def thisMeansTen():
    print(10)

thisMeansTen()


def ThisMeansTenV2():
    return 100


ThisMeansTenV2()


def getUserInput():
    someName = input("whats your name?")
    return someName


#print("Your name is: " , getUserInput())

def getUserInputV2(someName, someAge):
    print("Your name is: " + someName + " and your age is: " + str(someAge))


getUserInputV2("AJ", 9)

#Imagine you are a teacher and need to write a function that takes in a list of test scores
#and outputs the average

def averageTestScores(someList):
    average = 0.0

    for i in range(0, len(someList)): 
        average = average + someList[i]
        
    average = average / len(someList)



    print(average)



scores = [100.0, 78.5, 88.9, 65.4, 95.8, 86.3, 99.9]
averageTestScores(scores)


def averageTestScoresV2(someList):
    average = 0.0

    for element in someList: 
        average = average + element
        
    average = average / len(someList)



    print(average)


averageTestScoresV2(scores)


#if you had a list of names, how would you print the last name of the list

print(scores[6])
print(scores[len(scores) - 1])

#make a function called sameFirstLast, it should take in a list of intergers and ouptut
#yes if the first and last element are the same and no if not

def sameFirstLast(someList):
    if scores[0] == scores[len(scores) - 1]:
        print("yes")
    else:
        print("no")

sameFirstLast(scores)

#extra function practice 
#make a function called removeVowles, its input will always be a string
#your function should return string given but without any owles inside of it

def removeVowles(someString):
    vowles = ['a', 'e', 'i', 'o', 'u']
    
    for x in someString:
        if x.lower() in vowles:
            someString = someString.replace(x, '')
    return someString

someString = "We will not gO quietly into the night!"
print(removeVowles(someString))

#Frank example

def removeVowlesV2(word):

    newList = list(word)

    while("a" in newList):
        currentI = newList.index("a")
        newList.pop(currentI)

    while("e" in newList):
        currentI = newList.index("e")
        newList.pop(currentI)

    while("i" in newList):
        currentI = newList.index("i")
        newList.pop(currentI)

    while("o" in newList):
        currentI = newList.index("o")
        newList.pop(currentI)

    while("u" in newList):
        currentI = newList.index("u")
        newList.pop(currentI)

newString = ""
#take this list and convert it back into a string
#concatenation! use index psotions
for i in range(len(newList)):
    #concatenate!
    newString = newString + newList[i]

    return newString


# def revoveChar(someChar, someList):
#     while(someChar in somelist):
#         currentI = someList.index(someChar)
#         newList.pop(currentI)
#     return someList

# def removeVowlesV3(word):

#     newList = list(word)

#     newList = removeChar("a", newList)
#     newList = removeChar("e", newList)
#     newList = removeChar("i", newList)
#     newList = removeChar("o", newList)
#     newList = removeChar("u", newList)

# newString = ""
# #take this list and convert it back into a string
# #concatenation! use index psotions
# for i in range(len(newList)):
#     #concatenate!
#     newString = newString + newList[i]

#     return newString