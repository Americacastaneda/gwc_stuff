#assign some secret word that the user must guess
secret_word = list("gnarly")
#word = word.lower()

# example : ["a", "b", "c", "_", "_"]
blank_word = ["_", "_", "_", "_", "_", "_"]
#have some variable that tells us to keep the game going and to continue the while loop
guesses = []
maxFails = 10
fails = 0
#ask user to guess a letter

#if users guess is in the word fill in the list according to where the letter is in the word
while fails < maxFails:
    print(blank_word)
    guess = input("Guess a letter.")
    if (guess in secret_word):
        for guess in range(0,6):
            if(secret_word[guess] == guess):
                guesse
        
            if guess == secret_word[0]:
                blank_word = [guess, "_", "_", "_", "_", "_" ]
            #append 
            if guess == secret_word[1]:
                blank_word = ["_", guess, "_", "_", "_", "_" ]

    else:
        fails += 1



#if user's guess is NOT in the word, ask again. Do not update the list.