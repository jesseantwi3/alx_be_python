from robust_division_calculator import safe_divide

def main():
    num1 = input("Enter numerator: ")
    num2 = input("Enter denominator: ")

    result = safe_divide(num1, num2)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
