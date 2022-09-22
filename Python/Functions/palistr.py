#9.23
def isPaliStr(s):
    return s==s[::-1]

print(isPaliStr('madam'))