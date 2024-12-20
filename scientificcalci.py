import math

def scientific_calculator():
    print("Welcome to the Scientific Calculator!")
    print("Select an operation to perform:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (x^y)")
    print("6. Square root (√x)")
    print("7. Logarithm (log base 10)")
    print("8. Natural logarithm (ln)")
    print("9. Sine (sin)")
    print("10. Cosine (cos)")
    print("11. Tangent (tan)")
    print("12. Quit")

    while True:
        try:
            choice = int(input("\nEnter the number of the operation: "))

            if choice == 12:
                print("Exiting the calculator. Goodbye!")
                break

            if choice in [1, 2, 3, 4, 5]:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == 1:
                    print(f"Result: {num1} + {num2} = {num1 + num2}")
                elif choice == 2:
                    print(f"Result: {num1} - {num2} = {num1 - num2}")
                elif choice == 3:
                    print(f"Result: {num1} * {num2} = {num1 * num2}")
                elif choice == 4:
                    if num2 != 0:
                        print(f"Result: {num1} / {num2} = {num1 / num2}")
                    else:
                        print("Error: Division by zero is not allowed.")
                elif choice == 5:
                    print(f"Result: {num1}^{num2} = {math.pow(num1, num2)}")

            elif choice == 6:
                num = float(input("Enter the number: "))
                if num >= 0:
                    print(f"Result: √{num} = {math.sqrt(num)}")
                else:
                    print("Error: Cannot calculate the square root of a negative number.")

            elif choice == 7:
                num = float(input("Enter the number: "))
                if num > 0:
                    print(f"Result: log10({num}) = {math.log10(num)}")
                else:
                    print("Error: Logarithm undefined for non-positive numbers.")

            elif choice == 8:
                num = float(input("Enter the number: "))
                if num > 0:
                    print(f"Result: ln({num}) = {math.log(num)}")
                else:
                    print("Error: Natural logarithm undefined for non-positive numbers.")

            elif choice in [9, 10, 11]:
                angle = float(input("Enter the angle in degrees: "))
                radians = math.radians(angle)
                if choice == 9:
                    print(f"Result: sin({angle}°) = {math.sin(radians)}")
                elif choice == 10:
                    print(f"Result: cos({angle}°) = {math.cos(radians)}")
                elif choice == 11:
                    print(f"Result: tan({angle}°) = {math.tan(radians)}")

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    scientific_calculator()
