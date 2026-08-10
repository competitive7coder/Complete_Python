def isPalindrome(s: str) -> bool:
    s = s.lower()
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1
    return True

s = input("Enter a string: ")
result = isPalindrome(s)
if result:
    print("Palindrome ")
else:
    print("Palindrome not")


# Pehle isalnum() samjho
# s[i].isalnum()
# pointer pe special character mila
# Usko ignore karo
# Pointer aage badhao
# s[i].isalnum()
#  True → letter ya digit
#  False → space, comma, colon, symbol
# Examples:
# 'a'.isalnum()  → True
# '7'.isalnum()  → True
# ' '.isalnum()  → False
# ','.isalnum()  → False