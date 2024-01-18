def finish_work(n: int, works: list[str]) -> int:
    """ 퇴사2
    1. 각 날짜에 맞춰서 dictionary로 자료구조 변경
        - 각 날의 작업 소요 일 수에 맞춰 일하는 날 목록을 만들어 추가.
        ex) 0일, 3일소요 -> 0: [0, 1, 2]
        - 각 날의 작업에 해당하는 수당은 따로 list 구성
    2. find_max_profit function으로 재귀 호출
    3. 함수를 돌리며 추가된 수당 목록 - 각 작업 스케쥴 경우에 따른 수당들을 담음.
    -> 목록의 최대값 반환

    Args:
        n (int): 일을 해결할 최대 기간
        works (list[str]): 각 인덱스가 i+1 날일 때, 소요 일수와 일의 수당을 string으로 담은 목록

    Returns:
        int: 최대로 얻을 수 있는 수당(이득)
    """
    schedule = dict()
    candidate = []
    earns = [0 for _ in range(n)]
    for day in range(n):
        work = works[day].split()
        period, earn = int(work[0]), int(work[1])
        if day + period <= n:
            schedule[day] = list(range(day, day+period))
            earns[day] = earn
    
    def find_max_profit(start: int, prev: list[int], curr_earn: int) -> None:
        """
        각 날마다 할 수 있는 선택:
        - 만약 오늘 일 소요기간이 하루 이상이면,
            - 오늘 일할 것 - 수당 얻음 -> 소요기간의 마지막날 +1로 넘어감
            - 오늘 일하지 않을 것 - 다음날로 넘어감
        - 소요기간이 하루면 오늘 일할 것 - 수당 얻음 -> 다음날로 넘어감
        - 마지막날까지 dict에 있는 날을 모두 방문했으면 얻은 수당을 목록에 추가
        Args:
            start (int): 작업 시작 날
            prev (list[int]): 현재까지 작업한 날 목록
            curr_earn (int): 현재까지 얻은 수당
        """
        if start not in schedule:
            candidate.append(curr_earn)
            return
        complete = schedule[start]
        if len(complete) > 1:
            # 소요 기간이 하루 이상 걸릴 경우 오늘을 넘기고 내일 스케쥴을 진행하는 경우
            find_max_profit(start+1, prev, curr_earn)
        # 오늘 스케쥴을 진행하는 경우
        find_max_profit(complete[-1]+1, prev+complete, curr_earn+earns[start])
    find_max_profit(0, [], 0)
    # print(schedule, earns, candidate)
    return max(candidate)


if __name__ == "__main__":
    input = ["7", "3 10", "5 20", "1 10", "1 20", "2 15", "4 40", "2 200"]
    answer = finish_work(int(input[0]), input[1:])
    print(answer, answer == 45)

    input = ["10", "1 1", "1 2", "1 3", "1 4", "1 5", "1 6", "1 7", "1 8", "1 9", "1 10"]
    answer = finish_work(int(input[0]), input[1:])
    print(answer, answer == 55)

    input = ["10", "5 10", "5 9", "5 8", "5 7", "5 6", "5 10", "5 9", "5 8", "5 7", "5 6"]
    answer = finish_work(int(input[0]), input[1:])
    print(answer, answer == 20)

    input = ["10", "5 50", "4 40", "3 30", "2 20", "1 10", "1 10", "2 20", "3 30", "4 40", "5 50"]
    answer = finish_work(int(input[0]), input[1:])
    print(answer, answer == 90)
