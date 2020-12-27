top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    n = len(heights)
    result =[0 for i in range(5)]
    a=-1
    for i in range(n-1, 0, -1):
        a += 1
        for j in range(n-2-a, -1, -1):
            print(i)
            print(j)
            print()
            if heights[j] > heights[i]:
                result[i] = j+1
                print(result)

                break



    return result


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!