start = '''
It is the year 2030, global warming has not been solved, and because humans suck
we have broke out in a zombie apocalypse. Your goal is to survive, but if you 
decide that you don't want to anymore than that is cool too. You do you homie.
'''
keepplaying  = "yes"
print(start)

while keepplaying == "Yes" or keepplaying == "yes":
    print(" ")
    print("You wake up in the morning and see no one in sight, not even your dog.")
    
    userChoice = input("Do you go outside to meet someone or stay indoors? Type 1 to go outside or 2 to stay indoors.")
    if userChoice == "2":
        print(" ")
        print("Congrats! You didn't die, since you were too scared to even go outside")
        print("The zombies weren't able to break through, since they didn't even think there was anyone inside.")
        keepplaying = "no"
    elif userChoice == "1":
        print(" ")
        print("You realize you have no survival skills and didn't even bring a weapon with you.")
        print("You didn't even make it a mile out of your house before you got killed by a zombie in 7-11")
        print(" ")
        keepplaying = input("Would you like to try again? Type yes or no. ")
        if keepplaying == "no":
            quit()
    else:
        print(" ")
        print("Please select one of the valid options: 1 or 2.")
        keepplaying = input("would you like to try again? Type yes or no.")
        if keepplaying == "no":

keepplaying = "yes"
while keepplaying == "Yes" or keepplaying == "yes":
    print(" ")
    print("Someone is knocking in your door, they don't make any sounds that resemble a zombie.")
    userChoice = input("Do you open the door for them or do you not answer to the door? Type 1 to open the door or type 2 to not.")
    if  userChoice == "1":
        print(" ")
        print("You escaped death once again! There is no need to be selfish and let others die.")
        print("Liam Neeson is at the door and behind him is a van of supplies that will keep you guys alive for about 6 months.")
    elif userChoice == "2":
        print(" ")
        print("What kind of human are you?")
        print("This is the reason why this apocalypse even started. Selfish.")
        print("You could have met Liam Neeson but instead you were an introvert that failed to get supplies")
        print(" ")
        keepplaying = input("Would you like to try again? Type yes or no. ")
        if keepplaying == "no":
            quit()
    else:
        print(" ")
        print("Please select one of the valid options: 1 or 2.")
        keepplaying = input("would you like to try again? Type yes or no.")
        if keepplaying == "no":
            quit()


    