from collections import Counter
def clustering(str1: str, str2: str) -> int:
    SID = 65536
    split_str1 = []
    split_str2 = []
    for i in range(len(str1)-1):
        temp = str1.upper()[i:i+2]
        if temp.isalpha():
            split_str1.append(temp)
    for j in range(len(str2)-1):
        temp = str2.upper()[j:j+2]
        if temp.isalpha():
            split_str2.append(temp)

    if len(split_str1) + len(split_str2) == 0:
        return SID
    else:
        inter = Counter(split_str1) & Counter(split_str2)
        total = (Counter(split_str1) + Counter(split_str2)) - inter
        inter_elem_cnt = len(list(inter.elements()))
        total_elem_cnt = len(list(total.elements()))
        if inter_elem_cnt == 0 and total_elem_cnt == 0:
            return SID
        elif inter_elem_cnt == 0 and total_elem_cnt > 0:
            return 0
        return (inter_elem_cnt/total_elem_cnt*SID)//1