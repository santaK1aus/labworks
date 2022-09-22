#9.22
def revstr(s):
    if s=='':
        return ''
    return s[len(s)-1]+revstr(s[:len(s)-1])

def revstrn(s):
    return s[::-1]

print(revstrn('Hello there'))