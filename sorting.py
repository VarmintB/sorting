import time

def swap(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp

def bubble(array):
	for i in reversed(range(len(array))):
		for j in range(i):
			if array[j] >= array[j + 1]:
				swap(array, j, j + 1)

def selection(array):
	for i in range(len(array)):
		i_min = i
		for j in range(i + 1, len(array)):
			if array[j] < array[i_min]:
				i_min = j
		swap(array, i, i_min)

def insertion(array):
	for i in range(len(array)):
		j = i
		while j > 0 and array[j - 1] > array[j]:
			swap(array, j - 1, j)
			j -= 1
def minsearch(array):
        for i in range(len(array)):
                swap(array, array.index(min(array[i:])), i)

def case(name, array):
	switcher = {
		'bubble': bubble,
		'selection': selection,
		'insertion': insertion,
                'minsearch': minsearch
	}
	func = switcher.get(name, lambda: 'No such sort method')
	return func(array)

if __name__ == '__main__':

	methods = ['bubble', 'selection', 'insertion', 'minsearch']
	times = dict()

	# print("Input a list. Leave input empty when you are done.")
	numbers = list()
	# while True:
        #
	# 	elem = input()
	# 	if elem is '':
	# 		break
	# 	numbers.append(int(elem))

	for i in range(1000):
		if i % 2:
			i = -i
		numbers.append(i)

	for i in range(2):

		temp = numbers.copy()

		while True:
			print('Choose a sort method. Available methods are:\n', methods)
			sort = input()
			if sort in methods:
				break
			print('Wrong method.')

		start = time.time()
		case(sort, temp)

		times['{:.8f}'.format(time.time() - start)] = sort
		methods.remove(sort)

	best = min(list(times.keys()))
	print('Best time shown: {} sec by {} sort'.format(best, times.get(best)))
