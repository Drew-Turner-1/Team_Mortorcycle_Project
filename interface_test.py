import sys # Importing the sys module to use sys.exit()
import time
user_path = input("enter path to data file: ")

run = True

while(run) : 
    print("press h for list of options ")
    selection = input("Enter selection: ")
    if selection == 'h' : 
        print(''' list of options: 
                1 - option 1 
                2 - option 2 
                3 - option 3 
                4 - quit ''') # Added the quit option to display.
    elif selection == "1" : 
        print("opiton 1")
    elif selection == "2" : 
        print("option 2")
    elif selection == "3" : 
        print(user_path)
    elif selection == '4' : 
        print("quitting")
        run = False
    else : 
        print("invalid selection")

time.sleep(2) # Command to wait two seconds before executing the next command (in this case, exit).
sys.exit(0) # Command to quit the program from the sys library (on the sys object created when the program runs) and raises the SystemExit exception. The "0" indicates a successful termination (no errors).