from random import randint
import linecache
a = open("textos.txt", "r") # pode ter um erro na hora de abrir esse arquivo, precisa ver se ele está na mesma pasta do arquivo .py

linhas = len(a.readlines())
palavra:str
a.close() # fechar o arquivo pra otimização

tentativas = 6
primeira_vez = True

def mostrar_desenhos():
        if tentativas == 5: print("----\n   |\n  ---\n\n ~~")
        if tentativas == 4: 
            print("----\n   |\n  ---\n\n ~~")
            print(" ( )")
        if tentativas == 3: 
            print("----\n   |\n  ---\n\n ~~")
            print(" ( )")
            print(" /|\\")
        if tentativas == 2: 
            print("----\n   |\n  ---\n\n ~~")
            print(" ( )")
            print(" /|\\")
            print("  |")
        if tentativas == 1: 
            print("----\n   |\n  ---\n\n ~~")
            print(" ( )")
            print(" /|\\")
            print("  |")
            print(" / \\")
        if tentativas == 0: 
            print("----\n   |\n  ---\n\n ~~")
            print(" ( )")
            print(" /|\\")
            print("  |")
            print(" / \\")
            print("/   \\")

forca = ['-','-','-','-','-','-'] # pra funcionar com palavras de nº de caracteres diferentes tem que mudar essa lista

while True:
    chute = ""
    while len(chute)!=1:
        chute = input("Diga uma letra...").lower().strip()
        if len(chute)!=1: print("O chute precisa ter um caracter")

    if (tentativas == 6 and primeira_vez) or tentativas == 0 or '-' not in forca: # resetar 
        forca = ['-','-','-','-','-','-']
        palavra = linecache.getline('textos.txt', randint(1, linhas))
        tentativas = 6

    if chute not in palavra:
        print(f"Errou! Faltam {tentativas} tentativas")
        tentativas-=1
        mostrar_desenhos()
    primeira_vez = False

    index=0
    for letra_atual in palavra: # letra_atual é criada nesse for. ela verifica caractere por caractere na palavra
        if chute == letra_atual:
            forca[index]=letra_atual # se o chute for igual à letra_atual, trocar o hífen pela letra
        index+=1
    print(forca)

    if '-' not in forca: print(f"Você ganhou! A palavra era: {palavra}")
    if tentativas == 0: print(f"Você perdeu! A palavra era: {palavra}")
