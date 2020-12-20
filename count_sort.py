from time import time
from random import randrange

def comparison_count_sort(array: list):
	sorted: list = array.copy()
	length: int = len(array)
	count: list = []

	for i in range(0, length):
		count.append(0)

	for i in range(0, length - 1):
		for j in range(i + 1, length):
			if array[i] < array[j]:
				count[j] = count[j] + 1
			else:
				count[i] = count[i] + 1

	for i in range(0, length):
		sorted[count[i]] = array[i]

	return sorted

def distribution_count_sort(l: int, u: int, array: list):
	count: list = []
	length: int = len(array)
	sorted: list = array.copy()

	for i in range(0, u - l + 1):
		count.append(0)

	for i in range(0, length):
		count[array[i] - l] = count[array[i] - l] + 1

	for i in range(1, u - l + 1):
		count[i] = count[i - 1] + count[i]

	for i in range(length - 1, 0 - 1, -1):
		j = array[i] - l
		sorted[count[j] - 1] = array[i]
		count[j] = count[j] - 1
	
	return sorted

def generate_testing_array(l: int, u: int, length: int):
	array: list = []
	for i in range(0, length):
		array.append(randrange(l, u))
	
	return array

l: int = 0
u: int = 10
size: int = 100000
array: list = generate_testing_array(l, u, size)


print("[+] Sorting using comparison count sort...")
comparison_start_time: float = time()
print(comparison_count_sort(array))
comparison_end_time: float = time()
comparison_count_sort_execution_time: float = comparison_end_time - comparison_start_time
print("comparison execution time: ", comparison_count_sort_execution_time)


print("[+] Sorting using distribution count sort...")
distribution_start_time: float = time()
print(distribution_count_sort(l, u, array))
distribution_end_time: float = time()
distribution_count_sort_execution_time: float = distribution_end_time - distribution_start_time

print("comparison execution time: ", comparison_count_sort_execution_time)
print("distribution execution time: ", distribution_count_sort_execution_time)
