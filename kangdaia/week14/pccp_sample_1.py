# 붕대감기

def solution(bandage: list[int], health: int, attacks: list[list[int]]) -> int:
    """
    붕대감기
    조건:
    - t초동안 붕대를 감음 - 1초마다 x 만큼의 체력을 회복함.
    - t초 연속으로 붕대를 감는데 성공 - y 만큼의 체력 추가 회복
    - 최대 체력 존재 - 일정 값 이상 증가 불가
    - 감는 도중 몬스터 공격 - 기술 취소 - 공격 중 회복 불가
        - 이후 즉시 붕대 감기 다시 사용 - 연속 성공시간 0으로 초기화
    - 몬스터의 공격으로 체력이 0이 되면 체력 회복 불가 - 사망


    Args:
        bandage (list[int]): [시전시간, 초당 회복량, 추가 회복량]
        health (int): 최대 체력
        attacks (list[list[int]]): [[몬스터의 공격시간, 피해량]] 리스트

    Returns:
        int: 공격이 모두 끝난 직후 남은 체력, 사망시 -1
    """
    bandage_time, recover_per_sec, extra_recover = bandage
    curr_health = health
    last_attack = 0 # 마지막으로 연속 취소된 시간
    for attack_time, health_lost in attacks:
        # 공격 받기 전 회복
        prev_success_time = attack_time - last_attack - 1
        if prev_success_time > 0:
            total_extra_health = prev_success_time // bandage_time * extra_recover
            curr_health = min(health, curr_health+total_extra_health+recover_per_sec*prev_success_time)
        # 공격 후
        last_attack = attack_time
        curr_health -= health_lost

        if curr_health <= 0:
            return -1

    return curr_health