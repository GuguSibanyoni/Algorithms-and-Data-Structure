'''
given an array = [1, 3, 2, 2] and k = 4
we need to check the sum of which two numbers gives us k
'''

def two_number_sum(array, k):
    for i in range(len(array)-1):
        for j in range(1+i, len(array)):
            if array[i] + array[j] == k:
                print([array[i], array[j]])
    return []

array = [1, 2, 3, 2]
k = 4

two_number_sum(array, k)
