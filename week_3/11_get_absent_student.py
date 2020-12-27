all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    # 구현해보세요!
    student_dict = {}
    for key in all_array:   # O(N)
        student_dict[key] = True # 아무값이나 value로,   # 공간복잡도도 O(N)

    for key in present_array:       # O(N)
        del student_dict[key]

    for key in student_dict.keys():
        return key

print(get_absent_student(all_students, present_students))