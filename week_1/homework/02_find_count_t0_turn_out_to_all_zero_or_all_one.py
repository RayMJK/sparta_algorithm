input = "000010"

counter = 0
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    counter = 0
    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            counter += 1
    if counter % 2 == 0 :

        return (counter//2)

    elif counter % 2 == 1 :
        return (counter//2)+1


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)