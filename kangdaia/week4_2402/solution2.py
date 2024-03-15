def solution(n: int, s: int, eats: list[int]) -> int:
    """
    조건: 여러 사람이 동시에 소보루를 집는다면 번호가 작은 사람이 먼저 잡음
    매초마다, 각 사람의 먹는 속도가 시간의 배수인지 확인 (먹음)
    - 해당될 경우, 남은 소보루 개수 - 1, 마지막 사람 업데이트
        - 남은 소보루 개수가 0이면 반복 멈춤
    - time + 1
    Args:
        n (int): 영선이가 사온 튀김 소보루 개수
        s (int): 남아 있던 튀김 소보루 개수
        eats (list[int]): m명의 소보루를 먹는 속도

    Returns:
        int: 마지막으로 소보루를 집어 든 사람의 번호
    """
    time = 0
    eated = n-s
    while eated > 0:
        for i in range(len(eats)):
            if time%eats[i] == 0:
                eated -= 1
                num = i
                if eated == 0:
                    break
        time += 1
    return num+1

n, s = list(map(int,input().split()))
m = int(input())
m_lst = []
for i in range(m):
    m_lst.append(int(input()))