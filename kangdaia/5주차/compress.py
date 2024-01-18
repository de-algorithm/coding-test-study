def lzw_zip(msg: str) -> list[int]:
    file = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    search = [0]
    curr = ""
    for i in range(len(msg)):
        curr += msg[i]
        if curr not in file:
            file.append(curr)
            curr = msg[i]
            search.append(file.index(curr)+1)
        else:
            search[-1] = file.index(curr)+1
    return search
