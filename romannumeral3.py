#romathing2.py
#ICS3U
#Feburary 9, 2021

#I should either start with getting a user input for the number or i should find a way to correlate values.

romanNumerals = {

    1: 'I',

    5: 'V',

    10: 'X',

    50: 'L',

    100: 'C',

    500: 'D',

    1000: 'M',

}
while True:

    userNumber = 0


    def numbercheck(aChar):

        userNumber = input("Please enter a number from 1 - 3999: ")
                                                                                        #   Grabs an input from the user, makes sure its actually
        if userNumber.isdigit() == True:                                                #   a number and if it isnt, it runs again.
            return int(userNumber)                                                      #   also returns the new number in int() instead of str()
        while userNumber.isdigit() != True:
            userNumber = input("Enter a valid number: ")

        return int(userNumber)

    def lessthan(aNumber):
        while True:

            if aNumber < 4000 and aNumber > 0:                                          #   this runs a loop that checks if the number from numbercheck()
                return aNumber                                                          #   is actually capaable of being a roman numeral, so 1 - 3999
                                                                                        #   If it isn't, it will run numbercheck() until a valid int is entered
            else:
                aNumber = numbercheck(aNumber)
                continue

    def makingsure(theNumber):
        theNumber = numbercheck(theNumber)                                              #   Just puts the other two functions into one so it looks cleaner when
        theNumber = lessthan(theNumber)                                                 #   it's all said and done lol
        return theNumber                                                                #   don't know if this is bad practice

    newNumber = makingsure(userNumber)

    newNumblist = []
    numblist2 = []


    strNumb = str(newNumber)
    lenofNumb = len(strNumb)

    for i in range(lenofNumb):
        newNumblist.append(strNumb[i])                                                  #   This will be used to check the value of a digit column
                                                                                        #   (1000's, 100's, 10's, 1's)
                                                                                        #   <---- appends newNumber to a list
    for i in range(4 - lenofNumb):
        newNumblist.insert(i, 0)                                                        #   Makes sure each digit is always in the right column


    def digitMulti(aList, appendList):                                                  #   This function will multiply and separate
                                                                                        #   newNumblist into separate components
        num1 = int(aList[0]) * 1000                                                     #   can confirm it works like this - remember that its
        num2 = int(aList[1]) * 100                                                      #   an int() and not a str()
        num3 = int(aList[2]) * 10
        num4 = int(aList[3])

        appendList.append(num1)
        appendList.append(num2)
        appendList.append(num3)
        appendList.append(num4)

    def makeromanXX(list, lt1, lt2, lt3, lt4, lt5, lt6):                                #   This will make it easier to change the strings inside of the
                                                                                        #   list. So like now i can just swap out the letters i want
        for i in range(1, 11):                                                          #   which i think is pretty cool lol
            list[i] = list[i].replace(lt1, lt2)

        for i in range(1, 11):
            list[i] = list[i].replace(lt3, lt4)

        for i in range(1, 11):
            list[i] = list[i].replace(lt5, lt6)


    romanVX = [None, 'a', 'aa', 'aaa', 'ab', 'b', 'ba', 'baa', 'baaa', 'ac', 'c']

    romanLC = [None, 'a', 'aa', 'aaa', 'ab', 'b', 'ba', 'baa', 'baaa', 'ac', 'c']

    romanDM = [None, 'a', 'aa', 'aaa', 'ab', 'b', 'ba', 'baa', 'baaa', 'ac', 'c']

    makeromanXX(romanVX, 'a', 'I', 'b', 'V', 'c', 'X')
    makeromanXX(romanLC, 'a', 'X', 'b', 'L', 'c', 'C')
    makeromanXX(romanDM, 'a', 'C', 'b', 'D', 'c', 'M')


    def outRoman(aList):                                                                #   Should take the list input, and spit out the right index of
                                                                                        #   a romanXX index.
        intthem1 = int(aList[0])                                                        #
        intthem2 = int(aList[1])                                                        #   The whole function should now take a value from aList,
        intthem3 = int(aList[2])                                                        #   and then take the corresponding roman numeral and append it to
        intthem4 = int(aList[3])                                                        #   last list which is the return value
                                                                                        #
                                                                                        #
        lastlist = []                                                                   #
                                                                                        #
        if intthem1 != 0:                                                               #
            lastlist.append(intthem1 * 'M')                                             #

        lastlist.append(romanDM[intthem2])
        lastlist.append(romanLC[intthem3])
        lastlist.append(romanVX[intthem4])

        return lastlist



    finalthing = outRoman(newNumblist)
    anotherlist = [x for x in finalthing if x != None]


    s = ""
    s = s.join(anotherlist)


    print("\n            ", newNumber, "in Romam Numerals is ------>>>>>>>>   ", s, "   <<<<<<<<------")

    usrinput = input("1 to repeat, 0 to leave: ")

    continue
