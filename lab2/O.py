int1, int2 = input().replace('+', ' ').split()

to_int = { "ZER" : 0, "ONE" : 1 , "TWO" : 2, "THR" : 3, "FOU" : 4, "FIV" : 5, "SIX" : 6, "SEV" : 7, "EIG" : 8, "NIN" : 9}
to_str = {0 : "ZER", 1 : "ONE", 2 : "TWO", 3 : "THR", 4: "FOU", 5 : "FIV", 6 : "SIX", 7 : "SEV", 8 : "EIG", 9 : "NIN"}

def conv_str(s):
    result = 0
    for i in range(0, len(s), 3):
        buff_str = s[i:i+3]
        result = result*10 + to_int[buff_str]
    return result

def conv_int(n):
    s = ""
    while n > 0:
        dig = n % 10
        n //= 10
        s = to_str[dig] + s
    return s

sum = int(conv_str(int1) + conv_str(int2))
print(conv_int(sum))