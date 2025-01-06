""" Modulo que executa a função numero 1 do main"""

from main import terminal_interface
import subprocess

# inicio funcoes para validar o cpf digitado

def retira_a_pontuacao(cpf_digitado):
    pontuacoes_invalidas = '.- '
    cpf_sem_pontuacao = ''
    for digito in cpf_digitado:
        if digito not in pontuacoes_invalidas:
            cpf_sem_pontuacao += digito
    return cpf_sem_pontuacao

def validador_letras_cpf(cpf_sem_ponto: str):
    if cpf_sem_ponto.isnumeric() == False:
        print('Existe uma letra nos digitos digite corretamente! ')
        return subprocess.call(['Python','main.py'])
    
def pegando_nove_digitos(cpf_sem_ponto):
    lista_digitos = []
    for contador,cpf in enumerate(cpf_sem_pontuacao):
        if contador < 9:
            lista_digitos.append(cpf)
        else:
            return lista_digitos
        
# fim funcoes para validar o cpf digitado

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


terminal_interface('Verificador se cpf é valido.')
lista_de_digitos = []

cpf_digitado = input('Digite o cpf: ')
cpf_sem_pontuacao = retira_a_pontuacao(cpf_digitado)

validador_letras_cpf(cpf_sem_pontuacao)



if len(cpf_sem_pontuacao) > 11:
    print('SEU CPF TEM MAIS DIGITOS QUE O NECESSARIO')
    subprocess.call(['Python','main.py'])
elif len(cpf_sem_pontuacao) < 11:
    print('SEU CPF TEM MENOS DIGITOS QUE O NECESSARIO')
    subprocess.call(['Python','main.py'])

lista_de_digitos = pegando_nove_digitos(cpf_sem_pontuacao)

primeiro_digito = calculo_de_digitos(lista_de_digitos)
lista_de_digitos.append(primeiro_digito)

segundo_digito = calculo_de_digitos(lista_de_digitos)
lista_de_digitos.append(segundo_digito)

cpf_validado = ''.join(lista_de_digitos)


if cpf_validado ==cpf_sem_pontuacao:
    print(f'CPF: {cpf_digitado} é valido!!')
else:
    print(f'CPF: {cpf_digitado} é invalido!!')

subprocess.call(['Python','main.py'])


