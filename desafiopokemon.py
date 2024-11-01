class pokemon:
    def __init__(self, nome, level, hp):
        self.nome = nome
        self.level = level
        self.hp = hp

def cadastrar_pokemon():
    while True:
        nome = input("Nome: ").strip().title()
        if nome.isalpha():
            break
        else: 
            print("Entrada inválida! Digite apenas letras!")
            
    while True:
        try:
            level = int(input("Level: "))
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números em level!")

    while True:
        try:
            hp = int(input("HP: "))
            break
        except ValueError:
            print('Entrada inválida! Digite apenas números em HP!')
                
    return pokemon(nome, level, hp)

# def mostrar_matriz(matriz_pokemon):
#     print("Pokemón(s) cadastrado(s) com sucesso:")
#     for pokemon in matriz_pokemon:
#         print(f"Nome: {pokemon[0]}")
#         print(f"Level: {pokemon[1]}")
#         print(f"HP: {pokemon[2]}")
#         print(f"-"*15)

# def mostrar_matriz(matriz_pokemon):
#     print("Pokémon(s) cadastrado(s) com sucesso:")
#     for nome, level, hp in matriz_pokemon:
#         print(f"Nome: {nome}")
#         print(f"Level: {level}")
#         print(f"HP: {hp}")
#         print("-" * 15)

def mostrar_matriz(matriz_pokemon):
    print("Pokemón(s) cadastrado(s) com sucesso:")
    for nome, level, hp in matriz_pokemon:
        print(f"\nNome: {nome}\nLevel: {level}\nHP: {hp}\n{"-" * 15}")

# função principal
def principal():
    matriz_pokemon = []
    
    while True:
        print('Cadastre aqui seu pokémon: ')
        pokemon = cadastrar_pokemon()
        matriz_pokemon.append([pokemon.nome, pokemon.level, pokemon.hp])

        while True:    
            continuar = input("Deseja cadastrar outro pokémon? [S/N]: ")[0].strip().upper()
            if continuar == "N":
                mostrar_matriz(matriz_pokemon)
                return 
            elif continuar == "S":
                break
            else:
                print("S para SIM ou N para NÃO")
         
principal()
