from typing import List, Tuple

#Polimofismo
class Curso:
    def __init__(self: object, nome: str = 'Curso Padrão', carga_horaria: int = 45) -> None:
        self.__nome = nome
        self.__carga_horaria = carga_horaria
        
curso1: Curso = Curso()
curso2: Curso = Curso(nome= 'Design Patterns in Python')
curso3: Curso = Curso(nome= 'SQL Alchemy', carga_horaria=23)

print(curso1.__dict__)
print(curso2.__dict__)
print(curso3.__dict__)


#Mesma implementação com tipos diferentes
nome: str = 'Geek University'
tupla: Tuple = (1, 2, 3, 4, 5)
lista: List = [1, 2, 3, 4, 5]

print(nome[:4], tupla[:4], lista[:4])

#Herança
class Pessoa:
    def __init__(self: object, nome: str) -> None:
        self.__nome = nome
    
    def andar(self: object) -> None:
        print(f'{self.__nome} está andando')

class Aluno(Pessoa):
    def __init__(self: object, nome: str, matricula: str) -> None:
        super().__init__(nome)
        self.__matricula = matricula

mathias = Aluno('Mathias', '192657')
mathias.andar()

#Abstração
def gerar_fibonacci(qtd: int) -> None:
    if qtd <= 0:
        print('A quantidade deve ser maior que 0')
    else:
        print(f'A sequência Fibonacci para {qtd} termo(s) é: ')
        contador: int = 0
        aux1: int = 0
        aux2: int = 1
        while contador < qtd:
            print(aux1)
            proximo = aux1 + aux2
            aux1, aux2 = aux2, proximo
            contador += 1
            
gerar_fibonacci(10)


#Composição
class Motor:
    def ligar(self: object) -> None:
        print('Motor ligando...')
    
class Pneu:
    def encher(self: object) -> None:
        print('Pneu cheio')

class Carro:
    def __init__(self: object, modelo: str) -> None:
        self.__modelo = modelo
        self.__motor = Motor()
        self.__pneu1 = Pneu()
        self.__pneu2 = Pneu()
        self.__pneu3 = Pneu()
        self.__pneu4 = Pneu()

ferrari = Carro('Ferrari')
ferrari._Carro__motor.ligar()
