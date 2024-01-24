import sys
sys.stdin = open('yunji/input.txt', 'r')


N, C = map(int, sys.stdin.readline().split())
weights = list(map(int, sys.stdin.readline().split()))

weights1 = weights[:N/2]
weights2 = weights[N/2:]

sum1, sum2 = [], [ ]