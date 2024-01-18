def most_played_song(genres: list[str], plays: list[int]) -> list[int]:
    """_summary_
    노래 선택 우선순위:
    1. 속한 노래가 많이 재생된 장르
    2. 장르내에서 많이 재생된 노래
    3. 장르 내에서 재생횟수가 같으면 고유번호가 낮은 노래

    Args:
        genres (list[str]): 노래의 장르 목록
        plays (list[int]): 노래 재생횟수 목록

    Returns:
        list[int]: 우선 순위 기준으로 정렬된 노래의 고유번호 목록

    old code:
        answer = []
        genres_idx = dict()
        for i, each in enumerate(genres):
            if each not in genres_idx:
                genres_idx[each] = [i]
            else:
                genres_idx[each].append(i)
        total_plays = dict.fromkeys(genres_idx.keys())
        sum_plays = []
        for k, v in genres_idx.items():
            plays_by_gen = dict(zip(v, [plays[x] for x in v] ))
            total_plays[k] = dict(sorted(plays_by_gen.items(), key=lambda item: item[1], reverse = True))
        total_plays = dict(sorted(total_plays.items(), key= lambda item: sum(item[1].values()), reverse = True))
        [answer.extend(list(x.keys())[:2]) for x in total_plays.values()]    
        return answer
    """
    result = []
    plays_per_gen = dict()
    for i, (genre, play) in enumerate(zip(genres, plays)):
        idx_init = plays_per_gen.get(genre, dict())
        idx_init[i] = play
        plays_per_gen[genre] = idx_init
    most_plays_gen = sorted(list(plays_per_gen.items()), key=lambda x: sum(x[1].values()))
    while most_plays_gen:
        _, song_plays = most_plays_gen.pop()
        song_most_plays = sorted(song_plays.items(), key= lambda x: (-x[1], x[0]))
        song_idx = list(map(lambda x: x[0], song_most_plays))
        result = result + song_idx[:2]

    return result