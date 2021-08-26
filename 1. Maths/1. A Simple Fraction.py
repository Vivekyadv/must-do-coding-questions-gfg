# Problem Statement: https://practice.geeksforgeeks.org/problems/a-simple-fraction0921/1


def solve(p, q):
    if q == 0:
        return 'ZeroDivisionError'

    result = '-' if p//q < 0 else ''
    p, q = abs(p), abs(q)
    result += str(p//q)

    rem = (p % q) * 10
    if rem == 0:
        return result
    
    result += '.'
    store = {}
    while rem != 0:
        if rem in store:
            indx = store[rem]
            result = result[:indx] + '(' + result[indx:] + ')'
            return result
        
        store[rem] = len(result)
        result += str(rem//q)
        rem = (rem % q) * 10

    return result

print(solve(10, 7))

