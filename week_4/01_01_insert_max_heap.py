class MaxHeap:
    def __init__(self):
        self.items = [None]
    # 1. 새 노드를 맨 끝에 추가한다
    # 2. 지금 넣은 새 노드를 부모와 비교한다. 만약 부모보다 크다면 교체한다.
    # 3. 이 과정을 꼭대기 까지 반복한다.

    def insert(self, value):
        # 구현해보세요!
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:
            parent_index = cur_index // 2
            if self.items[cur_index] > self.items[parent_index] :
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index

            else :
                break


        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
max_heap.insert(5)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!