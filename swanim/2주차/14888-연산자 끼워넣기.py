n = int(input())
num_ls = list(map(int, input().split()))
opr_ls = list(map(int, input().split()))
opr_sum = sum(opr_ls)

# 각 연산자 인덱스 저장
ans = []
tmp = []

def back():
    if opr_sum == len(tmp):
        #print(tmp)
        cal(tmp)
        return
    for i in range(len(opr_ls)):
        operand = ''
        if opr_ls[i] != 0:
            if i == 0 : operand = '+'
            elif i == 1: operand = '-'
            elif i == 2: operand= '*'
            else: operand=  '/'
            tmp.append(operand)
            opr_ls[i] -= 1
            back()
            tmp.pop()
            opr_ls[i] += 1

def cal(tmp):
    result = num_ls[0]
    for i in range(1, len(num_ls)):
        opr = tmp[i-1]
        if opr == '+':
            result += num_ls[i]
        elif opr == '-':
            result -= num_ls[i]
        elif opr == '*':
            result *= num_ls[i]
        elif opr == '/':
            result = int(result / num_ls[i])
    ans.append(result)


back()
if len(ans) == 1: 
    print(ans[0])
    print(ans[0])
else:
    print(max(ans))
    print(min(ans))