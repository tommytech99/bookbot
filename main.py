def main():
    file_contents = get_book_contents()
    my_count = count_words(file_contents)
    print(f"My word count is: {my_count}") 
    my_count_dict = count_letters(file_contents)
    my_report(my_count_dict)

def get_book_contents():
    with open("books/frankenstein.txt") as f:
        return f.read()

def count_words(book_string):
    words = book_string.split()
    return len(words)

def my_report(report_dictionary):
    my_list = list(report_dictionary)
    my_list.sort()
    for lt in my_list:
        if lt.isalpha():
            print(f"The '{lt}' character was found {report_dictionary[lt]} times")

def count_letters(book_string):
    my_letters = {}
    for ch in book_string:
        current = ch.lower()
        if current not in my_letters:
            my_letters[current] = 1
        else: 
            my_letters[current] += 1
    return my_letters

main()
