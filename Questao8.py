from abc import ABC, abstractmethod

"""Métodos abstratos"""

"""VANTAGEM:Nessas duas primeira classe mostramos o uso do método abstrato, os a classe 'jogador'
herda obrigatoriamente os métodos da classe mãe 'Jogadores', nesse caso a vantagem está 
primeiro em nao esquecer de implementar alguns métodos que são essenciais, nesse caso
os métodos 'mostrar_idade' e 'mostrar_altura' necessitam ser obrigatoriamente implementados
nas classes filhas da classe 'Jogadores' impedindo que as mesma sejam criadas sem os 
métodos obrigatorios."""

class Jogadores(ABC):
    @abstractmethod
    def mostrar_idade(self):
        pass

    @abstractmethod
    def mostrar_altura(self):
        pass


class jogador(Jogadores):
    def __init__(self, idade, altura):
        self.idade = idade
        self.altura = altura

    def mostrar_idade(self):
        return self.idade

    def mostrar_altura(self):
        return self.altura


"""Métodos de classe"""

"""No caso a seguir temos o método 'set_new_year' que é um método de classe e permite 
mudar um atributo da classe"""

"""Vantagem: Um método de classe permite que façamos alteraçoes na classe sem a 
necessidade de um objeto instanciado, nesse caso em específico o método em questão 
permite mudar o atributo (current_year) da classe sem acessar nenhum objeto instanciado 
mesmo que essa alterçao possa interferir neles, como nesse caso em que o atributo 'current_year
é utilizado no método get_born_year dos mesmos."""

class Pessoa:
    current_year = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_born_year(self):
        print(self.current_year - self.idade)

    @classmethod
    def set_new_year(cls, new_year):
        cls.current_year = new_year


    @staticmethod
    def random_number():
        x = randint(100, 999)
        return x

""" Métodos estáticos"""
"""No ultimo método implementado acima temos um método estatico que não usa como
referencia nem a classe nem o objeto da classe e sua pricipal vantagem está no desempenho
umavez que nao precisa acessar um objeto para começar sua execução"""