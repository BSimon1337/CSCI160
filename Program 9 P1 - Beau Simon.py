'''
Beau Simon
beau.a.simon@und.edu
Online student
Program 9 - Part 1
'''


#parts = {} #global dictionary


def loadParts (fileName):
    parts = {}
    inFile = open (fileName, "r")
    for line in inFile:
        line = line.strip()
        part, partPrices = line.split("\t")
        parts[part] = partPrices
    inFile.close()
    return parts


def addParts (parts):
    partToAdd = input ("Enter new part ")
    while partToAdd != "":
        priceToAdd = input("Enter price for " + partToAdd + " ")
        if not partToAdd in parts:
            parts[partToAdd] = priceToAdd
        else:
            response = input (partToAdd + " exists in parts - overwrite [y/n]? ")            
            if response.lower().strip()[0] == 'y':
                parts[partToAdd] = priceToAdd
                print ("Parts updated")
            else:
                print ("Update cancelled")
        print()
        partToAdd = input ("Enter next new part ")

def saveParts (fileName, parts):
    outFile = open (fileName, "w")
    for part in parts:
        outFile.write (part)
        outFile.write ("\t") #delimiter between values
        outFile.write (parts[part])
        outFile.write ("\n")  #end of line/record 
    outFile.close()


def main():
    
    fileName = "parts.txt"
    parts = loadParts (fileName)    
    
    addParts (parts)
    saveParts(fileName, parts)
    
    
main()