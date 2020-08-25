def arrange(arr):
    n = len(arr)
    # count number of positives and negatives
    pos = 0
    for i in arr:
        if i > 0:
            pos += 1
    neg = n - pos

    # initialize indices
    p_idx = n_idx = 0
    if pos > neg:
        n_idx = 1
    else:
        p_idx = 1

    # this will not keep the original order
#    while p_idx < n and n_idx < n:
#        while p_idx < n and arr[p_idx] > 0:
#            p_idx += 2
#        while n_idx < n and arr[n_idx] < 0:
#            n_idx += 2
#        if p_idx < n and n_idx < n:
#            arr[p_idx], arr[n_idx] = arr[n_idx], arr[p_idx]
#    return arr

    while p_idx < n and n_idx < n:
        if arr[p_idx] > 0 and arr[n_idx] < 0:
            p_idx += 2
            n_idx += 2
        elif arr[p_idx] > 0 and arr[n_idx] > 0:

    

arr = [1, 2, -1, -2, -3]
print(arrange(arr))



arr = [1, 2, -1, -2, -3, 3, 4]
print(arrange(arr))

arr = [1, 2, -1, -2, -3, 4]
print(arrange(arr))
