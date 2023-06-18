import random as r 
# codigo visto em aula
def particionamento_lomuto(arr, start, end):
    pivo = arr[start]
    storeIndex = start + 1
    i = start + 1
    while(i <= end):
        if arr[i] <= pivo:
            ( arr[storeIndex], arr[i]) = (arr[i], arr[storeIndex])
            storeIndex = storeIndex + 1
        i += 1
    (arr[storeIndex-1], arr[start]) = (arr[start], arr[storeIndex-1])
    return storeIndex-1

# codigo visto em aula
def particionamento_hoare(arr, low, high):
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
    arr[low], arr[j] = arr[j], arr[low]
    return j
        
    
def quicksort(arr, start, end):
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
    quicksort(arr2, 0, len(arr2) - 1)
    print(arr2)