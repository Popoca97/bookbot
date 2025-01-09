def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    letter_dict = count_characters(text)
    print(letter_dict)



def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    letter = {}
    for c in text:
        lowered = c.lower()
        if lowered in letter:
            letter[lowered] += 1
        else:
            letter[lowered] = 1
    return letter







main()