# pylint: disable=invalid-name
"""
Compute descriptive statistics from a file with numeric data.

Statistics calculated:
- Mean
- Median
- Mode
- Variance
- Standard Deviation

Results are printed on screen and saved into StatisticsResults.txt
"""

import sys
import time


def read_numbers_from_file(filename):
    """
    Reads numbers from a file and ignores invalid data.

    :param filename: Name of the input file
    :return: List of valid float numbers
    """
    numbers = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                value = line.strip()
                if not value:
                    continue
                try:
                    numbers.append(float(value))
                except ValueError:
                    print(
                        f"Invalid data at line {line_number}: '{value}'"
                    )
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    return numbers


def compute_mean(numbers):
    """
    Computes the mean of a list of numbers.

    :param numbers: List of numeric values
    :return: Mean value
    """
    total = 0.0
    for number in numbers:
        total += number
    return total / len(numbers)


def compute_median(numbers):
    """
    Computes the median of a list of numbers.

    :param numbers: List of numeric values
    :return: Median value
    """
    sorted_numbers = sorted(numbers)
    size = len(sorted_numbers)
    middle = size // 2

    if size % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    return sorted_numbers[middle]


def compute_mode(numbers):
    """
    Computes the mode of a list of numbers.

    :param numbers: List of numeric values
    :return: Mode value
    """
    frequency = {}

    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    max_count = 0
    mode_value = None

    for number, count in frequency.items():
        if count > max_count:
            max_count = count
            mode_value = number

    return mode_value


def compute_variance(numbers, mean):
    """
    Computes the variance of a list of numbers.

    :param numbers: List of numeric values
    :param mean: Mean value of the list
    :return: Variance
    """
    total = 0.0
    for number in numbers:
        total += (number - mean) ** 2
    return total / len(numbers)


def compute_standard_deviation(variance):
    """
    Computes the standard deviation.

    :param variance: Variance value
    :return: Standard deviation
    """
    return variance ** 0.5


def write_results(results):
    """
    Writes the results to StatisticsResults.txt.

    :param results: String with formatted results
    """
    with open("StatisticsResults.txt", "w", encoding="utf-8") as file:
        file.write(results)


def main():
    """
    Main program execution.
    Handles input arguments, calculations, and output.
    """
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    numbers = read_numbers_from_file(filename)

    if not numbers:
        print("No valid numeric data found.")
        sys.exit(1)

    mean = compute_mean(numbers)
    median = compute_median(numbers)
    mode = compute_mode(numbers)
    variance = compute_variance(numbers, mean)
    std_deviation = compute_standard_deviation(variance)

    elapsed_time = time.time() - start_time

    results = (
        f"Count: {len(numbers)}\n"
        f"Mean: {mean}\n"
        f"Median: {median}\n"
        f"Mode: {mode}\n"
        f"Variance: {variance}\n"
        f"Standard Deviation: {std_deviation}\n"
        f"Execution Time (seconds): {elapsed_time}\n"
    )

    print(results)
    write_results(results)


if __name__ == "__main__":
    main()
