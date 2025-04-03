import random

# Constants for the number of random numbers and the range
N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    # Generate and print 10 random numbers in the specified range
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")

# This line is required to run the main() function
if __name__ == '__main__':
    main()
