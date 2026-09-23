"""
Tutorial 2: The Word Detective Case File (TEACHER SOLUTION)
=============================================================

This is the completed, bug-free solution for Tutorial 2. Every bug from
the student starter file has been fixed below.

Learning Objectives:
- Practice string manipulation: .lower(), .upper(), .replace(), .split(), .strip()
- Practice building and updating dictionaries
- Practice looping over dictionary key-value pairs with .items()

Instructions:
- Run the program using: uv run detective.py
- Check the "Expected" comment next to each print() call to confirm success.
"""


def normalize_text(text):
    """
    Convert text to lowercase so comparisons are consistent.

    Args:
        text (str): the raw message text

    Returns:
        str: the lowercase message text
    """
    return text.lower()


def replace_secret_word(text, old_word, new_word):
    """
    Replace every occurrence of `old_word` with `new_word`.

    Args:
        text (str): the text to search
        old_word (str): the word to find
        new_word (str): the word to insert instead

    Returns:
        str: the text with replacements made
    """
    return text.replace(old_word, new_word)


def split_into_words(sentence):
    """
    Break a sentence into a list of individual words.

    Args:
        sentence (str): a sentence separated by spaces

    Returns:
        list: the individual words
    """
    return sentence.split()


def strip_punctuation(word):
    """
    Remove common punctuation marks from the edges of a word.

    Args:
        word (str): a single word, possibly with punctuation attached

    Returns:
        str: the word with leading/trailing punctuation removed
    """
    return word.strip(".,!?\"'")


def build_word_count_dict(words):
    """
    Count how many times each word appears in a list of words.

    Args:
        words (list): a list of words (already lowercase, no punctuation)

    Returns:
        dict: maps each word to how many times it appeared
    """
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def print_dictionary_report(word_counts):
    """
    Print every word and its count, one per line.

    Args:
        word_counts (dict): maps words to their counts
    """
    for word, count in word_counts.items():
        print(f"  '{word}' appeared {count} time(s)")


def find_longest_word(words):
    """
    Find the longest word in a list of words.

    Args:
        words (list): a list of words

    Returns:
        str: the longest word found
    """
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def main():
    """
    Process the intercepted message and reveal the case results.
    """
    print("\n" + "=" * 60)
    print("Tutorial 2: The Word Detective Case File")
    print("=" * 60)

    message = "The Suspect Left in a HURRY, but the SUSPECT dropped a clue!"

    print("\n[Clue 1] Normalizing the message...")
    normalized = normalize_text(message)
    print(f"  {normalized}")
    # Expected: "the suspect left in a hurry, but the suspect dropped a clue!"

    print("\n[Clue 2] Replacing the codeword 'suspect' with 'culprit'...")
    replaced = replace_secret_word(normalized, "suspect", "culprit")
    print(f"  {replaced}")
    # Expected: "the culprit left in a hurry, but the culprit dropped a clue!"

    print("\n[Clue 3] Splitting the message into words...")
    raw_words = split_into_words(replaced)
    print(f"  {raw_words}")
    # Expected: ['the', 'culprit', 'left', 'in', 'a', 'hurry,', 'but', ...]

    print("\n[Clue 4] Stripping punctuation from each word...")
    clean_words = [strip_punctuation(word) for word in raw_words]
    print(f"  {clean_words}")
    # Expected: no more commas or exclamation marks attached to words

    print("\n[Clue 5] Counting word usage...")
    counts = build_word_count_dict(clean_words)
    print_dictionary_report(counts)
    # Expected: 'culprit' appeared 2 time(s), 'the' appeared 2 time(s), etc.

    print("\n[Clue 6] Finding the longest word (the case-breaking clue!)...")
    longest_word = find_longest_word(clean_words)
    print(f"  The longest word is: '{longest_word}'")
    # Expected: 'culprit'

    print("\n" + "=" * 60)
    print("Case closed! If every result above matches its Expected")
    print("comment, you cracked it.")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
