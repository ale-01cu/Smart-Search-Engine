def intercambiar(array, i, j):
	aux = array[i]
	array[i] = array[j]
	array[j] = aux

def partition(array, primero, ultimo):
	p = array[primero]
	i = primero
	j = ultimo

	while i < j:
		while array[i] < p:
			i += 1
		while p <= array[j]:
			j -= 1
			if i < j: 
				intercambiar(array, i, j)

	return j

def Quicksort(array, primero, ultimo):
	if len(array) <= 1:
		return array

	k = partition(array, primero, ultimo)
	Quicksort(array, primero, k)
	Quicksort(array, k+1, ultimo)

def burbuja(array):
	length = len(array)
	desestructurado = []
 
	for i in range(0, length):
		for j in range(0, length-1):
			if array[j]['datos']['total'] < array[j+1]['datos']['total']:
				intercambiar(array, j, j+1)


