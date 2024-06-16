'''
a+b+c=d

정렬된 집합에서 가장 뒤에 있는 숫자를 d로 정함
- 뒤에서부터 앞으로 오면서 c를 정함
- a+b = d-c를 구함 
- 
'''

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()
arr2 = []
for i in range(n):
    for j in range(i, n):
        arr2.append(arr[j] + arr[i])

arr2.sort()
result = 0
for i in range(n):
    for j in range(i, n):
        a = arr[j] - arr[i]    
        start = 0
        end = len(arr2) - 1
        
        while start <= end:
            mid = (start + end) // 2
            b = arr2[mid]
            if a > b:
                start = mid + 1
            elif a < b:
                end = mid - 1
            else:
                result = max(result, arr[j])
                break

print(result)