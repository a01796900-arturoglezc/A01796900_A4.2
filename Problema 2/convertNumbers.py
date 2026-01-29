# pylint: disable=invalid-name
"""
Convert decimal numbers to binary and hexadecimal representations.

Results are printed on screen and saved into ConvertionResults.txt
"""

import sys
import time


def read_numbers_from_file(filename):
    """
    Reads integer numbers from a file.
    Invalid data is reported but execution continues.

    :param filename: Name of the input file
    :return: List of valid integers
    """
    numbers = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                value = line.strip()
                if not value:
                    continue
                try:
                    numbers.append(int(value))
                except ValueError:
                    print(
                        f"Invalid data at line {line_number}: '{value}'"
                    )
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    return numbers


def convert_to_binary(number):
    """
    Converts a decimal number to binary using basic algorithms.

    :param number: Decimal integer
    :return: Binary representation as string
    """
    if number == 0:
        return "0"

    result = ""
    n = abs(number)

    while n > 0:
        result = str(n % 2) + result
        n //= 2

    if number < 0:
        result = "-" + result

    return result


def convert_to_hexadecimal(number):
    """
    Converts a decimal number to hexadecimal using basic algorithms.

    :param number: Decimal integer
    :return: Hexadecimal representation as string
    """
    if number == 0:
        return "0"

    digits = "0123456789ABCDEF"
    result = ""
    n = abs(number)

    while n > 0:
        result = digits[n % 16] + result
        n //= 16

    if number < 0:
        result = "-" + result

    return result


def write_results(results):
    """
    Writes the results to ConvertionResults.txt.

    :param results: String with formatted results
    """
    with open("ConvertionResults.txt", "w", encoding="utf-8") as file:
        file.write(results)


def main():
    """
    Main program execution.
    Handles input arguments, conversions, and output.
    """
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    numbers = read_numbers_from_file(filename)

    if not numbers:
        print("No valid numeric data found.")
        sys.exit(1)

    output_lines = []

    for number in numbers:
        binary = convert_to_binary(number)
        hexadecimal = convert_to_hexadecimal(number)

        output_lines.append(
            f"Decimal: {number} | Binary: {binary} | Hexadecimal: {hexadecimal}"
        )

    elapsed_time = time.time() - start_time

    results = "\n".join(output_lines)
    results += f"\n\nExecution Time (seconds): {elapsed_time}\n"

    print(results)
    write_results(results)


if __name__ == "__main__":
    main()
