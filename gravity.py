#!/usr/bin/python

print("This tool will output a table of data containing the x, y and z coordinates of up to 5 objects.\n\n")

while True:
    
# ENTER HOW MANY OBJECTS IN SYSTEM ----------------------------------------------------------------------------

    print("How many objects do you want?")

    try:
        number_of_objects = int(input())
        print()
        if number_of_objects < 1 or number_of_objects > 5:
            raise ValueError                        # this will send it to the print message and back to the input option
            continue
    except ValueError:
        print("\nInvalid selection. The number must be between 1-5.\n")
        print()
        continue
        
    print("There are " + str(number_of_objects) + " objects in your system.")
    
    # create names for the objects
    x = number_of_objects
    for i in range(x):
        i = i+1
        object = "object " + str(i)
        # print the object names. I want to store them as variables though. Not sure how.
        print(object)
        #i = i-1
        
    print("\n----------------------------\n")
    
    
# ENTER MASS OF OBJECTS IN SYSTEM ----------------------------------------------------------------------------

    num_done = 0
    
    while num_done < number_of_objects:
        x = number_of_objects
        for i in range(x):
            i = i+1
            print(f"What is the mass of object {i}?")
            object = "mass_object_" + str(i)
            int(input())
            print()
        break
        
    print("\n----------------------------\n")
    
    
# ENTER XYZ COORDINATES OF OBJECTS IN SYSTEM -----------------------------------------------------------------
        
    starting_points_defined = 0
    
    while starting_points_defined < number_of_objects:
        
        # Define starting coordinate variables 
        x_pos = 0
        y_pos = 0
        z_pos = 0
        o = number_of_objects
        
        # these are the lists we will need
        all_xyz_values = []                                     # this will be ALL x y z values in a big list
        name_and_coords = []                                    # output should look like ["object 1", 23, 34, 45]
        names_of_xyz_coord_lists = []                           # list of names of the xyz coord lists
        
        # Start a loop that creates a list of xyz coords for each object
        for i in range(o):
            i = i+1
            
            coord_lst = "coord_lst_" + str(i)                   # name the current xyz coord list
            names_of_xyz_coord_lists.append(coord_lst)          # make a list of the names of the xyz coord lists
            
            
# X COORDINATES --------------------------------------------------------------------------------------

            print(f"What is the starting position on the x axis of object {i}?")
            
            #xobject = "xobject_" + str(i)                      # create a name for the x value of the current object
            #object_names.append(xobject)                       # add name of each x value to a list (just in case?)
            
            start_pos_xaxis = int(input())                      # where the x value is actually inputted by the user
            
            all_xyz_values.append(start_pos_xaxis)              # add x input to a list of all xyz coord values
            
            print()
            
            
# Y COORDINATES --------------------------------------------------------------------------------------
            
            print(f"What is the starting position on the y axis of object {i}?")
            
            #yobject = "yobject_" + str(i)                      # create a name for the y value of each object
            #object_names.append(yobject)                       # add y input to the list
            
            start_pos_yaxis = int(input())                      # where the y value is actually inputted by the user
            
            all_xyz_values.append(start_pos_yaxis)              # add y input to a list of all xyz coord values       
            
            print()
            
            
# Z COORDINATES --------------------------------------------------------------------------------------
            
            print(f"What is the starting position on the z axis of object {i}?")
            
            #zobject = "zobject_" + str(i)                      # create a name for the z value of each object
            #object_names.append(zobject)                       # add z input to the list
            
            start_pos_zaxis = int(input())                      # where the z value is actually inputted by the user
            
            all_xyz_values.append(start_pos_zaxis)              # add Z input to a list of all xyz coord values 
            
            
# CLEAN UP A FEW THINGS --------------------------------------------------------------------------------
            
            # all starting points (xyz coords) for current object have been defined, therefore, add 1 to value
            starting_points_defined = starting_points_defined+1
            
            # earlier I made the i integer in the loop +1, so this is just so the loop doesn't get screwy (i think)
            i = i-1
            
            print("\n----------------------------\n")
                     
            
# OUTPUT THE RESULT --------------------------------------------------------------------------------------
    
        print("\n########################################################################################\n\n")
        print("These are the coordinates for the bodies of your system in table layout:\n")
        
        xyz_output = all_xyz_values
        
        print("\nObject Name | X | Y | Z ")
         # printing the list using loop
        for x in range(number_of_objects):
            x = x+1
            
            final_output = "object " + str(x) + " | " + str(xyz_output[0]) + " | " + str(xyz_output[1]) + " | " + str(xyz_output[2])
            
            print(final_output)
            for e in range(2):
                #popping brings the last value from the previous list to the first value of the next list, which is bad
                #all_xyz_values.pop(0)
                del xyz_output[:3]
                break
            x = x-1
            
        print("\n\n########################################################################################\n\n")
        
        break
        
    break

# END --------------------------------------------------------------------------------------

print("\n\nEnd")
