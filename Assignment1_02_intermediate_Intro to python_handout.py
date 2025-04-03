# Constants for gravity percentages of each planet
GRAVITY_FACTORS = {
    'Mercury': 37.6,
    'Venus': 88.9,
    'Mars': 37.8,
    'Jupiter': 236.0,
    'Saturn': 108.1,
    'Uranus': 81.5,
    'Neptune': 114.0
}

def main():
    # Prompt for weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Prompt for planet name
    planet = input("Enter a planet: ")
    
    # Check if the entered planet is valid
    if planet in GRAVITY_FACTORS:
        # Calculate weight on the selected planet
        planet_weight = earth_weight * (GRAVITY_FACTORS[planet] / 100)
        
        # Print the weight on that planet rounded to 2 decimal places
        print(f"The equivalent weight on {planet}: {round(planet_weight, 2)}")
    else:
        print("Invalid planet name. Please enter a valid planet.")

if __name__ == "__main__":
    main()
