def canPlace(stalls, cows, dist):
    count_cows = 1
    last_cow = stalls[0]
    for i in range(len(stalls)):
        if stalls[i] - last_cow >= dist:
            count_cows += 1
            last_cow = stalls[i]
            if count_cows == cows:
                return True
    return False



def aggressiveCows(stalls, cows):
    stalls.sort()
    start = 1
    end = (max(stalls) - min(stalls)) # (max - min) stalls[-1] - stalls[0]
    ans = -1
    while start <= end:
        mid = start + (end - start) // 2
        if canPlace(stalls, cows, mid):
            ans = mid
            start = mid + 1 # we move right cause q asked for largest(min) distance
        else:
            end = mid - 1
    return ans

stalls = [6,1,2,4,3]
cows = 2

print(aggressiveCows(stalls, cows))