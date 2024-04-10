import os

def desligar_app():
    os.system('cls')
    print('Desligando o app\n')

def nome_app():
    print('Restaurante Expresso\n')

def lista():
    print('1-Cadastrar um restaurante')
    print('2-Listar restaurantes')
    print('3-Ativar um restaurante')
    print('4-Sair do programa\n')

def opcoes():
    escolha=int(input('Escolha uma opção: '))
    print('Você selecionou a opção:',escolha,'\n')
    if escolha == 1:
        print('Você escolheu cadastrar um restaurante\n')
    elif escolha == 2:
        print('Você escolheu listar os restaurantes\n')
    elif escolha == 3:
        print('Você escolheu ativar um restaurante\n')
    else:
        print('Você escolheu sair do programa\n')
        desligar_app()

def main():
    nome_app()
    lista()
    opcoes()

if __name__=='__main__':
    main()