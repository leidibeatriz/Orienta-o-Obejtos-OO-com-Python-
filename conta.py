class Conta: #criando a classe Conta

    def __init__(self, numero, titular, saldo, limite): #definindo o construtor
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero #definindo os atributos
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self): #definindo os objetos
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor): #definindo os objetos
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): #definindo os objetos
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor): #definindo os objetos
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transfere(self, valor, destino): #definindo os objetos
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):  #definindo os objetos como privado
        return self.__saldo

    @property
    def get_titular(self): #definindo os objetos como privado
        return self.__titular

    @property
    def limite(self): #definindo os objetos como privado
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco(): #definindo os objetos como estático ou seja esse valor não pode mudar
        return "001"

    @staticmethod
    def codigos_bancos(): #definindo os objetos como estático ou seja esse valor não pode mudar
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}