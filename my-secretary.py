# simple-biginner-to-do-organiser
from time import *

# function to write items to the dictionary
def dict_write(event, time):
    schedules[event] = time
    
# function to view items in the dictionary
def dict_view():
    print("Loading data...")
    sleep(2)
    print("\nYour schedules appear here.\n")
    for key in schedules.keys():
        for item in schedules.values():
            print(key, end = " at ")
            print(item)
    
# function to clear all dictionary data after 24 hours (1 day)
def dict_clear():
    if strftime("%H:%M %p") == ("23:59 PM"):
        schedules.clear()
   
# function to print saving
def print_save():
   # if user_choice == 2:
   sleep(0.5)
   print("Saving.")
   sleep(0.5)
   print("Saving..")
   sleep(0.5)
   print("Saving...")
   print("Event Saved.")
 
#program title

print("*" *60)
print("_" *60)
print("|" * 60, end = "|")
print("=" * 14, end = ">")
print(" " *6, end = "")
print("MY TO-DO ORGANIZER", end ="")
print(" " * 6, end = "<")
print("=" * 12, end = "|")
print("|" * 60)
print("-" *60)
print("*" *60)

# get user info , welcome user and give user options to choose from
name = input("\vHello, what is your name: ", )
cap_name = name.upper()

print("\nLoading, please wait...")
sleep(0.5)#delay processing for some time

print(f"\vWelcome {cap_name}, please choose an option below")
print("\n1) Schedule event.\n2) Done.\n3) View Schedule ")

# getting user input on the above choices
user_choice = int(input(">>> "))

#dictionary to storr user schedules
schedules = dict()

#if statement to check if user_choice is in range with in the choices
if user_choice not in range(1, 4):
    raise ValueError
# loop to keep iterating to get user event input
# loop ends when user suggests s\he is done filling in events
while user_choice != 2:
    if user_choice == 1:
        print("\n")
        print("(" * 21, end = "     ")
        print("New Event", end = "     ")
        print(")" * 20)
        id = 1
        if id != 1000:
            event = input(f"\nEvent_{id} ")
            time = input("Time: ")
            id += 1
            dict_write(event, time)
         
        # user has to be asked whether s\he wants to continueadding schedules, save current data or view saved schedules       
        prompt_save = int(input("\n1)Continue \n2)Done \n3) View Schedules"))
        if prompt_save == 2:
            #  getting user choise to save 
            user_choice2 = input("\nSaved ")
            break
        elif prompt_save == 3:
            dict_view()
            break
          
#conditions if  user choice  not == 1
#conditioning for user choices for choice 2 and choice 3
if user_choice == 3:
    dict_view()
