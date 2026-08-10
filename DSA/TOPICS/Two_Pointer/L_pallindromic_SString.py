def LPS(s):
    if not s:
        return ""

    res = s[0]

    for i in range(len(s)):
        # odd-length palindromes
        l = r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(res):
                res = s[l:r + 1]
            l -= 1
            r += 1

        # even-length palindromes
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(res):
                res = s[l:r + 1]
            l -= 1
            r += 1

    return res

s = "babad"
ans = LPS(s)
print(ans)

# def LPS(s):
#     n = len(s)
#     if n == 0:
#         return ""
# 
#     longest = s[0]
#
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             substr = s[i:j]
#
#             if substr == substr[::-1]:
#                 if len(substr) > len(longest):
#                     longest = substr
#
#     return longest
