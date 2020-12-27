numbers = [1, 1, 1, 1, 1]
target_number = 3
result_count = 0

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):

    if current_index == len(numbers):
        global result_count
        if current_sum == target:
            result_count += 1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index+1, current_sum + numbers[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index+1, current_sum - numbers[current_index])



get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
print(result_count)