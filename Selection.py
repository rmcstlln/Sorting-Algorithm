def selectionSort(array):

    for i in range(9):
        minpos = i
        for j in range (i, 10):
            if array[j] < array[minpos]:
                minpos = j

        temp = array[i]
        array[i] = array[minpos]
        array[minpos] = temp

        print(array)


array = [40, 97, 41, 3, 6, 79, 7, 62, 83, 91]
