#Televisao
#marca, modelo, ligada, volume, canal
#ligarDesligar()
#aumentarVolume()
#diminuirVolume()
#trocarCanal(int)
#mostrarStatus() 

class Televisao:      
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligada = False
        self._volume = 50
        self._canal = 1

    def ligarDesliar(self):
        self._ligada = not self._ligada
        if self._ligada:
            print(f"A TV {self._marca} {self._modelo} está ligada.")
        else:
            print(f"A TV {self._marca} {self._modelo} está desligada.")

    def aumentarVolume(self):
        if self._ligada and self._volume < 100:
            self._volume += 1
            print(f"Volume aumentado para {self._volume}.")

    def diminuirVolume(self):
        if self._ligada and self._volume > 0:
            self._volume -= 1
            print(f"Volume diminuído para {self._volume}.")

    def trocarCanal(self, novo_canal):
        if self._ligada:
            self._canal = novo_canal
            print(f"Canal alterado para {self._canal}")

    def mostrarStatus(self):
        print(f"Marca: {self._marca}")
        print(f"Modelo: {self._modelo}")
        print(f"TV {'ligada' if self._ligada else 'desligada'}")
        print(f"Volume: {self._volume}")
        print(f"Canal: {self._canal}")

tv1 = Televisao("Sony", "Bravia")
tv1.mostrarStatus()
tv1.aumentarVolume()
tv1.mostrarStatus()


#Parâmetros default
#def __init__(self, marca="Desconhecida", modelo="Desconhecido"):
#
#Pode ser criada sem parâmetros
#tv2 = Televisao()
#ou pode alterar os dados de forma posicional
#tv3 = Televisao("LG","LED45")
#ou podem ser usados parâmetros nomeados
#tv4 = Televisao(modelo="Samsung", marca="SmartTV")


