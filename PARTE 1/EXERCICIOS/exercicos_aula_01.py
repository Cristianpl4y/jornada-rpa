# Exercício 01
# Construa um código em python que leia um número do teclado e verifique se um número é primo.
num = int(input("Digite um número: "))
i = 0
cont = 0

if num > 1:
    for i in range(1, num):
        if num % i == 0:
            cont = cont + 1

    if cont > 1:
        print("O número", num, "não é primo.")
    else:
        print("O número", num, "é primo.")
else:
    print("O número", num, "não é primo.")


# Exercício 02
# Escreva um código em python que verifique se uma string é um palíndromo, ou seja, uma palavra que se escreve do mesmo jeito de trás para frente. Exemplo de palíndromo: 'radar'.

palavra_digitada = str(input("Digite uma palavra:"))
palavra_em_minusculo = palavra_digitada.lower()
palavra_de_tras_para_frente = palavra_em_minusculo[::-1]

if palavra_de_tras_para_frente == palavra_em_minusculo:
    print(palavra_digitada+" se escreve do mesmo jeito de trás para frente.")
else:
    print("A palavra "+palavra_digitada+" não é um palíndromo")

# Exercício 03
# Escreva um código em python leia uma palavra e um caractere, e apague todas as ocorrências desse caractere na palavra.
texto = input('Digite uma palavra: ')
caractere = input('Digite o caractere que será removido: ')

for letras in texto:
    if(letras in caractere):
        texto_sem_caractere = texto.replace(letras,'')

print(f"A palavra {texto} sem o caractere {caractere} fica {texto_sem_caractere}")   


