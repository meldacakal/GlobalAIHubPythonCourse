# HW2
print("**** Welcome to our Website **** \n       Members only!!!")
#Creating a dictionary
members = {"Bee Gees": "stayinalive",
           "Micheal Jackson": "billiejean",
           "Bon Jovi":"itsmylife",
           "Eminem":"killshot",
           "Pink Floyd": "comfortablynumb",
           "Pearl Jam": "black"
           }
# sign_in variable is for registration purposes. It is used to create a loop.
sign_in = True
while sign_in == True:
    user = input("Please enter your username: ")
    if user in members:
        password = input("Please enter your password: ")
        if password == members[user]:
            print("You have successfully entered our secret website. Congrats!")
            sign_in = False
        else: print("The password you have written is incorrect. Please try again.")
    else:
        print("The username does not exist.")
        new = input("Would you like to register to our secret website? Y or N :")
        if new == "Y":
            register = input("Please enter your username: ")
            register_password = input("Please enter your password: ")
            members[register] = register_password
            print("You have successfully registered to our website. Please sign in.")
        else:
            print("This website is for members only.")
            sign_in = False


