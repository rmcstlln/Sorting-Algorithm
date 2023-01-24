def bubbleSort(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                print(array)


array = [40, 97, 41, 3, 6, 79, 7, 62, 83, 91]
bubbleSort(array)
print(array)
