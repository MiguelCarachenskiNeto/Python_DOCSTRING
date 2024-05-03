import os

restaurantes=[{"nome":"Boteco do Chef","categoria":"Bar","ativo":True},
              {"nome":"Comida Caseira","categoria":"Restaurante","ativo":False},
              {"nome":"Kibe Kitchen","categoria":"Árabe","ativo":True}]

def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal: \n")
    main() 

def mostrar_subtitulo(texto):
    os.system("clear")
    print(texto)
    print()


def desligar_app():
    mostrar_subtitulo("Finalizando o app")

def opcao_invalida():
    os.system("clear")
    print("Opção inválida\n")
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    os.system("clear")
    nome_do_restaurante=input("digite o nome do novo restaurante: \n")
    os.system("clear")
    categoria_do_restaurante=input(f"digite a categoria do restaurante {nome_do_restaurante}\n")
    restaurantes.append({"nome":nome_do_restaurante,"categoria":categoria_do_restaurante,"ativo":False})
    print(f"\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    os.system("clear")
    print("Restaurantes cadastrados:\n")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = restaurante["ativo"]
        print(f"-{nome_restaurante} -- {categoria} -- {ativo}")
    voltar_ao_menu_principal() 

def ativar_restaurante():
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
            

def nome_app():
    print('''
███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄─▄─██▀▄─██▄─██─▄█▄─▄▄▀██▀▄─██▄─▀█▄─▄█─▄─▄─█▄─▄▄─███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█─▄▄─█
██─▄─▄██─▄█▀█▄▄▄▄─███─████─▀─███─██─███─▄─▄██─▀─███─█▄▀─████─████─▄█▀████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█─██─█
▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀
''')

def exibir_opcoes():
    print("1-Cadastrar um restaurante")
    print("2-Listar restaurantes")
    print("3-Ativar um restaurante")
    print("4-Sair do programa\n")

def escolher_opcoes():
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
    os.system("clear")
    nome_app()
    exibir_opcoes()
    escolher_opcoes()

if __name__=="__main__":
    main()
