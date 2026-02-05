# File / Text Analyzer (CLI)

A simple Python command-line program that analyzes a text file and prints the most frequent words.

The program reads a text file, converts all words to lowercase, removes punctuation, ignores empty tokens, counts how often each word appears, sorts the results by frequency, and displays the most common words.

Features

Reads text from a file

Converts words to lowercase (case-insensitive analysis)

Removes punctuation from words

Ignores empty tokens

Counts word frequency

Sorts words by occurrence

User selects how many top words to display

Validates user input (prevents invalid numbers)

Handles missing files gracefully



## Usage

Run the script from the terminal:

When prompted, enter the name of a text file:

Insert filename: example.txt

Example Output
1. python - 12
2. code - 8
3. file - 5
Notes

The input file must be a plain text file.

If the file does not exist, the program prints an error message and exits.






```bash
python analyzer.py





