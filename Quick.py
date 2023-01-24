def quickSort(array, left, right):
    if left < right:
        partitionPosition = partition(array, left, right)
        quickSort(array, left, partitionPosition - 1)
        quickSort(array, partitionPosition + 1, right)


def partition(array, left, right):
    i = left
    j = right - 1
    pivot = array[right]

    while i < j:

        while i < right and array[i] < pivot:
            i += 1
        while j > left and array[j] >= pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]

    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]

    return i


array = [40, 97, 41, 3, 6, 79, 7, 62, 83, 91]
