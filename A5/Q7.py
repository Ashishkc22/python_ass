from collections import Counter

def word_frequency():
    with open('input.txt', 'r') as infile:
        text = infile.read()
        words = text.split()
    word_count = Counter(words)
    print(word_count)
    # Sort by frequency in descending order
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    print("Word Frequency:")
    for word, count in sorted_word_count:
        print(f"{word}: {count}")

word_frequency()