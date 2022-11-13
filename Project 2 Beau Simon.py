'''
Beau Simon
Projec 2
Online Student - 0869416
'''

import os
import FileUtils

volunteerList = []

def readInfo (fileName):
    fileName = FileUtils.selectOpenFile("Select file to open") #asking the user to open the file they want read
    if fileName == None: #user pressed cancel
        exit()    
        
    volunteerFile = open (fileName, "r") #adding the values to a list using a loop
    for volunteer in volunteerFile:
        volunteer = volunteer.strip() 
        volunteerList.append (volunteer) #getting a list of int and not string
             
    #print (numberList) #used to test the output of my for loop
    return(volunteerList)       
         
'''
creates and fills a list with the names of the volunteers for a
month. Each line in the file will be as described. The function returns the list containing the
volunteer information.
'''

#def saveInfo (fileName, calendar):
    

'''    
writes out calendar (day and volunteer) to the
specified file in the described format. This function does not return anything.
'''

def createCalendar (numOfDays):
    calendarList = []
    for i in range(1, numOfDays):
        calendarList.append(i)
        
    return calendarList

'''    
creates and returns an empty calendar with specified
number of days.
'''


#def isDayAvailable (calendar, date):
    
'''
returns True if date is available, or does not
currently have a volunteer. Otherwise the function returns False.
'''


#def daysVolunteer (calendar, date):
    
    
'''
returns the volunteer, if date has one, otherwise
returns None.
'''


#def setVolunteer (calendar, date, name): 

'''
if date is available (no current volunteer)
name is assigned to the specified date and True is returned. If date already has an assigned
volunteer do nothing to the calendar and return False.
'''


#def removeVolunteer (calendar, date):
    
'''
removes the volunteer from date, if there was a
volunteer for that date. If there wasn’t a volunteer assigned to that date no action is taken. This
function does not return anything.
'''


#def numOfDaysVolunteering (calendar, name):
    
    
'''
returns the number of days that name is
signed up to volunteer in the month.
'''



#def daysVolunteering (calendar, name):

'''
creates and returns a list containing the days
that name is signed up to volunteer in the month. This will return a list even if name is not signed
up for any day in that month.

'''
        
#def daysStillAvailable (calendar):

'''
returns the number of days in the month that do not
have a volunteer.  

'''

#def printMonth (calendar):

'''    
this function DOES create output on the display. Print out
each day of the month and its volunteer. Ensure that the days are right justified and that the
volunteer’s names are left justified. Print an appropriate label above each column. Do not print
anything for the name if there is no volunteer for that date. Do not return anything from the
function.
'''


def main():
    
    readInfo()

    
    
main()