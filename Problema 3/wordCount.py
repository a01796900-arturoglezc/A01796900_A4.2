# pylint: disable=invalid-name
"""
Count distinct words and their frequency from a text file.

Results are printed on screen and saved into WordCountResults.txt
"""

import sys
import time


def read_words_from_file(filename):
    """
    Reads words from a file.
    Invalid data is reported but execution continues.

    :param filename: Name of the input file
    :return: List of cleaned words
    """
    words = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue

                raw_words = line.split()
                for raw_word in raw_words:
                    cleaned_word = ""

                    for char in raw_word:
                        if char.isalnum():
                            cleaned_word += char.lower()

                    if cleaned_word:
                        words.append(cleaned_word)
                    else:
                        print(
                            f"Invalid word at line {line_number}: '{raw_word}'"
                        )
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    return words


def count_words(words):
    """
    Counts the frequency of each distinct word.

    :param words: List of words
    :return: Dictionary with word frequencies
    """
    frequencies = {}

    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1

    return frequencies


def write_results(results):
    """
    Writes the results to WordCountResults.txt.

    :param results: String with formatted results
    """
    with open("WordCountResults.txt", "w", encoding="utf-8") as file:
        file.write(results)


def main():
    """
    Main program execution.
    Handles input arguments, word counting, and output.
    """
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    words = read_words_from_file(filename)

    if not words:
        print("No valid words found.")
        sys.exit(1)

    frequencies = count_words(words)

    output_lines = []
    for word, count in frequencies.items():
        output_lines.append(f"{word}: {count}")

    elapsed_time = time.time() - start_time

    results = "\n".join(output_lines)
    results += f"\n\nExecution Time (seconds): {elapsed_time}\n"

    print(results)
    write_results(results)


if __name__ == "__main__":
    main()
