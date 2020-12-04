import random

dicionarioNumeros = {
    -10 : [1,0,1,1,0], -9 : [1,0,1,1,1], -8 : [1,1,0,0,0], -7 : [1,1,0,0,1], -6 : [1,1,0,1,0],
    -5 : [1,1,0,1,1], -4 : [1,1,1,0,0], -3 : [1,1,1,0,1], -2 : [1,1,1,1,0], -1 : [1,1,1,1,1],
    0 : [0,0,0,0,0], 1 : [0,0,0,0,1], 2 : [0,0,0,1,0], 3 : [0,0,0,1,1], 4 : [0,0,1,0,0],
    5 : [0,0,1,0,1], 6 : [0,0,1,1,0], 7 : [0,0,1,1,1], 8 : [0,1,0,0,0], 9 : [0,1,0,0,1],
    10 : [0,1,0,1,0]
}

class Individuo:
    def __init__(self, valorBinario=[]):
        self.funcaoX = None
        if len(valorBinario) == 0 :
            self.valorDecimal = int(random.uniform(-11,11))
            self.valorBinario = dicionarioNumeros[self.valorDecimal]
        else:
            self.valorBinario = valorBinario
            self.valorDecimal = self.calcularValorDecimal()

    def calcularValorDecimal(self):
        for chave in dicionarioNumeros.keys():
            if dicionarioNumeros[chave] == self.valorBinario:
                return chave

    def analiseExistencia(self):
        for chave in dicionarioNumeros.keys():
            if dicionarioNumeros[chave] == self.valorBinario:
                return True
        return False


