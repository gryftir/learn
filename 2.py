#!/usr/bin/env python
import random



def main():
    guessesTaken = 0
    print 'Hello, what is your name?'
    name = raw_input()
    number = random.randint(1, 20)
    guess = -1
    print "Well %s, I am thinking of a number between 1 and 20" % name
    while guessesTaken < 6 and guess != number:
        print 'take a guess.'
        guess = int(input())
        guessesTaken += 1
        if guess < number:
            print 'Your guess %d is too low.' % guess
        elif guess > number:
            print 'Your guess %d is too high.' % guess
    if guess == number:
        print "Good Job %s, you guessed my number in %d guesses" % (name,
                                                                    guessesTaken)
    else:
        print "nope, my number was %s." % str(number)
if __name__ == "__main__":
    main()
