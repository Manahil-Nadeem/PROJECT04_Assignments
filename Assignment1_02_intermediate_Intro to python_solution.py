# Constants for the gravitational constants of each planet
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0

def main():
    # Prompt the user to enter their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Prompt the user to enter the name of the planet
    planet = input("Enter a planet: ")
    
    # Determine the gravitational constant for the selected planet
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity_constant = NEPTUNE_GRAVITY
    else:
        # Default to Earth if an invalid planet is entered
        gravity_constant = EARTH_GRAVITY
        print(f"Invalid planet entered. Defaulting to Earth.")
    
    # Calculate the equivalent weight on the selected planet
    planetary_weight = earth_weight * gravity_constant
    
    # Round the result to 2 decimal places
    rounded_planetary_weight = round(planetary_weight, 2)
    
    # Print the result
    print(f"The equivalent weight on {planet}: {rounded_planetary_weight}")

# Ensure that the main function is called when the program is executed
if __name__ == "__main__":
    main()