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
    user_input = input('Insira o número: ').replace(' ','')
    lines = count_lines()

    if user_input == '1':
        return insert_and_verify(lines),menu()

    if user_input == '2':
       return load_file(lines),menu()

    if user_input == '3':
        return clean_file(), menu()

    if user_input == '4':
        return game(), menu()
    if user_input == '5':
        return

def count_lines():
    arq = open('palavras.txt', 'r', encoding='utf-8')
    arq.seek(0,0)
    arq.read()
    lines = arq.readlines()
    return lines


def insert_and_verify():
    lines = count_lines()
    print('Digite "0" e aperte ENTER para encerrar ou apenas dê um ENTER para continuar: ')
    print("Digite 10 palavras para o jogo da forca")
    palavras_arq = open('palavras.txt', 'w', encoding='utf-8')

    need_lines = 10 - len(lines)
    while need_lines > 0:
        user_input = str(input('Insira palavras para serem usadas no game da forca: ')).replace(' ','')
        if user_input != '0':
            palavras_arq.write(user_input + '\n')
            need_lines = need_lines -1
        elif need_lines > 0 and user_input == '0':
            print("O arquivo ainda não está pronto para o jogo! \n São necessárias",need_lines,"palavras")
    print("O arquivo está pronto para o jogo!")
    return(list)
        

def load_file():
    lines = count_lines()
    arq = open('palavras.txt', 'r', encoding='utf-8')
    arq.seek(0,0)
    arq.read()
    arq.seek(0,0)
    lines = arq.readlines()
    list_arq=[]
    for i in range(len(lines)):
        list_arq.append(lines[i].replace('\n',''))
    return(list_arq),print("Seu arquivo foi carregado para o jogo e o jogo já pode ser iniciado!")

def clean_file():
    with open('palavras.txt', 'w') as arqs:
        arqs.write('')
    print('File erased!')

def game():
    list_game = load_file()
    import random
    import time
    print('\n','*'*30, "Bem vindo ao Jogo da Forca!", '*'*30,'\n')    
    word_game = random.choice(list_game[0])    
    list_guess = []
    for i in range(len(word_game)):
        list_guess.append('_')    
    list_game = []
    for i in word_game:
        list_game.append(i)    
    time.sleep(0.3)
    print("A palavra escolhida tem",len(list_guess),"letras...")
    time.sleep(0.5)
    list_error = []
    list_repeat = []

    print("Palavra a adivinhar:",*list_guess)
    while list_game != list_guess:
        guess = input("Digite seu chute: ").replace(' ','')
        if len(guess) > 1 and guess == word_game:
            break
        elif len(guess) > 1 and guess != word_game:
            print("Seu chute está errado. Tente outro ou continue tentando...")
        while guess in list_repeat:
            guess = input("Você já digitou essa letra, por favor, digite outro chute: ").replace(' ','')
        list_repeat.append(guess)
        if guess in list_game:
            print("\nVocê acertou uma das letras!!")
            for i in range(len(list_game)):
                if list_game[i] == guess:
                    list_guess[i] = list_game[i]         
            print("Palavra:",*list_guess)
        else:
            list_error.append(guess+' -')
            print("\nVocê errou! Letras erradas totais:",*list_error)         
    print('\n'+'*'*30)
    print("\nParabéns, você acertou, a palavra era:",*list_game)
    print('\n'+'*'*30+'\n')
main()