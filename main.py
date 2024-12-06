from Part3 import *
from Part2 import *
from Part1 import *
from Part4 import *


def main():
    # Part 1
    text = """&#39;Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.
J.U.U.U Kmltin.
mmps iks nmk eio; ---> hkmu"""

    mapping = get_dictionary_mapping(text)
    print("Mapping:", mapping)

    # Part 2
    encrypted_text = "///bha Taa3add, bha Tdaer, enr b7ha Fdcccccbbb..."
    resolved_text = decipher_text(encrypted_text)
    print("Decrypted text:", resolved_text)

    # Part 3
    decipher_file("message.txt")
    # Part 4
    longest_words = get_longest_word_in_a_file("results.txt")
    num_lines = get_number_of_rows_in_a_file("results.txt")
    print("Longest words:", longest_words)
    print("Number of lines:", num_lines)

    # Writing the longest words to original message file
    with open("message.txt", 'a') as file:
        file.write('\n')
        for i in range(num_lines):
            for word in longest_words:
                file.write(word + ' ')

        file.write('\n')
        for row_number in range(7):
            if row_number in (0, 1, 5, 6):
                file.write('*' + ' ' * 3 + '*' + '\n')
            else:  # 2,3,4
                if row_number % 2 == 0:
                    space = 1
                    file.write(' ' * space + '*' + ' ' * (2 - space) + '*' + '\n')
                else:
                    space = 2
                    file.write(' ' * space + '*' + '\n')


if __name__ == '__main__':
    main()
