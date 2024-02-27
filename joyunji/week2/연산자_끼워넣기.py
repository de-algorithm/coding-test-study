'''
Date        : 2024.01.29
Problem     : https://www.acmicpc.net/problem/14888
Tag         : backtracking
'''

max_value = -1e9
min_value = 1e9

def dfs(depth,total, A, N, plus, minus, multiply, divide):
    global min_value, max_value
    
    # 수열의 마지막 숫자까지 연산을 하였을 때
    if depth == N:
        min_value = min(total, min_value)
        max_value = max(total, max_value)
        return
    
    if plus:
        dfs(depth+1, total + A[depth], A, N, plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total - A[depth], A, N, plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total * A[depth], A, N, plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total / A[depth]), A, N, plus, minus, multiply, divide-1)
        
def solution(A, op_list):
    """

    Args:
        A (list): 1 ≤ Ai ≤ 100를 만족하는 수열이다. 
        op_list (list): 차례대로 덧셈의 개수, 뺄셈의 개수, 곱셈의 개수, 나눗셈의 개수이다. 

    Returns:
        list: [최댓값, 최솟값] 형태로 반환  
    """
    N = len(A)  # 수의 개수 
    total = A[0]
    dfs(1, total, A, N, op_list[0], op_list[1], op_list[2], op_list[3])
    
    return [max_value, min_value]

