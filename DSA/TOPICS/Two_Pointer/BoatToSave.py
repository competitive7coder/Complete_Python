def bts(arr, limit):
    l, r = 0, len(arr)-1
    arr.sort()
    boat = 0
    while l <= r:
        if arr[l]+arr[r] <= limit:
            boat+= 1
            l, r = l+1, r-1
        # elif arr[l] < arr[r]:
        #     boat += 1
        #     l+= 1
        else:
            # print(arr[r])
            boat += 1
            r-= 1
    return boat


arr = [3,5,3,4]
limit = 5
ans = bts(arr, limit)
print(ans)