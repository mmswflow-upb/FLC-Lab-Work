import argparse

def basic_operations_parser(num1, num2):
    """
    Computes the sum, difference, multiplication, division, and mean of two numbers.
    """
    results = {
        'sum': num1 + num2,
        'difference': num1 - num2,
        'multiplication': num1 * num2,
        'division': num1 / num2 if num2 != 0 else "Division by zero error",
        'mean': (num1 + num2) / 2
    }
    return results


def symbol_based_parser(num1, num2, symbol):
    """
    Computes a mathematical operation based on the provided symbol.
    Supported symbols: +, -, *, /, m (mean).
    """
    if symbol == '+':
        return num1 + num2
    elif symbol == '-':
        return num1 - num2
    elif symbol == '*':
        return num1 * num2
    elif symbol == '/':
        return num1 / num2 if num2 != 0 else "Division by zero error"
    elif symbol == 'm':
        return (num1 + num2) / 2
    else:
        return "Invalid operation symbol"


def main():
    parser = argparse.ArgumentParser(description="Parser for basic arithmetic operations")
    
    parser.add_argument("num1", type=float, help="The first number")
    parser.add_argument("num2", type=float, help="The second number")
    parser.add_argument("symbol",  type=str, choices=['+', '-', '*', '/', 'm'], 
                        help="The operation symbol (+, -, *, /, m) for the second part of the task")
    
    args = parser.parse_args()

    if args.symbol:
        # Part 2: Compute based on symbol
        result = symbol_based_parser(args.num1, args.num2, args.symbol)
        print(f"Result for operation {args.num1} {args.symbol} {args.num2}: {result}")
    else:
        # Part 1: Compute all operations
        results = basic_operations_parser(args.num1, args.num2)
        print("Results for basic operations:")
        for operation, result in results.items():
            print(f"{operation}: {result}")


if __name__ == "__main__":
    main()
