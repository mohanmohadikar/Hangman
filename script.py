import random

def get_word():
    word_list = [
        "apple", "ball", "cat", "dog", "elephant", "fish"
    ]
    return random.choice(word_list).upper()

word = get_word()
word_letter = list(word)

def check(word,guesses,guess):
    status = ""
    match = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += "*"
 
        if letter == guess:
            match += 1
    if match > 1 :
        print("YOU HAVE GUESSED " +match+" LETTER TRULY "+ guess)
    elif match == 1:
        print("YOU HAVE GUESSED 1 LETTER TRULY"+guess)
    else:
        print("ENTERED INPUT DOESN'T MATCH")
    return status

def main():
    #print word_letter
    num_of_guess = 0
    guesses = []
    guessed = False
    count = 0
    test = '*' * len(word_letter)
    print ("WELCOME!\nTHE WORD IS "+test+" AND IT HAS " +str(len(word_letter))+" LETTERS, YOU SHOULD GUESS IT NOW :)")
    while not guessed and count<8:
        guess_string_warn ="YOU HAVE 1 GUESS LEFT, TRY YOUR LUCK" if count==6 else "YOU HAVE "+str(8-count)+" GUESSES LEFT, TRY HARD"
        print(guess_string_warn)
        guess = input("ENTER YOUR GUESS: ")
        count = count + 1
        guess = guess.upper()
        if  len(guess) == 1 or  len(guess) == len(word_letter):
            num_of_guess += 1 
            if guess in guesses:
                print("YOU ALREADY GUESSED IT, I HOPED BETTER FROM YOU "+str(guess))
            elif len(guess) == len(word):
                guesses.append(guess)
                if guess == word :
                    guessed = True 
                 
                else:
                    print("IT'S NOT CORRECT, SORRY :(")
            elif len(guess) == 1: 
                guesses.append(guess)
                result = check(word, guesses, guess)
                if '*' not in result :
                    guessed = True 
                else:
                    print(result)
        else:
            print("LENGTH OF STRING SHOULD BE ," +str(len(word_letter))+" ENTER AGAIN")
    if guessed and count<8:
        print("BRAVO! YOUR GUESS IS CORRECT : " + word +" IN " + str(count) +" STEPS :)")
    else:
        print("YOU TOOK " + str(num_of_guess) +" STEPS, STILL YOU FAILED :(")


if __name__ == "__main__":
    main()