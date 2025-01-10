def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    letter_dict = count_characters(text)
    sorted = letter_sorted(letter_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for c in sorted:
        if not c["char"].isalpha():
            continue
        print(f"The {c['char']} character was found {c['num']} times")
    print("--- End report ---")


#open book
def get_book_text(path):
    with open(path) as f:
        return f.read()

#count the number of words in the book
def count_words(text):
    words = text.split()
    return len(words)

#track count of each letter
def count_characters(text):
    letter = {}
    for c in text:
        lowered = c.lower()
        if lowered in letter:
            letter[lowered] += 1
        else:
            letter[lowered] = 1
    return letter

def sort_on(d):
    return d["num"]

#sorting dictionary into list from highest count to lowest
def letter_sorted(num_chars_dict):
    sorted = []
    for l in num_chars_dict:
        sorted.append({"char": l, "num": num_chars_dict[l]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted



main()