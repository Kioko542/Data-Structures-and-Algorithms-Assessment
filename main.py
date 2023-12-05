# main.py

def is_balanced(expression):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_brackets.index(stack.pop()) != closing_brackets.index(char):
                return False

    return not stack

def remove_duplicates(sequence):
    seen = set()
    result = []

    for element in sequence:
        if element not in seen:
            result.append(element)
            seen.add(element)

    return result

import string

def word_frequency(sentence):
    word_counts = {}
    sentence = sentence.lower()
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))

    words = sentence.split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

# Additional code or tests can go here

if __name__ == "__main__":
    # Example usage or tests
    expression1 = "([]{})"
    expression2 = "([)]"
    print(is_balanced(expression1))  # Output: True
    print(is_balanced(expression2))  # Output: False

    input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
    result = remove_duplicates(input_sequence)
    print(result)  # Output: [2, 3, 4, 5, 6, 7]

    sentence = "This is a test sentence. This sentence is a test."
    result = word_frequency(sentence)
    print(result)
