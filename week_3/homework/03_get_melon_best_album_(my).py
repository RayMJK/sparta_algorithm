genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    classic_count = 0
    pop_count = 0
    classic_index = []
    pop_index = []
    result = []
    for i in range(len(genre_array)):
        if genre_array[i] == "classic":
            classic_count += play_array[i]
            classic_index.append(i)
        elif genre_array[i] == "pop":
            pop_count += play_array[i]
            pop_index.append(i)

    classic_dict = dict()
    for i in classic_index:
        classic_dict[play_array[i]] = i

    pop_dict = dict()
    for i in pop_index:
        pop_dict[play_array[i]] = i
    a = sorted(classic_dict)
    b = sorted(pop_dict)

    classic_first = a.pop()
    classic_second = a.pop()
    pop_first = b.pop()
    pop_second = b.pop()
    if pop_count > classic_count:
        result.append(pop_dict[pop_first])
        result.append(pop_dict[pop_second])
        result.append(classic_dict[classic_first])
        result.append(classic_dict[classic_second])

    else:
        result.append(classic_dict[classic_first])
        result.append(classic_dict[classic_second])
        result.append(pop_dict[pop_first])
        result.append(pop_dict[pop_second])

    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
