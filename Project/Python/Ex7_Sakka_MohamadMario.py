import argparse
import csv

def compute_sum_and_product(input_file, output_file, column_index):
    try:
        integers = []
        with open(input_file, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  
            for row in reader:
                try:
                    integers.append(int(row[column_index]))
                except (ValueError, IndexError):
                    print(f"Skipping invalid row: {row}")

        total_sum = sum(integers)
        
        total_product = 1
        for num in integers:
            total_product *= num

        with open(output_file, 'w') as output:
            output.write(f"The sum is: {total_sum}\n")
            output.write(f"The multiplication is: {total_product}\n")

        print(f"Results written to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute sum and multiplication of integers from a CSV column.")
    parser.add_argument("input_file", help="Path to the input CSV file.")
    parser.add_argument("--output", required=True, help="Path to the output file.")
    parser.add_argument("--column", required=True, type=int, help="Column index for integers (0-based)")

    args = parser.parse_args()
    compute_sum_and_product(args.input_file, args.output, args.column)
