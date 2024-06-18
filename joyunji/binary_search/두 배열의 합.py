# 윤지 
# 메모리 초과 해결 
import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
A_len = int(input())
A = list(map(int, input().split()))
B_len = int(input())
B = list(map(int, input().split()))

# 누적합 배열 생성
def prefix_sums(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]
    return prefix

# 부분합 빈도수 계산
def subarray_sums(prefix, length):
    sub_sum = defaultdict(int)
    for i in range(length):
        for j in range(i + 1, length + 1):
            sub_sum[prefix[j] - prefix[i]] += 1
    return sub_sum

# A와 B의 누적합 배열
A_prefix = prefix_sums(A)
B_prefix = prefix_sums(B)

# A와 B의 부분합 빈도수 계산
A_sub_sum = subarray_sums(A_prefix, A_len)
B_sub_sum = subarray_sums(B_prefix, B_len)

# 정답 계산
answer = 0
for sum_v, count in A_sub_sum.items():
    if T - sum_v in B_sub_sum:
        answer += count * B_sub_sum[T - sum_v]

print(answer)