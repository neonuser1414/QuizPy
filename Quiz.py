#The program demonstrates the operation of if else statements
number = input("Welcome to the quiz program! Choose the below numbers: \n Press 1 - to continue \n Press 2 - to view the info about QuizPy \n Press 3 - to close the program  \n Choise: ")
#For example, if the number 1 is entered, then the quiz will start
if number == "1":
        print("Ok! Let's get started! \n First question:")
        variant = input("In what year was FIFA founded? \n 1 - 1904 year \n 2 - 1906 year \n 3 - 1920 year \n Answer: ")
        if variant == "1":
                #Here you guessed it
            print("You guessed it! \n Second question:")
            variant = input("What was the first processor released by Intel? \n 1 - Intel Atom \n 2 - Intel 4004 \n 3 - Intel Pentium \n Answer: ")
            if variant == "2":
                print("Great! You guessed it again! Let's move on! \n Third question:")
                variant = input("Date of appearance of the Python programming language \n 1 - 1991 year \n 2 - 1996 year \n 3 - 2001 year \n Answer: ")
                if variant == "1":
                    print("Excellent! You have good knowledge! And now the last - fourth question!: ")
                    variant = input("When did Windows 10 come out? \n 1 - 2 september 2015 year \n 2 - 30 june 2015 year \n 3 - 29 july 2015 year \n Answer: ")
                    if variant == "3":
                            #The program congratulates you and now you can press Enter to exit the program
                        print("Your knowledge is amazing! Thank you for your participation! See you soon!")
                        input("To confirm the exit, press Enter \n Confirmation: ")
                    else:
                            #It looks like you made a mistake
                        print("Oops... It seems you made a mistake. Try again!")
                else:
                    print("Oops... It seems you made a mistake. Try again!")
            else:
                print("Oops... It seems you made a mistake. Try again!")
        else:
            print("Oops... It seems you made a mistake. Try again!")
            input("Press Enter to exit the program")
elif number == "2":
        #Information about the program is shown here: version, developer, etc.
        print("\n QuizPy \n Version 1.3 \n Developed by neonuser1414: \n https://github.com/neonuser1414/QuizPy")
        print(">---------------------------<")
        print("QuizPy - it's a open-source mini-game, made on Python. Everyone can improve the program and add new features to it. \n")
        input("For exit, press Enter \n Confirmation: ")
elif number == "3":
        #The program will thank you for your participation and now you can exit it by pressing Enter
        print("Thank you for participating! Goodbye!")
        input("To confirm the exit, press Enter \n Confirmation: ")
else:
        #The program reports incorrect user input
        print("Incorrect input option. So, try it again.")
        input("For exit, press Enter \n Confirmation: ")

