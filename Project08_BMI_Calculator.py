import streamlit as st

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Streamlit UI
def main():
    st.title("BMI Calculator")
    
    # Getting user input
    st.write("Enter your details to calculate your BMI.")
    
    weight = st.number_input("Weight (in kg)", min_value=1.0, step=0.1)
    height = st.number_input("Height (in meters)", min_value=0.1, step=0.01)
    
    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            st.write(f"Your BMI is: {bmi:.2f}")
            
            # BMI categories
            if bmi < 18.5:
                st.write("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.write("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.write("You are overweight.")
            else:
                st.write("You are obese.")
        else:
            st.write("Please enter valid weight and height.")

# Run the app
if __name__ == "__main__":
    main()
