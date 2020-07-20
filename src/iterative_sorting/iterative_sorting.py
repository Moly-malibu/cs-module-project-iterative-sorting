# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i] # TO-DO: swap
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    did_swap = True
    iterations = 0
    while did_swap:
        did_swap = False
        for i in range(len(arr) - iterations - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                did_swap = True
        iterations +=1
    return arr


#Example 2 Rutledge
# def insertion_sort(arr):
#     # loops through the array starting at second element
#     for i in range(1, len(arr)):
#         # capture element to sort
#         cur = arr[i]
#         # capture the index to mutate
#         j = i
#         # comparison loop
#         while j > 0 and arr[j-1] > cur:
#             # moves greater item to right
#             arr[j] = arr[j-1]
#             # decrements comparison loop
#             j -= 1
#             # adds item to sort back into the array
#         arr[j] = cur
#         # return the finished array
#     return arr



'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
#Maximun
def counting_sort(arr, maximum=None):
    i = 0
    j = n - 1
    while(i < j): 
        min = arr[i] 
        min_i = i 
        max = arr[i] 
        max_i = i 
        for T in range(i, j + 1, 1): 
            if (arr[T] > max): 
                max = arr[T] 
                max_i = T 
            elif (arr[T] < min): 
                min = arr[T] 
                min_i = T  
        time = arr[i] 
        arr[i] = arr[min_i] 
        arr[min_i] = time 
        if (arr[min_i] == max): 
            time = arr[j] 
            arr[j] = arr[min_i] 
            arr[min_i] = time 
        else: 
            time = arr[j] 
            arr[j] = arr[max_i] 
            arr[max_i] = time 
  
        i += 1
        j -= 1
  
    print("Sorted array:", end = " ") 
    for i in range(n): 
        print(arr[i], end = " ")  

if __name__== '__main__': 
    arr = [53, 76, 41, 7, 33, 86, 1] 
    n = len(arr) 
    counting_sort(arr, n) 


