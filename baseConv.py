def convert(base1, base2, num, data1 = -1, data2 = -1):
    import math
    # Data cleanup and error code returns
    base10sym = "0123456789"
    if data1 == -1:
        if base1 <= 10:
            data1 = base10sym[:base1]
        else:
            return(-1)
    if data2 == -1:
        if base2 <= 10:
            data2 = base10sym[:base2]
        else:
            return(-2)
    
    if -1 in map(lambda x: data1.find(x), list(num)):
        return(-3)

    if len(data1) < base1:
        return(-4)
    if len(data2) < base2:
        return(-5)

    for i in range(len(data1)):
        if data1[i] in data1[:i]:
            return(-6)
    
    for i in range(len(data2)):
        if data2[i] in data2[:i]:
            return(-7)

    # Convert number to base 10 integer
    num10 = 0

    for i in range(-1,-len(num)-1,-1):
        val = data1.find(num[i])
        num10 += val * (base1 ** (-i-1))
    
    # Convert base 10 to desired base
    result = ""
    for pv in range(math.floor(math.log(num10, base2)) + 3):
        result = str(data2[num10 // (base2**(pv)) % base2]) + result

    # Strip leading zeroes
    for dig in range(len(result)):
        if result[dig] != data2[0]:
            return(result[dig:])

    # Return zero if number is only zeroes
    return data2[0]

print(convert(10,10,"bdfceg", data1 = "abcdefghij", data2 = "0123456789"))