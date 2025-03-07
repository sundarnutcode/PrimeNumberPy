import sys
import math

def main():
    args = len(sys.argv)
 
    if args < 2:
        # Show prime numbers less than 2000, if the user has not provided any command line parameter
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


def checkForPrime(number, suppress_flag = False):

    if suppress_flag == False:
        if number <= 1:
            print(f"{number} is not technically a prime number.")
            return
        elif number <= 3:
            print(f"{number} is a prime number.")
            return;

    index = 2
    is_prime_number = True

    limit = int(math.sqrt(number))

    while index <= limit:
        if number > 3:
            if number % index == 0:
                if suppress_flag == False:
                    print(f"{number} is not a prime number.")

                is_prime_number = False
                break

            if index == 2:
                index = 3
            else:
                index += 2

                # Skip odd numbers that are multiples of 3, 5, and 7.
                while index < number and (index % 3 == 0 or (index % 5 == 0 and index != 5) or (index % 7 == 0 and index != 7)):
                    index += 2

    if is_prime_number and number > 1:
        if suppress_flag == True:
            print(number)
        else:
            print(f"{number} is a prime number.")
 
if __name__ == "__main__":
    main()
