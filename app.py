import os

restaurantes=[{"nome":"Boteco do Chef","categoria":"Bar","ativo":True},
              {"nome":"Comida Caseira","categoria":"Restaurante","ativo":False},
              {"nome":"Kibe Kitchen","categoria":"Árabe","ativo":True}]

def nome_app():
    #docstring
    '''
    Exibe o nome do programa

    output:
    - Escreve o nome do programa

    '''
    print('''
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄─▄─██▀▄─██▄─██─▄█▄─▄▄▀██▀▄─██▄─▀█▄─▄█─▄─▄─█▄─▄▄─███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█─▄▄─█
██─▄─▄██─▄█▀█▄▄▄▄─███─████─▀─███─██─███─▄─▄██─▀─███─█▄▀─████─████─▄█▀████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█─██─█
▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀

                                                █▀▄▀█ █ █▀▀ █░█ █▀▀ █░░                                                
                                                █░▀░█ █ █▄█ █▄█ ██▄ █▄▄
''')

def exibir_opcoes():
    #docstring
    '''
    Exibe a lista de opções

    output:
    - escreve as opcões disponiveis a serem escolhidas

    '''
    print("1-Cadastrar um restaurante")
    print("2-Listar restaurantes")
    print("3-Ativar um restaurante")
    print("4-Sair do programa\n")

def cadastrar_novo_restaurante():
    #docstring
    '''
    Essa função é responsável por cadastrar um novo restaurante

    input:
    - nome do restaurante
    - categoria do restaurante

    output:
    - adiciona um novo restaurante ao dicionário restaurante

    '''
    os.system("clear")
    nome_do_restaurante=input("digite o nome do novo restaurante: \n")
    os.system("clear")
    categoria_do_restaurante=input(f"digite a categoria do restaurante {nome_do_restaurante}\n")
    restaurantes.append({"nome":nome_do_restaurante,"categoria":categoria_do_restaurante,"ativo":False})
    print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    #docstring
    '''
    Mostra os restaurantes cadastrados no dicionario restaurante

    output:
    - escreve o nome, categoria e status dos restaurantes presentes no dicionário restaurante

    '''
    os.system("clear")
    print("Restaurantes cadastrados:\n")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = restaurante["ativo"]
        print(f"-{nome_restaurante} -- {categoria} -- {ativo}")
    voltar_ao_menu_principal() 

def ativar_restaurante():
    #docstring
    '''
    Muda o status de um restaurante para ativo ou inativo

    input
    - nome do restaurante

    output
    - muda o status do restaurante escolhido

    '''
    mostrar_subtitulo("Alterando o estado do restaurante")
    nome_restaurante=input("digite o nome do restaurante que deseja ativar/desativar:\n")
    restaurante_encontrado = False
    os.system("clear")
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True       
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")
    voltar_ao_menu_principal()
            
def desligar_app():
    #docstring
    '''
    Finaliza o programa

    output:
    - limpa a exibição

    '''
    os.system("clear")
    mostrar_subtitulo("Finalizando o app")

def opcao_invalida():
    #docstring
    '''
    Redireciona o usuário ao menu principal caso a opção escolhida seja inválida

    output:
    - redireciona o usuário ao menu principal

    '''
    os.system("clear")
    print("Opção inválida\n")
    voltar_ao_menu_principal()    

def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal: \n")
    main() 

def mostrar_subtitulo(texto):
    #docstring
    '''
    Exibe o subtitulo 

    output:
    - escreve o subtítulo descrito nos parâmetros

    '''
    os.system("clear")
    print(texto)
    print()

def escolher_opcoes():
    #docstring
    '''
    Permite ao usuário executar a opção que deseja
    
    input:
    - opcão escolhida

    output:
    - executa uma função dependendo da escolha

    '''

    try:
        escolha=int(input("Escolha uma opção: "))
        print("Você selecionou a opção:",escolha,"\n")
        if escolha == 1:
            cadastrar_novo_restaurante()
        elif escolha == 2:
            listar_restaurantes()
        elif escolha == 3:
            ativar_restaurante()
        elif escolha == 4:
            print("Você escolheu sair do programa\n")
            desligar_app()
        else:
            opcao_invalida()

    except:
        opcao_invalida()

def main():
    #docstring
    '''
    Exibe a página principal do programa

    output:
    - exibe o nome
    - exibe as opcoes
    - escolha de opcoes

    '''
    os.system("clear")
    nome_app()
    exibir_opcoes()
    escolher_opcoes()

if __name__=="__main__":
    main()
