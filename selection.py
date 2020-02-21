numbers = [5,7,2,8,9,1,3,6,4]

def selectionSort(numbers):
    for x in range(len(numbers)):
        min = x
        for y in range(x + 1, len(numbers)): 
            print("unsorted element is " +str(numbers[x]))
            if numbers[y] < numbers[min]:
                min = y
                
        aux = numbers[x]
        numbers[x] = numbers[min]
        numbers[min] = aux
        print("swap")
        print(numbers)
    return numbers

print(selectionSort(numbers))