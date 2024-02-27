# n
# 한칸 움직일 때 마다 연료 1소모
# 손님을 목적지 까지 대려다 주면 이동시 연로 x2를 충전
# 택시는 최단거리에 있는 손님을 우선으로 픽업
# 각 손님은 목적지가 다름

# 1.장애물을 피하며 손님 별 최단거리를 구함
# 2.최단거리 손님한테 이동
# 3.목적지 최단거리 구하며 남은 연료 계산
# 4.반복

# input: N=map크기, M=손님 수, F= 연료양

import sys

N, M, F = map(int,sys.stdin.readline().split())

map_ = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

start = sys.stdin.readline().split()

son = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
