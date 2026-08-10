'''
1. Arithmetic Operators
| Operator | Meaning             | Example   | Result     |
| -------- | ------------------- | --------- | ---------- |
| `+`      | Addition            | 10 + 3  | 13       |
| `-`      | Subtraction         | 10 - 3  | 7        |
| `*`      | Multiplication      | 10 * 3  | 30       |
| `/`      | Division            | 10 / 3  | 3.333... |
| `//`     | Floor division      | 10 // 3 | 3        |
| `%`      | Modulus (remainder) | 10 % 3  | 1        |
| `**`     | Power               | 2 ** 3  | 8        |

'''

a = 10
b = 3
#print(a + b)
#print(a ** b)


'''
2. Assignment Operators
| Operator | Example  | Same as     |
| -------- | -------- | ----------- |
| `=`      | `a = 5`  | assign      |
| `+=`     | `a += 2` | `a = a + 2` |
| `-=`     | `a -= 2` | `a = a - 2` |
| `*=`     | `a *= 2` | `a = a * 2` |
| `/=`     | `a /= 2` | `a = a / 2` |
'''



'''
3. Comparison (Relational) Operators
| Operator | Meaning          | Example  |
| -------- | ---------------- | -------- |
| `==`     | Equal to         | `5 == 5` |
| `!=`     | Not equal        | `5 != 3` |
| `>`      | Greater than     | `5 > 3`  |
| `<`      | Less than        | `5 < 3`  |
| `>=`     | Greater or equal | `5 >= 5` |
| `<=`     | Less or equal    | `5 <= 5` |
'''
print(5 == 5)   # True


'''
4. Logical Operators
| Operator | Meaning           | Example            |
| -------- | ----------------- | ------------------ |
| `and`    | Both true         | `a > 5 and b < 10` |
| `or`     | At least one true | `a > 5 or b > 10`  |
| `not`    | Reverse result    | `not(a > 5)`       |

'''
#print(not True)    # False
#print(not False)   # True
a = 10
b = 5

print(a > b)        # True
print(not (a > b))  # False (not reverses it → False)
#is_logged_in = False
#print(not is_logged_in)  # True



'''
5. Bitwise Operators
| Operator | Meaning     |    |
| -------- | ----------- | -- |
| `&`      | AND         |    |
| `        | `           | OR |
| `^`      | XOR         |    |
| `~`      | NOT         |    |
| `<<`     | Left shift  |    |
| `>>`     | Right shift |    |

'''
'''
1. Left Shift (<<)
Moves bits to the left and adds zeros on the right.
Syntax
number << positions
Example
5 << 1
Step-by-step
5 in binary → 00000101
Shift left by 1 → 00001010
Result → 10
print(5 << 1)  # 10
Rule
Each left shift by 1 multiplies the number by 2:
5 << 2  # 5 × 2² = 20

2. Right Shift (>>)
Moves bits to the right and removes bits on the right.
Syntax
number >> positions
Example
5 >> 1
Step-by-step
5 in binary → 00000101
Shift right by 1 → 00000010
Result → 2
print(5 >> 1)  # 2
Rule
Each right shift by 1 divides the number by 2 (integer division):
20 >> 2  # 20 ÷ 2² = 5
'''




'''
6. Membership Operators
| Operator | Example            |
| -------- | ------------------ |
| `in`     | `'a' in "apple"`   |
| `not in` | `3 not in [1,2,4]` |

'''
print(f"Example of Membership Operators: {'a' in 'apple'}")
print(f"Another Example is 5 in [1, 3, 5, 7]:  {5 in [1, 3, 5, 7]}")      # True
print(f"Another 'py' in 'python': {'py' in 'python'}")



'''
7. Identity Operators
| Operator | Example      |
| -------- | ------------ |
| `is`     | `a is b`     |
| `is not` | `a is not b` |

'''
a = [1,2]
b = [1,2]
print(a is b)   # False
print(a == b)   # True



'''
Operator Precedence (High → Low)
**
*, /, //, %
+, -
Comparison
not
and
or 

'''