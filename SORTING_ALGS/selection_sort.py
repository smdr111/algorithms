def selection_sort(array: list) -> list:
    
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i+1,len(array)):
            if array[j] < array[min_index]:
                min_index = j
        
        if i != min_index:
            array[min_index], array[i] = array[i], array[min_index]
    return array
