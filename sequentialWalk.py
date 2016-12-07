digits = 'LDUR'

def nthWalk(n):
    result = []
    while n:
        n, rem = divmod(n-1, len(digits))
        result.append(digits[rem])
    return ''.join(reversed(result))
