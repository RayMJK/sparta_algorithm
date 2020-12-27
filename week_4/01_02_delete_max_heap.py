class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    # 1. 루트 노드를 맨 마지막 노드 (맨 아래 레벨의 맨 오른쪽 노드)와 교환한다 = self.items[마지막 원소] = self.items[-1]
    # 2. 루트 노드를 배열에서 제거한뒤, 저장해둔다.
    # 3. 현재 꼭대기에 올라간 (원래 마지막) 노드를 자식 노드들과 비교하면서 내려보낸다. 이때, 더 큰 자식노드와 교환하면서 내려가야한다.
    # 4. 이 과정을 자식들 보다 내가 더 클때 혹은 바닥에 다다랐을때 까
    def delete(self):
        # 구현해보세요!
        # 1
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        # [None, 4, 7, 6, 2, 5, 8]
        prev_max = self.items.pop()
        # [None, 4, 7, 6, 2, 5]
        cur_index = 1
        while cur_index <= len(self.items) - 1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index

            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            if max_index == cur_index:
                break
            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index
        return prev_max  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]
