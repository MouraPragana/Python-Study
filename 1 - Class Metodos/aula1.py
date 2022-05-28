# Marca, Memoria Ram, Placa de vídeo
# python -m ensurepip
# python -m pip install --upgrade pip
# & C:/Python310/python.exe -m pip install -U pylint
# https://www.youtube.com/watch?v=j6B8shHXzks


class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def Ligar(self):
        print("Estou ligando")

    def Desligar(self):
        print("Estou desligando")

    def ExibirInformacoesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

    pass


computador1 = Computador("Asus", "8gb", "Nvidia")
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformacoesDesteComputador()
# computador2 = Computador("Dell", "10gb", "GeForce")
# computador3 = Computador("Acer", "16gb", "ATM")
