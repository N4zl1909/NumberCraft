def calculate_gcd_lcm(number1, number2):
    if number1 <= 0 or number2 <= 0:
        return "Please enter positive integers greater than zero.", None

    a, b = number1, number2
    while b != 0:
        a, b = b, a % b

    gcd = a
    lcm = (number1 * number2) // gcd

    return gcd, lcm


while True:
    print("\n" + "=" * 40)
    print("GCD and LCM Calculator (Type 'q' to quit)")
    print("=" * 40)

    input1 = input("Enter 1st number: ").strip()
    if input1.lower() == 'q':
        print("Exiting program...")
        break

    input2 = input("Enter 2nd number: ").strip()
    if input2.lower() == 'q':
        print("Exiting program...")
        break

    try:
        num1 = int(input1)
        num2 = int(input2)
    except ValueError:
        print("Error: Please enter a valid integer!")
        continue

    gcd_result, lcm_result = calculate_gcd_lcm(num1, num2)

    if lcm_result is None:
        print(gcd_result)
    else:
        print(f"\nFor numbers {num1} and {num2}:")
        print(f"- GCD: {gcd_result}")
        print(f"- LCM: {lcm_result}")