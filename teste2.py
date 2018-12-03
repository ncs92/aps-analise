from time import time
from random import *


n_inst_quick = 0
n_inst_merge = 0
n_inst_maxVetor = 0
n_inst_heap = 0

v1 = []
v2 = []
v3 = []

def carregaVetor(arquivo):
    arq = open(arquivo)
    return [int(num) for num in arq.read().split(' ') if num != '']

def carregaArquivoVetor():
    global v1, v2, v3
    #gerar1000()
    #gerar10000()
    #gerar100000()
    v1 = carregaVetor('./arq-1000.txt')
    v2 = carregaVetor('./arq-10000.txt')
    v3 = carregaVetor('./arq-100000.txt')

def calculaSub(vetor):
	soma = 0
	e = 1
	d = 1
	n_inst = 0
	maior_soma = vetor[1]
	for i in range(0, len(vetor)-1):
		n_inst += 1
		for j in range(i, len(vetor)):
			n_inst += 1
			soma = soma + vetor[j]
			if soma > (maior_soma):
				maior_soma = soma
				e = i
				d = j
		soma = 0
	return maior_soma, n_inst

def calculaSubvetorMaximo():
    tempo_inicial_v1 = time()
    v11 = v1.copy()
    soma, n = calculaSub(v11)
    tempo_final_v1 = time() - tempo_inicial_v1
    arquivo = open("resultado_1000_subVetorMaximo.txt", 'w+')
    cab = "instructions: " + str(n) + ", tempo: " + str(tempo_final_v1) + ", soma: " + str(soma) + "\n"
    print(cab)
    arquivo.writelines(cab)
    arquivo.close()
    
    tempo_inicial_v2 = time()
    v22 = v2.copy()
    soma, n = calculaSub(v22)
    tempo_final_v2 = time() - tempo_inicial_v2
    arquivo = open("resultado_10000_subVetorMaximo.txt", 'w+')
    cab = "instructions: " + str(n) + ", tempo: " + str(tempo_final_v2) + ", soma: " + str(soma) + "\n"
    arquivo.writelines(cab)
    arquivo.close()
    
    tempo_inicial_v3 = time()
    v33 = v3.copy()
    soma, n = calculaSub(v33)
    tempo_final_v3 = time() - tempo_inicial_v3
    arquivo = open("resultado_100000_subVetorMaximo.txt", 'w+')
    cab = "instructions: " + str(n) + ", tempo: " + str(tempo_final_v3) + ", soma: " + str(soma) + "\n"
    arquivo.writelines(cab)
    arquivo.close()
    
if __name__ == '__main__':
    carregaArquivoVetor()
    #ordenaBubble()
    #ordenaInsertion()
    #ordenaSelection()
    #ordenaQuick()
    #ordenaMerge()
    #ordenaHeap()
    #ordenaBubbleSortMelhorado()
    #calculaPesquisaBinaria()
    calculaSubvetorMaximo()