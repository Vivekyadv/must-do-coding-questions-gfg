# Problem Statement: https://practice.geeksforgeeks.org/problems/nth-natural-number/1

def solve(n):
    result = ''

    while n:
        result += str(n % 9)
        n = n//9

    return int(result[::-1])

print(solve(1509))


def solve(n):
    result = 0
    p = 1

    while n:
        result += p * (n % 9)
        n = n//9
        p = p * 10

    return result

print(solve(1059))