import sys
sys.stdin = open("yunji/input.txt", "r")


N = int(sys.stdin.readline())   # 센서의 개수
K = N = int(sys.stdin.readline())   # 집중국의 개수
sensor = list(map(int, sys.stdin.readline().split()))
