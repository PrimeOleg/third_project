# program that prompts the user to enter a password. 
# If the password is incorrect, prompt the user to enter the password again until they enter the correct password.

attempts = 3 # attempt counter to track how many times password was enetered wrong
password = [] # list in which the user's password will be stored, (in real case scenario dictionary would be better)

# LOOP TO ASK USER FOR THEIR REGISTERED PASSWORD
while True:
    to_register = input("Enter the password you wish to register: ")
    if to_register == "": 
        print("Please enter something\n".upper())
        continue
    else:
        password.append(to_register) # appends the password user wanted to register with
        print("Password successfully registered")
        break

# LOOP TO ASK USER TO LOGIN WITH THEIR PASSWORD
while True:
    to_login = input("Enter your password to login: ")

    # IF THE PASSWORD IS NOT MATCHED THE ATTEMPTS COUNTER IS DECREMENTED BY 1
    if to_login not in password:
        print("\nWrong password please try again")
        to_login
        attempts -= 1 # attempts = attempts - 1
    
    else:
        print("\nWelcome user logging you in...".upper())
        break

    # CHECKS IF THE ATTEMPT COUNTER IS 0 AND BLOCKS THE USER BY BREAKING THE LOOP
    if attempts <= 0:
        print("attempt limit exceeded you have been blocked".upper())
        break
    # IF USER LEAVES THE PASSWORD BLANK THE PROGRAM ASKS THEM TO ENTER SOMETHING WITHOUT DEDUCTING THEIR ATTEMPTS
    if to_login == "":
        print("Please enter something don't leave the password blank".upper())
        attempts += 1

# FEEDBACK FROM CHATGPT:
# Password Storage: Storing passwords in a list may not be the most secure or efficient approach, especially for real-world applications. Using a dictionary or a more secure storage mechanism would be preferable.
# Repetitive Code: Some parts of your code could be refactored to avoid repetition and improve readability. 
# For example, the logic for handling blank password inputs and checking for maximum attempts could be centralized.
# Lack of Modularity: Your solution could benefit from being organized into functions to promote code reusability and maintainability.
