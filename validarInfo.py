'''Faça um programa que leia e valide as seguintes informações (crie sua própria
função):
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''
def validar_nome(nome):
    return len(nome) > 3

def validar_idade(idade):
    return 0 <= idade <= 150

def validar_salario(salario):
    return salario > 0

def validar_sexo(sexo):
    return sexo in ['f', 'm']

def validar_estado_civil(estado_civil):
    return estado_civil in ['s', 'c', 'v', 'd']

nome = input("Digite seu nome: ")
while not validar_nome(nome):
    print("Nome inválido. Deve ter mais de 3 caracteres.")
    nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))
while not validar_idade(idade):
    print("Idade inválida. Deve estar entre 0 e 150.")
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salário: "))
while not validar_salario(salario):
    print("Salário inválido. Deve ser maior que zero.")
    salario = float(input("Digite seu salário: "))

sexo = input("Digite seu sexo (f/m): ")
while not validar_sexo(sexo):
    print("Sexo inválido. Deve ser 'f' ou 'm'.")
    sexo = input("Digite seu sexo (f/m): ")

estado_civil = input("Digite seu estado civil (s/c/v/d): ")
while not validar_estado_civil(estado_civil):
    print("Estado civil inválido. Deve ser 's', 'c', 'v' ou 'd'.")
    estado_civil = input("Digite seu estado civil (s/c/v/d): ")

print("Informações válidas. Obrigado!")