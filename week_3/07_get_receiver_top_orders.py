top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):  # ==> O(N^2)
    answer = [0] * len(heights)
    while heights:      # O(N)
        height = heights.pop()
        for idx in range(len(heights)-1, -1, -1):        # O(N)
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!