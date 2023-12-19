class Veiculo:
    def __init__(self, marca="", modelo="",ano=""):
        self._marca   = marca
        self._modelo  = modelo
        self._ano     = ano


    def mostrar_informacoes(self):
        print(f"Marca: {self._marca}")
        print(f"Modelo: {self._modelo}")
        print(f"ano: {self._ano}")

class Carro(Veiculo):
    def __init__(self, marca="", modelo="",ano="",num_portas="") :
        super().__init__(marca="", modelo="",ano="")
        self._num_portas    = num_portas

    def mostrar_informacoes(self):
        print(f"Marca: {self._marca}")
        print(f"Modelo: {self._modelo}")
        print(f"ano: {self._ano}")
        print(f"num_portas: {self._num_portas}") 


class Moto(Veiculo):
    def __init__(self, marca="", modelo="",ano="",cilindrada=""):
        super().__init__(marca="", modelo="",ano="")
        self._cilindrada    = cilindrada

    def mostrar_informacoes(self):
        print(f"Marca: {self._marca}")
        print(f"Modelo: {self._modelo}")
        print(f"ano: {self._ano}")  
        print(f"cilindrada: {self._cilindrada}")    


v1= Veiculo(marca="Fiat", modelo="Uno",ano=2016)
car1= Carro(marca="Fiat", modelo="Uno",ano=2016,num_portas=4)
mot1= Moto(marca="Yamaha", modelo="FZ25",ano=2024,cilindrada=250)


print()
v1.mostrar_informacoes()
car1.mostrar_informacoes()
mot1.mostrar_informacoes()

