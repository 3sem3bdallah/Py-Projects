""" Bagels, A deductive logic game where you must guess a number based on clues. """

import random 
# (!) Try setting this to 1 or 10.
Num_Digits = int(input('Enter number of digit: '))
 # (!) Try setting this to 1 or 100.
Max_Guesses = int(input('Enter number of guess: '))

def main():
    print(f"""Bagels, a deductive logic game.
          You thinking of a {Num_Digits}-digit number with no repeated digits.
          Try to guess what it is, here some clues:

          When I say:       That means:
                Pico           One digit is correct but in wrong position.
                Fermi          One digit is correct and in correct position.
                Bagels         No digit is correct.

            For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.
            """)

    while True: # Main game loop.
        #  This stores the secret number the player need to guess:
        secret_num = getSecretNum()
        print('I have thought up the number.')
        print(f'You have {Max_Guesses} guesses to get it.')

        num_guesses = 1
        while num_guesses <= Max_Guesses:
            guess = ' '
            # Keep looping until they enter a valid guess:
            while len(guess) != Num_Digits or not guess.isdecimal():
                print(f'Guess #{num_guesses}: ')
                guess = input('> ')
            
            clues = getClues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break # they are correct, so break out of this loop.
            if num_guesses > Max_Guesses:
                print('You ran out of guesses.')
                print(f'the answer was {secret_num}.')

            # Ask player if they want to play again.
            print('Do you want to play again? (yes or no)')
            if not input ('> ').lower().startswith('y'):
                break
            print('Thanks for playing!')


def getSecretNum():
    """Returns a string made up of num_digit unique random digits"""
    numbers = list('0123456789') # Create a list of digits 0 to 9.
    random.shuffle(numbers) # Shuffle them into random order.
    
    # Get the first num_digits in the list for secret number:
    secret_num = ''
    for i in range(Num_Digits):
        secret_num += str(numbers[i])
    return secret_num


def getClues(guess, secret_num):
    """Returns a string with pico, fermi, bagels clues for a guess and secret number pair"""
    if guess == secret_num:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
            # There are no digits at all.
        return 'Bagels' 
    else:
        # Sort the clues into alphabetical order so their original order
        #  doesn't give information away.
        clues.sort()
        # make a single string from a list of string.
        return ' '.join(clues)
    
# if program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()