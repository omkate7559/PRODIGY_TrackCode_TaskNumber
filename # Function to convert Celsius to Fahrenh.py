# Function to convert Celsius to Fahrenheit and Kelvin
def celsius_to_other(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F and {kelvin:.2f}K")

# Function to convert Fahrenheit to Celsius and Kelvin
def fahrenheit_to_other(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C and {kelvin:.2f}K")

# Function to convert Kelvin to Celsius and Fahrenheit
def kelvin_to_other(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    print(f"{kelvin}K is equal to {celsius:.2f}°C and {fahrenheit:.2f}°F")

# Main program loop
def main():
    while True:
        print("\n--- Temperature Conversion Program ---")
        print("1. Celsius to Fahrenheit and Kelvin")
        print("2. Fahrenheit to Celsius and Kelvin")
        print("3. Kelvin to Celsius and Fahrenheit")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            celsius_to_other(celsius)
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            fahrenheit_to_other(fahrenheit)
        elif choice == '3':
            kelvin = float(input("Enter temperature in Kelvin: "))
            kelvin_to_other(kelvin)
        elif choice == '4':
            print("Exiting Temperature Conversion Program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the temperature conversion program
if __name__ == "__main__":
    main()
