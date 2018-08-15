Gravity Simulator
-----------------

A gravity simulator in python

Version 1.2 released August 15, 2018 at 1:00am
+ Improved and simplified the program so that x y z coordinates can be inputted from 1 line (instead of 3)
+ Made it so the program cannot be broken by failing to enter 3 numbers in the 1 line inputs for x y z coordinates
+ Made it so that the program cannot be broken by entering in a wrong data type anywhere (such as a string where an integer is expected)
+ Added function strings in more places
+ Set a limit for the mass of objects
+ Bolded the headings of the table outputs
+ Added an option at the end to either run the program again or end it

Version 1.1 released August 14, 2018 at 12:30am
+ Updated Gravity Simulator to actually do something useful!
+ Removed tons of useless code
+ Made the program output a usable table of x, y & z coordinates that can be used to plot the location of the objects in the system
+ Right now the part of the program that asks for mass for each object is not being put to use. It will eventually be used to calculate gravity.
+ It took me two weeks to figure out how to export the data in a usable format.

Version 1.0 released August 1, 2018 at 2:30am
+ Initial commit
+ Allows you to enter a number of objects (between 1 and 5), enter their mass, then enter their x, y and z coordinates in space
+ After giving all inputs the program outputs the data in a list
+ Several bugs currently exist that need to be fixed, such as all coordinates data for all objects being stored into 1 list (super confusing) and right now it is not possible to enter decimals (floating point numbers), only integers (whole numbers)
+ Several optimizations need to be made including removing duplicate code, removing excess comments and completing a few concepts
+ In the future we will have a GUI and a visual representation of the objects interacting with each other as if they were planets in space
+ Future possibilities include collision detection, the ability for objects that touch to combine and gain mass or a game functionality
