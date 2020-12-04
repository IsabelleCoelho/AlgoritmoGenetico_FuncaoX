from Individuo import Individuo
import random

def ordena(a):
    return a.funcaoX

class AlgoritmoGenetico:
    def __init__(self,tamanhoPopulacaoInicial=4, epocas=5):
        self.listaIndividuos = []
        self.resultado = None
        self.epocas = epocas
        self.preencher(tamanhoPopulacaoInicial)
        self.solucao()

    def preencher(self, tamanhoPopulacaoInicial):
        for _ in range(tamanhoPopulacaoInicial):
            individuo = Individuo()
            individuo.funcaoX = self.calcularFuncaoObjetivo(individuo.valorDecimal)
            self.listaIndividuos.append(individuo)

    def calcularFuncaoObjetivo(self, x):
        return ((x*x) - (3*x) + 4)

    def mutacao(self, filhos):
        posicaoEscolhida = int(random.uniform(0, len(filhos)))
        bitEscolhido = int(random.uniform(0, 5))
        filhos[posicaoEscolhida].valorBinario[bitEscolhido] = 1 if filhos[posicaoEscolhida].valorBinario[bitEscolhido] == 0 else 0
        if not filhos[posicaoEscolhida].analiseExistencia():
            filhos.remove(filhos[posicaoEscolhida])
        return filhos

    def crossover(self, pais):
        novosFilhos = []
        listaAuxiliar = []
        for i in range(3):
            listaAuxiliar.append(pais[0].valorBinario[i])
        listaAuxiliar.append(pais[1].valorBinario[3])
        listaAuxiliar.append(pais[1].valorBinario[4])
        novosFilhos.append(Individuo(listaAuxiliar))
        for i in range(3):
            listaAuxiliar.append(pais[1].valorBinario[i])
        listaAuxiliar.append(pais[0].valorBinario[3])
        listaAuxiliar.append(pais[0].valorBinario[4])
        novosFilhos.append(Individuo(listaAuxiliar))

        elementosRemover = []
        for i in range(len(novosFilhos)):
            if novosFilhos[i].valorDecimal == None:
                elementosRemover.append(novosFilhos[i])
        for elemento in elementosRemover:
            novosFilhos.remove(elemento)
        for i in range(len(novosFilhos)):
            novosFilhos[i].funcaoX = self.calcularFuncaoObjetivo(novosFilhos[i].valorDecimal)
        #analisando se ocorrera mutacao
        testeMutacao = random.uniform(0,101)
        if testeMutacao <= 1 and len(novosFilhos) > 0:
            return self.mutacao(novosFilhos)
        else:
            return novosFilhos

    def solucao(self):
        epocaAtual = 1
        while epocaAtual <= self.epocas:
            pais = []
            #aplicando o torneio
            for _ in range(2):
                posUm = int(random.uniform(0,len(self.listaIndividuos)))
                posDois = int(random.uniform(0,len(self.listaIndividuos)))
                if(self.listaIndividuos[posUm].funcaoX >= self.listaIndividuos[posDois].funcaoX):
                    pais.append(self.listaIndividuos[posUm])
                else:
                    pais.append(self.listaIndividuos[posDois])
            #analisando se ocorrera crossover
            testeCrossover = int(random.uniform(0,101))
            filhos = []
            if testeCrossover <= 70:
                filhos = self.crossover(pais)
            #atualizando a geracao
            self.listaIndividuos.sort(key=ordena)
            if len(filhos) > 0:
                filhos.sort(key=ordena,reverse=True)
                for i in range(len(filhos)):
                    trocou = False
                    posicaoTroca = 0
                    while posicaoTroca < len(self.listaIndividuos) and (not trocou):
                        if filhos[i].funcaoX > self.listaIndividuos[posicaoTroca].funcaoX:
                            self.listaIndividuos[posicaoTroca] = filhos[i]
                            trocou = True
                        posicaoTroca += 1

            self.resultado = self.listaIndividuos[-1].valorDecimal
            print("Epoca atual: {} |".format(epocaAtual), end=" ")
            self.printIndividuos()
            epocaAtual += 1
        print("O valor de X que leva a funcao x^2 -3x + 4 a obter seu valor maximo e: {}".format(self.resultado))

    def printIndividuos(self):
        for individuo in self.listaIndividuos:
            print(individuo.valorDecimal, end=" ")
        print()
if __name__ == "__main__":
    AlgoritmoGenetico()