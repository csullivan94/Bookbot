def main():
    book_path = "books/Frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = book_length(book_text)
    char_count = character_count(book_text)
    let_count = letter_count(char_count)
    char_report(book_path, word_count, let_count)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def book_length(text):
    word_list = text.split()
    return len(word_list)

def character_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(char_dict_list):
    sort_on =  char_dict_list["count"]
    return sort_on

def letter_count(char_count):
    char_dict_list = []
    for i in char_count:
        if i.isalpha():
            char_dict_list.append({"char": i,  "count":char_count[i]})
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list



def char_report(book_path, words, list):
    print(f"------------Begin report of {book_path}-----------")
    print(f"There are {words} words in the document.\n")
    for i in list:
        print(f"There are {i["count"]} instances of the character {i["char"]}.")
    print(f"------------End of report-----------------")




main()
