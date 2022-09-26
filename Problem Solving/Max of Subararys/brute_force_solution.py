def print_sub_array(arr,n,k):
    maxs_arr = list()
    max = 0
    i = 0
    while (i + k) <= n:
        max = arr[i]
        for j in range(i+1,k+i):
            if arr[j] > max:
                max = arr[j]
        maxs_arr.append(max)
        i += 1
    return maxs_arr
    
arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
x = print_sub_array(arr,10,3)
print(x)