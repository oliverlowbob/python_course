# Exercise:
#	* Create a login application, that can store and handle multiple users.
#	* The user should be asked if he wants to log in or create a login.
#	* If 'create': The users credentials should be written to a file
#	* If 'login': The users information should be checked agains the content of the file. 
#	* The user should be granted or denied acces. 
#
# Go for the simplest, easiest, fastest approach!
#
# Most of what you need we already have covered, the rest is easy.
# You get 15 min. 
# Then we do it together

i = input("1: Create login \n2: Log in\n")

if i == "1":
    file = open("login.txt", "w")
    username = input("Username: ")
    password = input("Password: ")
    file.write(username + " " +password + "\n")
if i == "2":
    file = open("login.txt", "r")
    users = file.read().split("\n")
    print(users)
else:
    print("please enter 1 or 2")
