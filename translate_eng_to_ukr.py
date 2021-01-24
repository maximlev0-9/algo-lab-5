eng_text = " QWERTYUIOP{ }ASDFGHJKL:\"ZXCVBNM<>/qwertyuiop[]asdfghjkl;'zxcvbnm,./!#$%^&*()_+?"
ukr_text = " ЙЦУКЕНГШЩЗХ ЇФІВАПРОЛДЖЄЯЧСМИТЬБЮ.йцукенгшщзхїфівапролджєячсмитьбю.!№;%:?*()_+,"

def translate(text: str):
    result = ''
    for i in text:
        index = eng_text.find(i)
        result+= ukr_text[index]
    return result

if __name__ == '__main__':
    print('enter your text: \n')
    while True:
        input_text = input()
        if not input_text:
            print('Exit')
            break
        print(translate(input_text))
        print()
