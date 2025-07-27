# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main interaction with user
def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temp = float(temp_input)  # This line should raise ValueError if input is not numeric

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        elif unit == 'C':
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")
        else:
            # Explicitly raise error if unit is wrong
            raise ValueError("Invalid unit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Only run if file is run directly
if __name__ == "__main__":
    main()

