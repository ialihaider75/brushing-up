'''
 - Here we are using deque module to use a build-in queue data struture
 - We are using a queue as our window of size k.
'''
from collections import deque
def print_sub_array(arr,n,k):
    maxs_arr = list()
    sliding_window = deque(list())
    for i in range(0,k):
        sliding_window.append(arr[i])
    j = 0
    maximum = 0
    while (j + k) <= n - 1 :
        maximum = max(sliding_window)
        sliding_window.popleft()
        sliding_window.append(arr[j+k])
        maxs_arr.append(maximum)
        j += 1
    maxs_arr.append(max(sliding_window))
    return maxs_arr
    
arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
x = print_sub_array(arr,10,4)
print(x)