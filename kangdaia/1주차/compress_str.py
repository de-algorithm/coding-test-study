def compress_str_solution(s):
    N = len(s)  # 문자열의 길이
    candidate = []
    unit = 1
    while unit < N // 2 + 1:
        visited = ["" for _ in range(N)]
        curr = 0
        # 유닛 단위 만큼 문자열 잘라서 리스트
        split_s = [s[x:x+unit] for x in range(0, N, unit)]
        for i, each in enumerate(split_s):
            if len(visited[curr]) == 0 or split_s[curr] != split_s[i]:
                curr = i
                visited[curr] = (1, split_s[curr])
            else:
                visited[curr] = (visited[curr][0] + 1, visited[curr][1])
        for j in range(N):
            if visited[j] != "":
                visited[j] = str(visited[j][0])+visited[j][1] if visited[j][0] > 1 else visited[j][1]
        candidate.append(len("".join(visited)))
        unit += 1
    return min(candidate) if candidate else 1
