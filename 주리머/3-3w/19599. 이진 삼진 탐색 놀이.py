'''
백준 19599. 이진 삼진 탐색 놀이
https://www.acmicpc.net/problem/19599
'''
def binary_search(A, value, left, right, count):
    mid = (left + right) // 2
    if (A[mid] == value):
        return count
    elif (value < A[mid]):
        return binary_search(A, value, left, mid - 1, count+1)
    else:
        return binary_search(A, value, mid + 1, right, count+1)

def ternary_search(A, value, left, right, count):
    left_third = left + ((right - left) // 3)
    right_third = right - ((right - left) // 3)
    # print(f'찾는 값: value: {value}, left: %s right: %s, left_third: %s, right_third: %s' % (left, right, left_third, right_third))
    if (A[left_third] == value):
        return count
    elif (A[right_third] == value):
        return count + 1
    elif (value < A[left_third]):
        return ternary_search(A, value, left, left_third - 1, count+2)
    elif (value < A[right_third]):
        return ternary_search(A, value, left_third + 1, right_third - 1, count+2)
    else:
        return ternary_search(A, value, right_third + 1, right, count+2)
n = int(input())
arr = [i for i in range(1, n+1)]
bArr = [binary_search(arr, a, 0, len(arr)-1, 0) for a in arr]
tArr = [ternary_search(arr, a, 0, len(arr)-1, 0) for a in arr]

print(sum([1 for i in range(n) if bArr[i] < tArr[i]]))
print(sum([1 for i in range(n) if bArr[i] == tArr[i]]))
print(sum([1 for i in range(n) if bArr[i] > tArr[i]]))
