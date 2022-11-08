'''
Beau Simon
beau.a.simon@und.edu
Online student
Program 9 - Part 2
'''

#parts = {} #global dictionary

def readParts (fileName):
    parts = {}
    inFile = open (fileName, "r")
    for line in inFile:
        line = line.strip()
        part, partPrices = line.split("\t")
        parts[part] = partPrices
    inFile.close()
    return parts

def totalParts(theDictionary):
    totalParts = 0
    for i in theDictionary:
        totalParts += 1
    return totalParts

def priceList(theDictionary):
    priceList = ()
    for part, price in theDictionary:
        theDictionary[part] = float(price)
        priceList.append(price)
    return priceList

        

   

def printParts (theDictionary):
    priceWidth = 5
    for part in theDictionary:
        if len(theDictionary[part]) > priceWidth:
            priceWidth = len(theDictionary[part])
    priceWidth = priceWidth + 3    
    formatStr = "%-10s %-" + str(priceWidth) + "s|"    
    print (formatStr  % ("Part", "Price"))
    for part in theDictionary:
        print (formatStr % (part, theDictionary[part]))
    print()        


      






      





def main():

    fileName = "parts.txt"
    parts = readParts (fileName)  
    

    priceList(parts)
    print("The number of parts is: ", totalParts(parts))
    printParts (parts)


main()