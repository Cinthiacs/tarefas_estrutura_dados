'''4. Faça um programa que converta da notação de 24 horas para a notação de 12
horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é
dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a
conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’
para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um
parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o
usuário repita esse cálculo para novos valores de entrada todas as vezes que
desejar.'''

from datetime import datetime

def exibe_hora(hora,min):
    if hora >= 12 and hora <= 24:
        print(f'Agora são {hora} : {min} PM')

    else:
        print(f'Agora são {hora} : {min} AM')

def converte_hora(hora_usu):
    for h in hora:
        
continuar = True

while continuar:

    hora_atual = datetime.now().time()
    hora = int(hora_atual.strftime('%H'))
    min = hora_atual.strftime('%M')

    exibe_hora(hora,min)

    hora_usu = int(input('Olá Usuário, digite um valor dentro das 24 horas abaixo:\r\n'))

    min_usu = int(input('Olá Usuário, digite um valor dentro dos 60 minutos abaixo:\r\n'))

    exibe_hora(hora_usu,min_usu)    

    while True:
        resposta_usu = input('Deseja inserir um novo valor novamente? Digite S/N \r\n')

        if resposta_usu == 'S':
            continuar = True
        elif resposta_usu == 'N':
            continuar = False
            break
        else:   
            print('Voce digitou incorretamente:')
