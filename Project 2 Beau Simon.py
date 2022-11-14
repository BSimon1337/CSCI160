'''
Beau Simon
Projec 2
Online Student - 0869416
'''

import os
import FileUtils

def readInfo (fileName):
    volunteerList = []
    volunteerFile = open (fileName, "r") #adding the values to a list using a loop
    for volunteer in volunteerFile:
        volunteer = volunteer.strip() 
        volunteerList.append (volunteer) 
             
    
    return(volunteerList)       
         

def createCalendar (numOfDays):
    calendarList = [None]*numOfDays
        
    return calendarList


def saveInfo (fileName, calendar):
    outFile = open (fileName, "w")
    for i in range(len(calendar)):
        volunteer = ""
        if calendar[i] != None:
            volunteer = (" " + calendar[i])
        outFile.write (str(i+1)+ volunteer+ "\n")
    outFile.close()

def isDayAvailable (calendar, date):
    if calendar[date-1] == None:
        return True
    else:
        return False


def daysVolunteer (calendar, date):
    return calendar[date-1]



def setVolunteer (calendar, date, name): 
    if isDayAvailable(calendar, date):
        calendar[date-1] = name
        return True
    else:
        return False
    


def removeVolunteer (calendar, date):
    if isDayAvailable(calendar, date) == False:
        calendar[date] = None
        


def numOfDaysVolunteering (calendar, name):
    totalDays = 0
    for volunteer in calendar:
        if volunteer == name:
            totalDays += 1
    return totalDays



def daysVolunteering (calendar, name):
    volunteerDates = []
    for i in range(len(calendar)):
        if calendar[i] == name:
            volunteerDates.append(i+1)
            
    return volunteerDates

        
def daysStillAvailable (calendar):
    openDays = 0
    for volunteer in calendar:
        if volunteer == None:
            openDays += 1
    return openDays    


def printMonth (calendar):
    formatStr = "{:>4} {}"   
    print (formatStr.format("Date", "Volunteer"))
    
    for i in range(len(calendar)):
        volunteer = ""
        if calendar[i] != None:
            volunteer = calendar[i]
            
        print(formatStr.format(i+1, volunteer))




def main():
    
    volunteers = readInfo("volunteers.txt")
    #print(volunteers)
    
    calendar = createCalendar(31)
    #print(calendar)
    
    setVolunteer(calendar, 12, volunteers[3])
    setVolunteer(calendar, 12, volunteers[2])
    
    printMonth(calendar)
    saveInfo("calendar.txt", calendar)

    
    
    
main()