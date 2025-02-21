import re

from collections import Counter

def analyze_file(file_path):
    try:
        # Open AND READ THE FILE 
        with open("/home/ali/example.txt", "r", encoding="utf-8") as file:
            text = file.read()
        
        # COUNT THE CHARACTERS
        total_characters = len(text.replace(" ", "").replace("\n", ""))
        
        # COUNT THE WORDS
        words = text.split()
        total_words = len(words)
        
        # COUNT THE UNIQUE WORDS
        unique_words = len(set(words))
        
        # COUNT THE LINES
        total_lines = text.count("\n") + 1
        
        # COUNT THE SPECIAL CHARACTERS
        special_characters = len(re.findall(r"[^\w\s]", text))
        
        # FIND THE MOST COMMON WORD
        word_count = Counter(words)
        most_common_word, most_common_count = word_count.most_common(1)[0]
        
        # FIND THE LONGEST WORD
        longest_word = max(words, key=len)
        longest_word_length = len(longest_word)
        
        print("File Analysis:")
        print("Total Characters:", total_characters)
        print("Total Words:", total_words)
        print("Unique Words:", unique_words)
        print("Total Lines:", total_lines)
        print("Special Characters:", special_characters)
        print("Most Common Word:", most_common_word, "(appears", most_common_count, "times)")
        print("Longest Word:", longest_word, "(length:", longest_word_length, ")")
        
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Error reading file:", e)

# Example usage
file_path = "example.txt"  # Change this to your file name
analyze_file(file_path)

