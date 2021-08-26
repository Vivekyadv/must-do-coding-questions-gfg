# Problem Statement: https://www.geeksforgeeks.org/find-smallest-value-represented-sum-subset-given-array/


def solve(arr, n):
    res = 1
    for i in range(n):
        if arr[i] <= res:
            res += arr[i]
        else:
            break
    return res

arr = [1, 2, 3, 4, 6, 8]
print(solve(arr, len(arr)))
