# Silver 2

# 25 min
# 메모리 : 44980KB
# 시간 : 284ms


# start 와 end를 지정하고 +=1 하면서 비교하기 


def solution():

    s, p  = map(int, input().split())
    dna = list(str(input()))
    cnt_a, cnt_c, cnt_g, cnt_t = map(int, input().split())

    check_dict = {'A' :0, 'C' : 0, 'G' : 0, 'T' : 0}

    start, end = 0, p-1
    check_arr = dna[start : end]
    for word in check_arr :
        check_dict[word] += 1

    cnt = 0


    while end  < s:
        check_dict[dna[end]] += 1
        
        if check_dict['A'] >= cnt_a and check_dict['C'] >= cnt_c and check_dict['T'] >= cnt_t and check_dict['G'] >= cnt_g :
            cnt += 1
        
        check_dict[dna[start]] -= 1
        start += 1
        end += 1


    print(cnt)
        
        



if __name__ == '__main__':
    solution()
    