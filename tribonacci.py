def tribonacci(signature, n):
    a = signature[0]
    b = signature[1]
    c = signature[2]
    next = 0
    result = [a, b, c]
    if n < 0:
        return []
    if n < len(result):
        return result[:n]

    n = n - len(result)
    for i in range(1, n+1):
        next = a + b + c
        a = b
        b = c
        c = next
        result.append(c)
    return result




print(tribonacci([1, 1, 1], 10))
print(tribonacci([1, 1, 1], 1))
