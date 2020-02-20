numbers = [5,3,8,1,4,9,7,2,6]

def insertionSort(numbers):
    # for every element in our array
    for x in range(1, len(numbers)):
        key = numbers[x]
        y = x

        while y > 0 and numbers[y-1] > key:
            #print("Swapped {} for {}".format(my_list[position], my_list[position-1]))
            numbers[y] = numbers[y-1]
            #print(numbers)
            y -= 1

        numbers[y] = key

    return numbers


print(insertionSort(numbers))