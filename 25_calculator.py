def mini_math_tool():
    print("=== Math Operations Menu ===")
    print("A. Add")
    print("B. Subtract")
    print("C. Multiply")
    print("D. Divide")

    action = input("Pick an option (A/B/C/D): ").upper()

    if action in ['A', 'B', 'C', 'D']:
        val_a = float(input("Enter first value: "))
        val_b = float(input("Enter second value: "))

        if action == 'A':
            answer = val_a + val_b
            symbol = "+"
        elif action == 'B':
            answer = val_a - val_b
            symbol = "-"
        elif action == 'C':
            answer = val_a * val_b
            symbol = "*"
        elif action == 'D':
            if val_b == 0:
                return "❌ Cannot divide by zero!"
            answer = val_a / val_b
            symbol = "/"

        return f"{val_a} {symbol} {val_b} = {answer}"
    else:
        return "⚠ Invalid option! Try again."


print(mini_math_tool())
