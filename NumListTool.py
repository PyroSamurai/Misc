#############################################################################
#    NumListTool - python tool for a repetitive job + some comedy           #
#    Copyright (C) 2013  Sean R. Stafford                                   #
#                                                                           #
#    This program is free software: you can redistribute it and/or modify   #
#    it under the terms of the GNU General Public License as published by   #
#    the Free Software Foundation, either version 3 of the License, or      #
#    any later version.                                                     #
#                                                                           #
#    This program is distributed in the hope that it will be useful,        #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#    GNU General Public License for more details.                           #
#                                                                           #
#    You should have received a copy of the GNU General Public License      #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#                                                                           #
######################### End of copyright notice ###########################


# importing possible modules
import random
import math
import sys
import datetime
import os

# Number List Generator Introduction
def numListGenIntro(var0):
    if var0 == 'hellyeah':
        print('\nHi Master, I\'m a program that prints a list of numbers\
\nthat starts and ends at numbers you will define for me.')
        print('\nNow, let us begin, Master.')
    else:
        print('\nThank you for giving me another chance to please you, Master.')

# Function which asks the user the first and last numbers and error checks.
# Returns the first and last numbers.
def nums():
    print('\nWhat number would you like to start with, Master?', end = ' ')
    var1 = input()
    while True:
        if var1.isdigit():
            var1 = int(var1)
            break
        else:
            print('What you entered has non-digit characters in it.')
            print('Please try again, Master, so that I may serve you.')
        
    print('\nWhat number would you like the list to end with, Master?', end = ' ')
    var2 = input()
    while True:
        if var2.isdigit():
            var2 = int(var2)
            break
        else:
            print('What you entered has non-digit characters in it.')
            print('Please try again, Master, so that I may serve you.')

    return var1,var2

# List form question
# Returns form number
def getForm():
    print('\nIn what form do you wish me to print the list, Master?')
    print('To separate each number with only a space, answer with a one.')
    print('To start each number on a new line, answer with a two.')
    print('Answer:', end=' ')
    var3 = input()
    while True:
        if var3.isdigit():
            var3 = int(var3)
            break
        else:
            print('Answer with a 1 or 2 only, please.')
            print('Please try again, Master, so that I may serve you.')
            continue

    return var3

    
# The function that will take the first and last number and
# prints them and all the numbers in between in order from least to greatest
# Returns nothing
def numList(var1, var2, var3, var4):
    f = open(var4, 'r+')
    while True:
        if var1 >= var2:
            temp = var1
            var1 = var2
            var2 = temp
            print('Master, it is not nice to try to trick me.')
            print('The first and last numbers have been switched\nto their proper positions.')
        if var3 == 1 or var3 == 2:
            if var3 == 1:
                print('\nMaster, the numbers you wanted are being written to this file:\n')
                print(var4)
                print('\nPlease wait a moment...')
                for i in range(var1, (var2 - 1)):        
                    f.write(str(i)+' ')
                f.write(str(var2))
                print('           (\\_/)')
                print('...Done! (\\(^v^)/)')
                break
            if var3 == 2:
                print('\nMaster, the numbers you wanted have been written to this file:\n')
                print(var4)
                print('\nPlease wait a moment...')
                for i in range(var1, (var2 - 1)):        
                    f.write(str(i)+'\n')
                f.write(str(var2))
                print('           (\\_/)')
                print('...Done! (\\(^v^)/)')
                break
        else:
            continue
    f.close()
    return None

# Asks the user if he/she wants to use the tool again. Saves the response.
# Returns the user's response.
def use():
    print('\nWould you like to use me again, Master?\nAnswer(y/n):', end=' ')
    var0 = input().lower()

    return var0

# Creates a file if it doesn not already exist.
def touch(path):
    with open(path, 'a'):
        os.utime(path, None)
    return None


# Asks the player if they want return to the menu then reacts to his/her response.
# Returns the players response.
def keepGoing():
    var5 = '0'
    var6 = 0
    while var6 == 0:
        if not var5.isalpha():
            print('\n== Would you like to return to the main menu (y or n)?', end=' ')
            var5 = input()
        else:
            break
    var5 = var5.lower()

    return var5


######### The NumListGenMain function starts here #############################
def NumListGenMain():
    print('==                                                        ==')
    print('==  Starting Number List Generator Program......          ==')
    print('==                                                        ==')
    ans = 'hellyeah'
    while ans == 'y' or ans == 'yes' or ans == 'hellyeah':
        numListGenIntro(ans)
        first,last = nums()
        form = getForm()
        getTime = datetime.datetime.now(tz=None)
        appendTime = str(getTime.strftime("%Y-%b-%d_at_%H-%M-%S"))
        filename = 'numberList_'+ appendTime + 'sec.txt'
        touch(filename)
        numList(first, last, form, filename)
        ans = use()
    
    return ans

######### The NumListGenMain function ends here ###############################

###############################################################################    
######### The main function starts here #######################################
def main():
    ansMain = 'y'
    while ansMain == 'y': 
        inputValidation = 0
        print('============================================================')
        print('================== NumListTool Main Menu ===================')
        print('============================================================')
        print('============================================================')
        print('============================================================')
        print('==                                                        ==')
        print('==                                                        ==')
        print('==                                                        ==')
        print('== Program options for NumListTool:                       ==')
        print('==                                                        ==')
        print('== 1. Number List Generator                               ==')
        print('==                                                        ==')
        print('== 2. Exit NumListTool                                    ==')
        print('==                                                        ==')
        print('============================================================')
        while inputValidation == 0:
            print('== Please enter the number of program you want to use: ',end='')
            progOpt = input()        
            if not progOpt.isdigit():
                print('== Please input a number on the list.                     ==')
                print('==                                                        ==')
                continue
            else:
                break
        progOpt = int(progOpt)        
        if progOpt == 1:
            ansMain = NumListGenMain()
            print('\nI hope I have pleased you, Master.\nPlease come again soon.')

        else:
            print('\n\nBye bye, Master :3')

        ansMain = keepGoing()

    input('\n\n//Hit "Enter" to leave the program.//')
    return None
######### The main function ends here #########################################
###############################################################################

main()
