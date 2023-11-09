s, p = map(int, input().split())
dna = list(input())
a, c, g, t = map(int, input().split())

answer = 0
dic = {"A": 0, "C": 0, "G": 0, "T": 0}
window = dna[:p]

# 초기 설정
for i in window:
    dic[i] += 1 

if dic["A"] >= a and dic["C"] >= c and dic["G"] >= g and dic["T"] >= t:
    answer += 1

start = 0
end = start + p
for i in range(len(dna)-p):
    dic[dna[start+i]] -= 1
    dic[dna[end+i]] += 1

    if dic["A"] >= a and dic["C"] >= c and dic["G"] >= g and dic["T"] >= t:
        answer += 1

print(answer)