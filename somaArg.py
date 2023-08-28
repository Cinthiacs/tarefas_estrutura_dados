'''3. Faça um programa, com uma função que necessite de três argumentos, e que
forneça a soma desses três argumentos.'''

args = [0,0,0]
num_usuario = []

for i in range (len(args)):
    while True:
        numero_digitado = input('Olá Usuário(a) digite um numero inteiro\r\n')

        if numero_digitado.isdigit():
            numero_usuario = int(numero_digitado)
            num_usuario.append(numero_usuario)
            break
        else:   
            print('Você digitou incorretamente')

soma_total = sum(num_usuario)
print(f'A soma dos tres valores é {soma_total}')