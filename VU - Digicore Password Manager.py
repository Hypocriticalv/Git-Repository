#Filename: VU - Digicore Password Manager | Author: Vimal Balamurugan - s8125487
#Script Purpose: To provide a password manager to store user credentials and view them.
#Development Date Start: 22/04/2024 | Development Date End: 23/04/2024

#check if user entry exists

# Module Imports
import os
import time
import getpass

def exit_program():  #function to exit program
    delay()
    print('\nThanks for using the Digicore Password Manager. \n\nExiting the program now..') 

def remove_user_info(): #function to delete user data
    if os.path.exists('passFile.txt'):
                os.remove('passFile.txt')
                print('\nData has beens successfully deleted.')
                menu_return()
    else:
        print('\nData does not exist, please add user information.')
        menu_return()

def view_user_info():   #function to view user data
    if os.path.exists('passFile.txt'): #checks validation if file exists
                print('Gathering information now..\n')
                with open('passFile.txt', 'r') as passFile: #opens text file in read only and displays user credentials
                    print(passFile.read())
                    menu_return()
    else:
        print('\nThis file does not exist. Please enter user data.')
        menu_return()

def add_user_info():  #function to add data
    with open('passFile.txt', 'a') as passFile: #creates text file if it doesn't exist, adds data without overwriting
                user = input('Please enter your username: ') 
                while True:
                    password = getpass.getpass('Please enter your password: ') 
                    if len(password) < 8:
                        print('Please enter atleast 8 digits for your password.')
                    else:
                        break
                email = input('Please enter the name or URL, to where these credentials belong: ')
                passFile.write(f'\n====== {email} ======\nUsername: {user}\nPassword: {password} \n')
                print('User data has been successfully added.') 
                menu_return() 

#offers return to menu or exit program after viewing
def menu_return():
    while True:
        menu_return = str(input('\nWould you like to return to the main menu? (y/n): \n')) 
        if menu_return.lower() == 'y':
            clear()
            menu()
            break
        elif menu_return.lower() == 'n':
            print('Thanks for using the Digicore Password Manager. \nExiting the program now..')
            exit()
        else:
            print('Invalid input. Please choose y or n.')
            continue
            

def delay():
    return time.sleep(0.75)

#function to clear screen after menu input
def clear():
    if os.name == 'nt':
        os.system('cls') 
    else:
        os.system('clear') #for linux os 

#Main menu presents the user with options, contained within function to recall
def menu():
    print('         DIGICORE PASSWORD MANAGER         ') 
    print('----------------------------------------\n')
    print('''1. Add User Information\n2. View User Information\n3. Delete User Information\n4. Exit\n
----------------------------------------''')

def main():  #defining main function for clarity
    menu()
    while True:
        user_input = input('Please choose an option from the menu above: ') #User input to choose 1 of 3 options
        try:
            user_input = int(user_input) #casting input to integer 
            if user_input == 1:
                add_user_info()
            elif user_input == 2:
                view_user_info()
            elif user_input == 3:  #if file exists, gives option to delete data
                remove_user_info()
            elif user_input == 4: #offers option to exit program
                exit_program()
                break
            else:
                print('Invalid option, please choose option 1, 2, 3 or 4.')
        except ValueError:
            print('Invalid input. Please enter number 1, 2, 3 or 4.') #exceptions for inputs other than menu options
        except Exception as e:
            print(f'An error occurred: {e}') #exceptions for unexpected errors
        except FileNotFoundError:
            print('Please create a file before attempting to view user credentials.')
        except TypeError:
            print('Please create a file before attempting to view user credentials.')

if __name__=='__main__':
     main()







    
    
