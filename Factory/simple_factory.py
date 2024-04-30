from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print('Au Au Au')

class Gato(Animal):
    def falar(self):
        print('Miau')

class Peru(Animal):
    def falar(self):
        print('Pruuu')
        
#Factory
class Factory:
    def criar_animal_falante(self, tipo):
        # return eval(tipo)().falar()
        return eval(tipo)()
    
#Client
if __name__ == '__main__':
    fab = Factory()
    animal = input('Qual animal você quer que fale? [Cachorro, Gato, Peru] ')
    obj = fab.criar_animal_falante(animal)
    obj.falar()