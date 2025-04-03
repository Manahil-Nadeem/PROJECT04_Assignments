def main():
    # Get the 3 side lengths of the triangle
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculate and print the perimeter (sum of the sides)
    perimeter = side1 + side2 + side3
    print("The perimeter of the triangle is " + str(perimeter))

# To call the main() function.
if __name__ == '__main__':
    main()
