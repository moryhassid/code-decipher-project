from Part2 import decipher_text


def decipher_file(file_path):
    with open(file_path, 'r') as fd:
        content = fd.read()

    resolved_text = decipher_text(content)
    # print(f'{resolved_text=}')

    with open(file_path, 'a') as fd:
        fd.write('The encryption for the above text is:\n')
        fd.write(resolved_text)

    with open('results.txt', 'w') as fd:
        fd.write(resolved_text)


if __name__ == '__main__':
    decipher_file(r'C:\Users\mory9\PycharmProjects\homework5_project\message.txt')
