# Parâmetros com valores padrão

# Podemos pré-definir valores padrão para parâmetros. Assim, se ao chamarmos uma função e não passarmos valores para estes
# parâmetros, automaticamente eles adotarão os valores padrões definidos em suas declarações.

# Este primeiro exemplo apresenta quatro parâmetros e não define valores padrão. Logo ao realizar a chamada deve-se passar
# todos os valores para cada parâmetro ou indica-los como vazios passando "".

def dados_usuario(nome, cpf, email, pais):
    print("Nome: " + nome)
    print("CPF: " + cpf)
    print("E-mail: " + email)
    print("País: " + pais)

dados_usuario("Bilbo Bolseiro", "123.456.789-10", "bilbinho@email.com", "Condado")


# Já no caso abaixo, note que os parâmetros de email e pais estão com valores pré-definidos na declaração da função.
# Logo, quando estes parâmetros não forem passados na chamada da função, eles vão automaticamente atribuir o 
# valor que está como padrão na função.

# Importante ressaltar que os parâmetros que tem valores padrão devem sempre estar definidos em sequência
# ao final da lista de parâmetros.

def dados_usuario_padrao(nome, cpf, email = "Não informado", pais = "Não informado"):
    print("Nome: " + nome)
    print("CPF: " + cpf)
    print("E-mail: " + email)
    print("País: " + pais)

dados_usuario_padrao("Gollum", "000.000.000-10")