import sys
import random as r 
import time
# codigo visto em aula
def particionamento_lomuto(arr, start, end):
    global swaps
    pivo = arr[start]
    storeIndex = start + 1
    i = start + 1
    while(i <= end):
        if arr[i] <= pivo:
            (arr[storeIndex], arr[i]) = (arr[i], arr[storeIndex])
            swaps+=1
            storeIndex = storeIndex + 1
        i += 1
    (arr[storeIndex-1], arr[start]) = (arr[start], arr[storeIndex-1])
    swaps+=1
    return storeIndex-1

# codigo visto em aula
def particionamento_hoare(arr, low, high):
    global swaps
    chave = arr[low]
    i = low + 1
    j = high
    
    while True:
        while arr[i] <= chave:
            if i == high:
                break
            i = i + 1
        while chave < arr[j]:
            if j == low:
                break
            j = j - 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        swaps+=1
    arr[low], arr[j] = arr[j], arr[low]
    swaps+=1
    return j
        
    
def quicksort(arr, start, end):
    global recursoes
    recursoes+=1
    if start < end: 
        # pega a mediana de tres (first, middle and end) do array caso o usuario escolha esse tipo de particionador
        if tipoDePivo == 1:
            if arr[start] > arr[end//2]:
                arr[start], arr[end//2] = arr[end//2], arr[start]
            if arr[end] < arr[end//2]:
                arr[end], arr[end//2] = arr[end//2], arr[end]    
            arr[end//2], arr[start] = arr[start], arr[end//2]

        # randomiza caso o usuario escolher esse tipo de particionador
        if tipoDePivo == 2:
            random = r.randint(start,end)
            arr[random], arr[start] = arr[start], arr[random]

        # Usa o particionamento de Lomuto ao ser selecionado 1
        if tipoDeParticionamento == 1:
            pivo = particionamento_lomuto(arr, start, end)

        # Usa o particionamento de Hoare ao ser selecionado 2
        if tipoDeParticionamento == 2:
            pivo = particionamento_hoare(arr,start,end)
        quicksort(arr, start, pivo-1)
        quicksort(arr, pivo+1, end)



if __name__ == '__main__':
    arr2 = [-5, 10, 3 , 0 , 1 , 6, -200, 30 ,2 , 5, 3, 4, -5, 1000, 3213, -4 , -4 , 5 , -1000, 0 , 1321, 31]

    tipoDePivo = int(input('(1) Mediana de três \n(2) Randomizado\nEscolha a estratégia de particionamento: '))
    tipoDeParticionamento = int(input('(1) Lomuto\n(2) Hoare\nEscolha o tipo de particionamento: '))
    swaps = 0
    recursoes = 0

    if tipoDePivo == 1 and tipoDeParticionamento == 1:
        arquivo_saida = 'stats-mediana-lomuto.txt'
    if tipoDePivo == 1 and tipoDeParticionamento == 2:
        arquivo_saida = 'stats-mediana-hoare.txt'
    if tipoDePivo == 2 and tipoDeParticionamento == 1:
        arquivo_saida = 'stats-aleatorio-lomuto.txt'
    if tipoDePivo == 2 and tipoDeParticionamento == 2:
        arquivo_saida = 'stats-aleatorio-hoare.txt'

    if len(sys.argv) == 2:
        arquivo_entrada = sys.argv[1]   #Pega o primeiro argumento da linha de comando pra ser o nome do arquivo de entrada, senão por padrão é o arquivo entrada-quicksort.txt
    else:
        arquivo_entrada = 'entrada-quicksort.txt'  

    with open (arquivo_saida, 'w'):
        pass  #limpa o arquivo de saída
    with open(arquivo_entrada, 'r') as arq:
        for linha in arq:
            linha = linha.split()
            linha = list(map(int,linha)) #transforma a linha do arquivo de entrada em um vetor com os números
            tamanho = linha[0]
            linha.remove(linha[0]) #remove o primeiro elemento do vetor q indica o tamanho do vetor
            tempo_inicial = time.perf_counter()
            quicksort(linha, 0, tamanho - 1)
            tempo_final = time.perf_counter()
            tempo_total = (tempo_final - tempo_inicial)*1000
            tempo_total = format(tempo_total, '.4f')
            with open(arquivo_saida, 'a') as arq_saida:
                arq_saida.write("TAMANHO ENTRADA " + str(tamanho) + '\n')
                arq_saida.write("SWAPS " + str(swaps) + '\n')
                arq_saida.write("RECURSOES " + str(recursoes) + '\n')            
                arq_saida.write("TEMPO EM MILISSEGUNDOS "+ str(tempo_total) + '\n')    
    
    
    



