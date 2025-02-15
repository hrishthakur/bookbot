from collections import Counter

def count_characters(text):
    return dict(Counter(text.lower()))

def count_words(text):
    return len(text.split())

def main():
    with open("books/frankenstein.txt", "r") as file:
        file_contents = file.read()
        
    # Get the word count
    word_count = count_words(file_contents)
    print(f"The book contains {word_count} words.")
    
    # Get the character count
    char_count = count_characters(file_contents)
    for char, count in char_count.items():
        print(f"'{char}': {count}")

main()
