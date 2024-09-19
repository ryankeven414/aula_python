#criando a class chamada carro
class Carro:
    #def __init__(self,fabricante):
    def __init__(self,fabricante,modelo,cor,valor,ano,placa):
        #definido os atributos
        self.fabricante = fabricante
        self.modelo = modelo
        self.cor  = cor
        self.valor = valor
        self.ano  = ano
        self.placa  = placa
    

#criando objeto
celta=Carro("gm","celta","azul",12000,2012,"BDNI580")
print("carro",celta.modelo,"ano:",celta.ano)
    