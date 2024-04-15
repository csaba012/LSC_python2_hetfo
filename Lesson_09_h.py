# + - * /
# % // **
# < > <= >= == != 

print(14)
print(bin(14))

# 1 * 10 + 4 * 1 = 14
# 1 * 2^3 + 1* 2^2 + 1 * 2^1 + 0 * 2^0 = 
# 1 * 8 + 1 * 4 + 1 * 2 + 0 * 1 = 8 + 4 + 2 + 0 = 14

print(bin(6))
# and or xor 
print(bin(14 & 6))
# 1 1 1 0
# 0 1 1 0
# 0 1 1 0
print(bin(14 | 6))
# 1 1 1 0
# 0 1 1 0
# 1 1 1 0
print(bin(14 ^ 6))
# 1 1 1 0
# 0 1 1 0
# 1 0 0 0

if 6 % 2 == 0:
    print("Páros")
else:
    print("Páratlan")

# 1 1 0
# 0 0 1
# 0 0 0

# 1 1 1
# 0 0 1
# 0 0 1
if 6 & 1 == 0:
    print("Páros")
else:
    print("Páratlan")

print(bin(14 << 1))
# 0 1 1 1 0
# 1 1 1 0 0 
print(14 << 1)

print(bin(14 >> 2))
# 1 1 1 0
# 0 0 1 1
print(14 >> 2)

# <<= >>=
n = 14
n <<= 2
print(n)