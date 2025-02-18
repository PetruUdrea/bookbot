def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_num_word(text)
    num_char = get_char_count(text)
    report(book_path, num_words, num_char)
    


def report(path, num_words, char_count):
    # selecting only alphabetical characters
    alphabetical_dict = {k: v for k, v in char_count.items() if k.isalpha()}
    # creating a list of dictionaries
    dict_list = [{"char": char, "count": count} for char, count in alphabetical_dict.items()]
    # sorting the list
    sorted_list = sorted(dict_list, key=lambda x: x['count'], reverse=True)
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for dict in sorted_list:
        print(f"The '{dict["char"]}' character was found {dict["count"]} times")


def get_char_count(text):
    char_count = {}
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    
    return char_count


def get_num_word(text):
    words = text.split()
    return len(words)


def get_text(path):
    with open(path) as f:
        return f.read()


main()