def bubble(list):
	for i in reserved(range(len(list))):
		for j in range(1, i + 1):
			if list[j-i] > list[j]:
				list[j], list[j-1] = list[j-1], list[j]
				
def selection(list):
	for i in range(len(list)):
		list[list.index(min(list[i:]))], list[i] = list[i], list[list.index(min(list[i:]))]

def insertion(list):
	for i in range(1, len(list)):
		temp = list[i]
		index = i - 1
		while i >= 0 and temp < list[index]:
			if temp < list[index]:
				list[index+1] = list[index]
				list[index] = temp
		