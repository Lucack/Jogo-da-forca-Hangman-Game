# 1 - creat a menu that calls functions and execute it, and after, return to the menu if the game isn't called.
# 2 - creat a function that writes random words from the user input and store it in a txt. file
# 3 - creat a func. that loads the main file, allows to continue if the txt. file has more >= than 10 words,
#     and if not,
#     keep asking to the user to insert new words until it reaches 10 in total but not overwriting the first words
#     already inserted
# 4 - creat a func. that erases all the words in the txt. file if the user press the menu key for it
# 5 - creat a func. that calls a hangman game using the words in the txt. file

def main():
    menu()


def menu():
    print('Welcome! Select a number to start...')
    print('Insira o número 1 para inserir palavras no arquivo.')
    print('Insira o número 2 para carregar o arquivo.')
    print('Insira o número 3 para limpar o arquivo.')
    print('Insira o número 4 para iniciar o game da forca.')
    print('Insira o número 5 para encerrar.')
    user_input = input('Insira o número: ')

    if user_input == '1':
        return insert_words(), load_file()
    if user_input == '2':
        return load_file(), menu()
    if user_input == '3':
        return clean_file(), menu()


def insert_words():
    print('Digite "0" e aperte ENTER para encerrar ou apenas dê um ENTER para continuar: ')
    user_input = str(input('Insira palavras para serem usadas no game da forca: '))

    palavras_arq = open('palavras.txt', 'w', encoding='utf-8')

    while user_input != '0':
        palavras_arq.write(user_input)
        palavras_arq.write('\n')
        user_input = str(input('Insira palavras para serem usadas no game da forca: '))


def load_file():
    with open('palavras.txt', 'r', encoding='utf-8') as arq:
        arq.read()
        arq.seek(0, 0)
        l_arq = arq.readlines()

        lista_arq = []

        if len(l_arq) < 10:
            need_lines = 10 - len(l_arq)
            print('O arquivo parace não conter aquivos ou menos de 10...')
            print('Você ainda precisa de mais', need_lines, 'palavras para continuar...')
        for word in l_arq:
            lista_arq.append(word.replace('\n', ''))
        if need_lines != 0:
            for i in range(need_lines):
                with open('palavras.txt', 'a') as arq2_app:
                    user_input = input('Insira as palavras restantes: ')
                    arq2_app.write(user_input + '\n')
                    lista_arq.append(user_input)
        # for word in lista_arq:
        #     arq.write(word + '\n')


def clean_file():
    with open('palavras.txt', 'w') as arqs:
        arqs.write('')
    print('File erased!')


main()