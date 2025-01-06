""" Modulo que é usado para gerar um cpf aleatorio"""

import random
import subprocess
from main import terminal_interface

def gerador_digitos_aleatorios():
    lista_digitos = []

    for digito in range(0,9):
        digito_string = str(random.randint(0,9))
        lista_digitos.append(digito_string)

    return lista_digitos

def colocando_ponto_cpf(cpf_validado):
    resultado = ''
    for contador,digito in enumerate(cpf_validado):
        if contador == 3 or contador == 6:
            resultado += '.'
        elif contador == 9:
            resultado += '-'
        resultado += digito
    return resultado

def calculo_de_digitos(lista_de_digitos):
    contador = len(lista_de_digitos) + 1
    soma_digitos = 0 
    for digito in lista_de_digitos:
        soma_digitos = soma_digitos + (int(digito) * contador)
        contador -= 1

    resultado = (soma_digitos * 10) %11
    
    if resultado > 9:
        resultado = 0
    
    return str(resultado)

lista_digitos_cpf = gerador_digitos_aleatorios()

primeiro_digito = calculo_de_digitos(lista_digitos_cpf)
lista_digitos_cpf.append(primeiro_digito)
segundo_digito = calculo_de_digitos(lista_digitos_cpf)
lista_digitos_cpf.append(segundo_digito)

cpf_validado = ''.join(lista_digitos_cpf)
cpf_validado_com_ponto = colocando_ponto_cpf(cpf_validado)


terminal_interface('GERADOR CPF')
print(f'CPF GERADO SEM PONTO: {cpf_validado}')
print(f'CPF GERADO COM PONTO: {cpf_validado_com_ponto}')

subprocess.call(['Python','main.py'])
