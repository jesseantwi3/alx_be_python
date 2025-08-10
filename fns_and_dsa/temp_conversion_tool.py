# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion functions
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    print("Temperature Conversion Tool")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter your choice (1 or 2): ").strip()

    try:
        temp = float(input("Enter the temperature: "))
    except ValueError:
        print("Invalid temperature input. Please enter a number.")
        return  # or exit()

    if choice == '1':
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C is {result:.2f}°F")
    elif choice == '2':
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F is {result:.2f}°C")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

