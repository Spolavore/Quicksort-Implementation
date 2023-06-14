import random as r
def particionamento_lomuto(arr, start, end):
    pivo = arr[start]
    print(f'pivo: {pivo}, arr: {arr}')
    storeIndex = start + 1
    i = start + 1
    while(i <= end):
        if arr[i] <= pivo:
            ( arr[storeIndex], arr[i]) = (arr[i], arr[storeIndex])
            storeIndex = storeIndex + 1
        i += 1
    (arr[storeIndex-1], arr[start]) = (arr[start], arr[storeIndex-1])
    print(f'ordenacao: {arr}')
    return storeIndex-1



def quicksort(arr, start, end):
    if start < end: 
        if tipoDePivo == 2: # randomiza caso o usuario escolher esse tipo de particionador
            random = r.randint(start,end)
            arr[random], arr[start] = arr[start], arr[random]
        if tipoDePivo == 1: # pega a mediana do array caso o usuario escolha esse tipo de randomizacao
            if arr[start] > arr[len(arr)//2]:
                arr[start], arr[len(arr)//2] = arr[len(arr)//2], arr[start]
            if arr[len(arr)-1] < arr[len(arr)//2]:
                arr[len(arr)-1], arr[len(arr)//2] = arr[len(arr)//2], arr[len(arr)-1]    
            arr[len(arr)//2], arr[start] = arr[start], arr[len(arr)//2]

        pivo = particionamento_lomuto(arr, start, end)
        quicksort(arr, start, pivo-1)
        quicksort(arr, pivo+1, end)


arr2 = [-5, 10, 3 , 0 , 1 , 6, -200, 30 ,2 , 5, 3, 4, -5]
arr = [-5, 10, 3 , 0 , 1]

tipoDePivo = int(input('(1) Mediana de três \n(2) Randomizado\nEscolha a estratégia de particionamento: '))
quicksort(arr2, 0, len(arr2) - 1)
print(arr2)



