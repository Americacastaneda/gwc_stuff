secret_word = list("gnarly")
blank_word = ["_", "_", "_", "_", "_", "_"]
guesses = []
maxFails = 10
fails = 0
while fails < maxFails:
    print(blank_word)
    guess = input("Guess a letter.")
    if (guess in secret_word):
        for i in range(0,6):
            if(secret_word[i] == guess):
                blank_word[i] = guess
    else:
        maxFails += fails

      