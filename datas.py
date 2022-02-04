
class Data: #definindo a classe data
    def __init__(self,dia,mes,ano): #definindo o construtor
        self.dia = dia
        self.mes = mes #atributos
        self.ano = ano

    def imprime_data(self,dia,mes,ano): #objeto
        print("{}/{}/{}".format(self.dia,self.mes,self.ano)) #imprimindo




