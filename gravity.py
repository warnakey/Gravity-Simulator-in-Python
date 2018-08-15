#!/usr/bin/python

while True:
    print("This tool will output a table of data containing the x, y and z coordinates of up to 5 objects.\n\n")
    
    # ENTER HOW MANY OBJECTS IN SYSTEM
    try:
        number_of_objects = int(input("How many objects do you want? "))
        if not 1 <= number_of_objects <= 5:
            raise ValueError                # this will send it to the print message and back to the input option
    except ValueError:
        print("\nInvalid selection. The number must be between 1-5.\n\n")
        continue
    
    # show a different output if there is only 1 object
    if number_of_objects == 1:
        print("\nThere is 1 object in your system")
    else:
        print()
        print(f"There are {number_of_objects} objects in your system.")
    
    # create names for the objects
    for i in range(1, number_of_objects + 1):
        print("object", i)
        
    print("\n----------------------------\n")
    
    objects = []
    # ENTER MASS OF OBJECTS IN SYSTEM
    for i in range(1, number_of_objects + 1):
        object_info = [i]
        
        valid_mass = True
        
        while valid_mass == True:
            # enter the mass of objects and make sure the input is a number in the correct range
            try:
                mass = int(input(f"What is the mass of object {i}? "))
                if not mass >= 0 and mass <= 9999999:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("\nInvalid selection. Mass must be between 0 and 9,999,999.\n")
                continue
        
        need_starting_positions = True
        
        # loop created so it will show an error message if someone forgets to enter 3 values in the single line input
        while need_starting_positions == True:
            try:
                x, y, z = input(f"What is the starting position of object {i} in the format x y z? ").split()
                print()
                if x == "" or y == "" or z == "" or x.isdigit() != True or y.isdigit() != True or z.isdigit() != True:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("\nInvalid Selection. Please enter 3 values, like so: '3 45 500'\n")
                continue
        
        objects.append((i, mass, int(x), int(y), int(z)))
        print("\n----------------------------\n")

    # OUTPUT THE RESULT
    
    print("\n########################################################################################\n\n")
    print("These are the coordinates for the bodies of your system in table layout:\n")
    
    class style:
        bold = '\033[1m'
        end = '\033[0m'
        
    print(f"{style.bold}Object Name | X | Y | Z{style.end}")
    # printing the list using loop
    for i, mass, x, y, z in objects:
        final_output = f"object {i} | {x} | {y} | {z}"
        print(final_output)
    print("\n\n########################################################################################\n\n")
    
    # RUN THE PROGRAM AGAIN OR END IT
    
    again = True
    
    # create a loop asking if they want to run the game again. If something other than yes or no is entered it asks again.
    while again == True:
        run_again = input("Do you want to run the program again? Yes or No? ")
        run_again = run_again.lower()
    
        # run again option
        if run_again == "yes":
            print("\n----------------------------\n")
            break
        elif run_again == "no":
            break
        else:
            print("\nPlease type either 'Yes' or 'No'.\n")
    
    # once we are out of the loop asking yes or no, we then either start the program over or end it
    if run_again == "yes":
        continue
    elif run_again == "no":
        break

# END --------------------------------------------------------------------------------------

print("\n\nEnd")
