#!/usr/bin/env python

def main():
    for num in range(1,101):
        printString = ''
        if num % 3 == 0:
            printString +='Fizz'
        if num % 5 == 0:
            printString += 'Buzz'
        if printString != '':
            print printString
        else:
            print num


if __name__ == "__main__":
	main()
