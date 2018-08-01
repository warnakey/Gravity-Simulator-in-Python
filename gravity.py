#!/usr/bin/python
import time
import os
import sys
from sys import platform
from IPython.display import clear_output

#Use this for cross platform clear screen.
if platform == 'linux' or platform == 'linux2':
    clear = lambda: os.system('clear')
elif platform == 'darwin':
    clear = lambda: os.system('clear')
elif platform == 'win32':
    clear = lambda: os.system('cls')
#Then call "clear()" to clear the screen.
#And call "clear_output()" to clear the contents of a cell in Jupyter Notebook

#################################################################################
                      #Example land#
#################################################################################
#run = input("Start? > ")
#mins = 0
# Only run if the user types in "start"
#if run == "start":
    # Loop until we reach 20 minutes running
#    while mins != 20:
#        print(">>>>>>>>>>>>>>>>>>>>>"), mins
        # Sleep for a minute
#        time.sleep(60)
        # Increment the minute total
#        mins += 1
    # Bring up the dialog box here
    
#gravity_on == True
    
#while gravity_on == True:
#    sec = 0
#    if sec = 
#
#
#text examples of how to clear the screen if i should want to do that for any reason
#who = input("Do you want a hug? ")
#clear()
#clear_output()
#print ("Big hugs are in your future")
#time.sleep(2)
#clear()
#clear_output()

from time import gmtime, localtime, strftime

show_gmt_time = 'print("Greenwich Mean Time: " + strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))'
show_local_time = 'print("Local Time: " + strftime("%a, %d %b %Y %H:%M:%S +0000", localtime()))'

#a stopwatch that is a prototype for a future time system
def stopwatch(seconds):
    start = time.time()
    time.process_time()    
    elapsed = 0
    while elapsed < seconds:
        elapsed = time.time() - start
        exec(show_local_time)
        print()
        print(int(elapsed))
        time.sleep(1)
        clear()
        clear_output() 

stopwatch(1)

#this is the beginning of the actual gravity simulator

while True:

    print("How many objects do you want?")

    try:
        number_of_objects = int(input())
        if number_of_objects < 1 or number_of_objects > 5:
            raise ValueError #this will send it to the print message and back to the input option
            continue
    except ValueError:
        print("\nInvalid selection. The number must be between 1-5.\n")
        print()
        continue

    num_done = 0
    
    print("\nHere we are\n")

    while num_done < number_of_objects:
        x = number_of_objects
        for i in range(x):
            print(f"What is the mass of object {i}?")
            object = "mass_object_" + str(i)
            print(object)
            input()
            print()
        break
    
    starting_points_defined = 0
        
    while starting_points_defined < number_of_objects:
        x_pos = 0
        y_pos = 0
        z_pos = 0
        o = number_of_objects
        
        positionlist = []
        name_and_positionlist = []
        
        for i in range(o):
            print(f"What is the starting position on the x axis of object {i}?")
            xobject = "xobject_" + str(i)
            print(xobject)
            start_pos_xaxis = input()
            positionlist.append(start_pos_xaxis) # add input to the list
            start_pos_xaxis = name_and_positionlist.insert(0, xobject)
            name_and_positionlist.append(start_pos_xaxis) # add input to the list
            print()
            print(f"What is the starting position on the y axis of object {i}?")
            yobject = "yobject_" + str(i)
            print(yobject)
            start_pos_yaxis = input()
            positionlist.append(start_pos_yaxis) # add input to the list
            start_pos_yaxis = name_and_positionlist.insert(0, yobject)
            name_and_positionlist.append(start_pos_yaxis) # add input to the list
            print()
            print(f"What is the starting position on the z axis of object {i}?")
            zobject = "zobject_" + str(i)
            print(zobject)
            start_pos_zaxis = input()
            positionlist.append(start_pos_zaxis) # add input to the list
            start_pos_zaxis = name_and_positionlist.insert(0, zobject)
            name_and_positionlist.append(start_pos_zaxis) # add input to the list
            print()     
        
        print("These are the coordinates for the bodies of your system:")
        #FIX THIS so each object appears in its own list inside the positionlist list because it is confusing right now
        print(positionlist)
        #FIX THIS! I want this to look like this ['object1', '2', '11', '45']
        #print(name_and_positionlist)
        print()
        break        
        
    break
        
print("End")