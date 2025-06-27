class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        # Create dummy head and tail to simplify edge case handling
        self.head = Node()  # Dummy head
        self.tail = Node()  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        # Check index validity
        if index < 0 or index >= self.size:
            return -1
        # Optimize traversal: from head or tail
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - 1, index, -1):
                curr = curr.prev
        return curr.val

    def addAtHead(self, val: int) -> None:
        self._add(self.head, self.head.next, val)

    def addAtTail(self, val: int) -> None:
        self._add(self.tail.prev, self.tail, val)

    def addAtIndex(self, index: int, val: int) -> None:
        # Insert only if 0 <= index <= size
        if index < 0 or index > self.size:
            return
        # Find prev and next nodes
        if index < self.size // 2:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            nxt = prev.next
        else:
            nxt = self.tail
            for _ in range(self.size - index):
                nxt = nxt.prev
            prev = nxt.prev
        self._add(prev, nxt, val)

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        # Find node to delete
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - 1, index, -1):
                curr = curr.prev
        self._remove(curr)

    # Internal helper: insert node between prev and next
    def _add(self, prev: Node, nxt: Node, val: int):
        node = Node(val)
        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node
        self.size += 1

    # Internal helper: remove node from list
    def _remove(self, node: Node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1
