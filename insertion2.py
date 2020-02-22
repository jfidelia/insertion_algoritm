numbers = [5,3,8,1,4,9,7,2,6]

def insertionSort(numbers):
  for x in range(1, len(numbers)):
    key = numbers[x]
    y = x-1
    print('if '+str(numbers[x])+' is less than '+str(numbers[x-1]))
    while y >= 0 and key < numbers[y]:
        numbers[y+1] = numbers[y]
        print("swap")
        print(numbers)
        y -= 1
        print("y is "+str(y))
    print("Time to put back key ("+str(key)+") into the position: "+str(y+1))
    numbers[y+1] = key
    print("The new array is: "+str(numbers))
  return numbers

print(' '.join([str(elem) for elem in insertionSort(numbers)]))
