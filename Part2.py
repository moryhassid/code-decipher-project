# 'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'
# J.U.U.U Kmltin.
from Part1 import get_dictionary_mapping


def decipher_text(input_str):
    input_str = input_str.lower()
    total_mapping = get_dictionary_mapping(input_str)
    print(total_mapping)
    output = ''
    for char in input_str:
        output += total_mapping.get(char, char)
    # print(f'{output=}')

    return output


if __name__ == '__main__':
    input_str = '''Puackich, hvhnkrally oaths phufhck.All ymr nhhd is Pykemn.'
J.U.U.U Kmltin.
mmps iks nmk eio; ---> hkmu'''

    decipher_text(input_str)
