import sys
import math

def main():
    args = len(sys.argv)
 
    if args < 2:
        list = range(0,2000)

        for i in list:
            checkForPrime(i, True)

        return

    number = -1

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Please enter a valid number.")
        return

    if (number >= 0):
        checkForPrime(number)
    else:
        print("Please enter positive numbers.")


def checkForPrime(number, suppress = False):

    if suppress == False:
        if number <= 1:
            print(f"{number} is not technically a prime number.")
            return
        elif number <= 3:
            print(f"{number} is a prime number.")
            return;

    index = 2
    primeNumber = True

    while index <= int(math.sqrt(number)):
        if number > 3:
            if number % index == 0:
                if suppress == False:
                    print(f"{number} is not a prime number.")

                primeNumber = False
                break

            if index == 2:
                index = 3
            else:
                index += 2

                while index < number and (index % 3 == 0 or (index % 5 == 0 and index != 5) or (index % 7 == 0 and index != 7)):
                    index += 2

    if primeNumber:
        if suppress == True:
            print(number)
        else:
            print(f"{number} is a prime number.")
 
if __name__ == "__main__":
    main()
