import re


def get_longest_word_in_a_file(file_path):
    with open(file_path, 'r') as fp:
        lines = fp.readlines()

    whole_text = ' '.join(lines)
    regex = re.compile('[^ a-zA-Z]')
    result = regex.sub('', whole_text)
    result = result.split(' ')
    sorted_result = sorted(result, key=lambda x: -len(x))
    length_of_longest_words = len(sorted_result[0])
    list_of_longest_words = []

    for word in sorted_result:
        if len(word) == length_of_longest_words:
            list_of_longest_words.append(word)

    return list_of_longest_words


def get_number_of_rows_in_a_file(file_path):
    with open(r"results.txt", 'r') as fp:
        count_of_lines = len(fp.readlines())

    return count_of_lines


if __name__ == '__main__':
    result = """practice, eventually makes perfect. all you need is python.
    j.r.r.r tolkin.
    oops its not him; ---> etor
    """

    file_path = 'results.txt'
    result_of_longest_words = get_longest_word_in_a_file(file_path)
    print(f'{result_of_longest_words=}')

    number_of_rows = get_number_of_rows_in_a_file(file_path)
    print(f'{number_of_rows=}')
 
