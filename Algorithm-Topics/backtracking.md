# 백트래킹이란

## DFS에서 가지치기가 추가된 알고리즘

# 개요

- DFS를 하는데, 노드에 깊이 들어가기 전 조건을 통해 해가 유망한지 아닌지 ( Promising )를 판단하여 유망하지 않는 노드에는 진행하지 않고 ( Pruning ) 되돌아가는것
    
    **⇒ DFS를 하는데 조건문을 추가해서 조건문에 부합하는 것만 진행하는 알고리즘이라고 판단**
    

![Alt text](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRAV0kcolRTgsqjMKtmOXzWcFIQjIVOlLsyPGP1BxTf2VqHDH7x)

## 중요개념

### 1. 가지치기 ( Prunning )

- 조건문을 통해 유망하지 않은 경로를 따라가지 않게하여 시도 횟수를 줄인다

## 예제

[N - Queen](https://thd0011.tistory.com/19) 

N-Queen 문제는, 크기가 N*N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제.

![Alt text](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99B8D13F5A927B1132)
![Alt text](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99B834345A927C0818)
<aside>

1. (1, 1) 에서 시작하여 DFS 수행을 통해 가장 첫번째 노드인 (2, 1) 지점으로 간다.

2. (2, 1) 노드를 검사해보니 첫번째 퀸의 이동반경에 포함되기 때문에 유망한 노드가 아니어서 백트래킹을 수행하여 상위 노드인 (1, 1) 지점으로 이동한다.

3. 다시 DFS 를 수행하여 다음 노드인 (2, 2) 로 이동한다.

4. (2, 2) 노드를 검사해보니 첫번째 퀸의 이동반경에 포함되기 때문에 유망한 노드가 아니어서 백트래킹을 수행하여 상위 노드인 (1, 1) 지점으로 이동한다.

5. 다시 DFS 를 수행하여 다음 노드인 (2, 3) 로 이동한다.

6. (2, 3) 노드를 검사해보니 첫번째 퀸의 이동반경에 포함되지 않아서 유망한 노드가 되었다. 이제 (2, 3) 을 기준으로 DFS 를 수행하여 3번째 퀸의 위치를 찾는다.
</aside>

```python
# 상하좌우 대각선 체크 함수
def check(n):
  for i in range(n):
    if (board[n] == board[i]) or (n-i == abs(board[n] - board[i])):    # 좌우에 있거나, 대각선에 있다면 
      return False 

  return True
```

### [보글게임](https://cinux.tistory.com/14)

![Alt text](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F2653F54457BD83AF22)

<aside>

1. 찾는 단어가 "PRETTY" 이면  Word문자열의 첫 글자는 1행 4열의 "P"가 될 것이다. 

2. 그림에서는 2행 2열의 "P"가 빨간색으로 돼있지만 이 코드에서는 팔방재귀 즉, 대각선도 검사하므로 1행 4열의 "P"가 선택이 될 것이고 

3. 다음 2행 3열의 R ... 2행 4열의 E..이런식으로 재귀호출시 전달인자로 Word배열 + 1 을 주어서 단어의길이가 1이 될때 종료를 시킨다.

</aside>

참고

[Youtube - 코딩테스트 알고리즘 3.백트래킹](https://www.youtube.com/watch?v=atTzqxbt4DM) 

[Tistory - **[알고리즘] 백트래킹 (Backtracking) 알고리즘**](https://thd0011.tistory.com/19)

[Tistory - **[알고리즘] 백트래킹**](https://rlakuku-program.tistory.com/34)

[백 트래킹 ( Backtracking )](https://cinux.tistory.com/14)

[Tistory - **[백준] N-Queens 문제(Python) - 백트래킹**](https://daeun-computer-uneasy.tistory.com/80)