def is_sub(t, s):
    i, j = 0, 0
    while i < len(t) and j < len(s):
        if t[i] == s[j]:
            j += 1
        i += 1
    return j == len(s)


s = "axc"
t = "ahbgdc"
print(is_sub(t, s))

