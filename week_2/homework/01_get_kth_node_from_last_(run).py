class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        cur = self.head
        new = []
        while cur.next is not None:
            new.append(cur)
            cur = cur.next
        new.reverse()
        n = 1
        m=0
        for i in new:
            n+=1
            if n == k:
                m=i
        return m


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
# [6]->[7]->[8]
print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!