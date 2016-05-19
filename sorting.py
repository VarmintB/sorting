import time

def bubble(list):
	for i in reversed(range(len(list))):
		for j in range(i):
			if list[j] >= list[j + 1]:
				list[j], list[j + 1] = list[j + 1], list[j]
				
def selection(list):
	for i in range(len(list)):
		list[list.index(min(list[i:]))], list[i] = list[i], list[list.index(min(list[i:]))]

def insertion(list):
	for i in range(1, len(list)):

		temp = list[i]
		index = i - 1

		while i >= 0 and temp < list[index]:
			if temp < list[index]:
				list[index + 1] = list[index]
				list[index] = temp

if __name__ == '__main__':

	methods = ['bubble', 'selection', 'insertion']
	times = dict()

	while True:

		print("Input a list. Leave input empty when you are done.")
		numbers = list()

		while True:
			elem = input()
			if elem is '':
				break
			numbers.append(int(elem))

		print('Choose a sort method. Available methods are:\n', methods)
		sort = input()

		methods.remove(sort)

		if sort == 'bubble':
			start = time.time()
			bubble(numbers)

		elif sort == 'selection':
			start = time.time()
			selection(numbers)

		elif sort == 'insertion':
			start = time.time()
			insertion(numbers)

		print(numbers)
		times[sort] = '{:.15f}'.format(time.time() - start)
		print(times)
