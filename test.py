# Python program for implementation of Insertion Sort 
numbers = [5,3,8,1,4,9,7,2,6]
#numbers = [5,3,8,1,4,9,7,2,6]
# Function to do insertion sort 
def insertionSort(numbers): 

	# Traverse through 1 to len(arr) 
	for i in range(1, len(numbers)): 

		key = numbers[i] 

		# Move elements of arr[0..i-1], that are 
		# greater than key, to one position ahead 
		# of their current position 
		j = i-1
		while j >= 0 and key < numbers[j] : 
				numbers[j + 1] = numbers[j] 
				j -= 1
		numbers[j + 1] = key 


# Driver code to test above  
insertionSort(numbers) 
for i in range(len(numbers)): 
	print ("% d" % numbers[i]) 

print(numbers)

# This code is contributed by Mohit Kumra 
