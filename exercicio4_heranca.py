class Produto:
    def __init__(self, codigo ="", nome="", preco=""):
        self._codigo    = codigo
        self._nome      = nome
        self._preco     = preco

    def informacoes(self):
        print(f"Codigo: {self._codigo}")
        print(f"Nome: {self._nome}")
        print(f"Preco: {self._preco}")  


class ProdutoEletronico(Produto):
    def __init__(self, codigo="", nome="", preco="",mesesGarantia=""):
        super().__init__(codigo, nome, preco)
        self._mesesGarantia =   mesesGarantia

    def informacoes(self):
        print(f"Codigo: {self._codigo}")
        print(f"Nome: {self._nome}")
        print(f"Preco: {self._preco}")  
        print(f"Meses Garantia: {self._mesesGarantia}") 

class ProdutoAlimenticio(Produto):
    def __init__(self, codigo="", nome="", preco="",dataValidade = ""):
        super().__init__(codigo, nome, preco)
        self._dataValidade  =   dataValidade

    def informacoes(self):
        print(f"Codigo: {self._codigo}")
        print(f"Nome: {self._nome}")
        print(f"Preco: {self._preco}")     
        print(f"Data Validade: {self._dataValidade}")


p1  = Produto(codigo= 8, nome="Bolas", preco="R$5,00")
pE1  = ProdutoEletronico(codigo= 24, nome="Notebook", preco="R$2.500,00", mesesGarantia= 24) 
pA1  = ProdutoAlimenticio(codigo= 34, nome="Banana", preco="R$15,00", dataValidade="19/10/2023")

print()
p1.informacoes()
pE1.informacoes()
pA1.informacoes()