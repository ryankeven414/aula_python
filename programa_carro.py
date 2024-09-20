# Definição da classe Carro
class Carro:
    # O método __init__ é o construtor da classe e define os atributos de um carro.
    def __init__(self, codigo, fabricante, modelo, cor, valor, ano):
        # Atributos do carro
        self.codigo = codigo          # Código identificador do carro
        self.fabricante = fabricante  # Fabricante do carro (ex: Toyota, Ford)
        self.modelo = modelo          # Modelo do carro (ex: Corolla, Mustang)
        self.cor = cor                # Cor do carro
        self.valor = valor            # Valor do carro em reais (R$)
        self.ano = ano                # Ano de fabricação do carro

    # Método para calcular o valor das parcelas
    # O método solicita a quantidade de parcelas e divide o valor do carro pelo número de parcelas
    def calcular_parcelas(self):
        quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
        valor_parcela = self.valor / quantidade_parcelas
        return f"O valor de cada parcela para {quantidade_parcelas}x será: R$ {valor_parcela:.2f}"

    # Método para exibir os dados do carro
    # Este método solicita os dados do carro via input e exibe todas as informações
    def exibir_dados(self):
        self.codigo = input("Digite o código do carro: ")
        self.fabricante = input("Digite o fabricante do carro: ")
        self.modelo = input("Digite o modelo do carro: ")
        self.cor = input("Digite a cor do carro: ")
        self.valor = float(input("Digite o valor do carro (em R$): "))
        self.ano = input("Digite o ano de fabricação do carro: ")

        return (f"\nDados do carro:\n"
                f"Código: {self.codigo}\n"
                f"Fabricante: {self.fabricante}\n"
                f"Modelo: {self.modelo}\n"
                f"Cor: {self.cor}\n"
                f"Valor: R$ {self.valor:.2f}\n"
                f"Ano: {self.ano}")

# Exemplo de uso:
# Criando um objeto da classe Carro. Um objeto é uma instância da classe.
carro1 = Carro(0, '', '', '', 0.0, 0)

# Chamando o método exibir_dados para receber os dados do carro via input
print(carro1.exibir_dados())

# Chamando o método calcular_parcelas para calcular o valor das parcelas
print(carro1.calcular_parcelas())