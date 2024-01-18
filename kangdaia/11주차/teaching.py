def antarctica(n: int, k: int, words: list[str]) -> int:
    learning = set("antic")
    if k < len(learning):
        return 0
    elif k == 26:
        return n
    
    left_k = k - len(learning)
    result = 0
    new_word_set = []

    for word in words:
        word_set = set(word) - learning
        if not word_set:
            result += 1
        else:
            new_word_set.append(word_set)



if __name__ == "__main__":
    result = antarctica(3, 6, ["antarctica", "antahellotica", "antacartica"])
    print(result, result == 2)