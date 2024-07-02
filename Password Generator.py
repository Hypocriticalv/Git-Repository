import string
import random
import pyfiglet
import sys
import time

#Random Password Generator

def banner():
    intro_banner = pyfiglet.figlet_format('Password Generator')
    print(intro_banner)
    
def intro():
    global length
    try:
        while True:
            length = int(input('\nHow long would you like your password to be? (12-16 characters): '))
            if length < 12:
                print('\nMinimum not met, enter 12 or more characters.')
            elif length > 16:
                print('\nPlease select between 12 and 16 characters.')
            else: 
                password_generator()
                break   
    except ValueError:
        time.sleep(2)
        print('Please enter a digit between 12 and 16.')
        main() 
    
def password_generator():
    password = [] 
    
    for special in range(length - 9):
        special = random.choice(['!','@','#','$','%','*']) #needs to be contained in a list
        password.append(special)
    
    for numbers in range(length - 8):
        numbers = random.randint(0,9)
        password.append(str(numbers)) #.append gives outputs in a horizontal line
        
    for alphabet in range(length - 7):
        alphabet = random.choice(string.ascii_letters) #contains entire list of alphabet lower + uppercase
        password.append(alphabet)
        
    random.shuffle(password) #shuffles all the outputs
    
    print('\nYour password is:',f''.join(password)) #everything is joined
    while True:
        again = input('\nWould you like to create another password? (y/n): ')
        if again == 'y':
            intro()
            break
        elif again == 'n':
            print('Thanks for using the password generator!')
            break
        else:
            print('Please enter "y" or "n".')
    
        
        

def main():
    banner()
    intro()

if __name__=='__main__':
    main()
    

        


    