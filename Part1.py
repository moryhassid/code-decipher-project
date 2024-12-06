# Assume that this is the text that appears in your text file:
# AB DMF GR YGI
# You found the next logic that connects between alphabetical characters to other alphabetical characters:
# M=A, Y=B, C=D, A=M, T=F, I=G, S=R, B=Y and G=I
# Pay attention that the logic is two directions, this means that if you found that M = A this automatically says that A = M.
# By this logic our decrypted text will be:
# MY CAT IS BIG
# Our actual decrypted text file will contain the next text:
# 'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'
# J.U.U.U Kmltin.
# mmps iks nmk eio; ---> hkmu

def get_dictionary_mapping(input_str):
    input_str = input_str.lower()
    dict_counter = dict()
    for char in set(input_str):
        if char.isalpha():
            dict_counter[char] = input_str.count(char)
    # print(f'Frequency of the characters in the message:')
    # print(dict_counter)
    # print('#' * 50)
    # In English =      ‘e’,’t’,’o’,’r’
    english_langauge_most_common = ['e', 't', 'o', 'r']
    dict_counter = dict(sorted(dict_counter.items(), key=lambda item: -item[1]))
    four_most_common_in_message = list(dict_counter)[:4]
    mapping = dict(zip(four_most_common_in_message, english_langauge_most_common))
    reverse_mapping = {v: k for k, v in mapping.items()}
    total_mapping = mapping | reverse_mapping
    return total_mapping


if __name__ == '__main__':
    mapping = {
        'M': 'A',
        'Y': 'B',
        'C': 'D',
        'T': 'F',
        'I': 'G',
        'S': 'R'
    }

    reverse_mapping = {v: k for k, v in mapping.items()}

    total_mapping = mapping | reverse_mapping
    print()

    input_str = 'AB DMF GR YGI'

    output = ''
    for char in input_str:
        output += total_mapping.get(char, char)

    print(f'{output=}')
