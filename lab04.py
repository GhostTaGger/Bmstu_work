class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def equal_brackets(string: str):
        stack = Stack()
        open_brackets = ['(', '[', '{']
        close_brackets = [')', ']', '}']
        match_brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in string:
            if char in open_brackets:
                stack.push(char)
            elif char in close_brackets:
                if stack.is_empty() or stack.peek() != match_brackets[char]:
                    return "Brackets does not correct!"
                else:
                    stack.pop()

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.is_empty():
            value = self.head.value
            self.head = self.head.next
            return value
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.head.value
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("peek from empty queue")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.is_empty():
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return value
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.head.value
        else:
            raise IndexError("peek from empty queue")

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

class ArrayDeque:
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.deque.pop(0)
        else:
            raise IndexError("remove from empty deque")

    def remove_rear(self):
        if not self.is_empty():
            return self.deque.pop()
        else:
            raise IndexError("remove from empty deque")

    def peek_front(self):
        if not self.is_empty():
            return self.deque[0]
        else:
            raise IndexError("peek from empty deque")

    def peek_rear(self):
        if not self.is_empty():
            return self.deque[-1]
        else:
            raise IndexError("peek from empty deque")

    def is_empty(self):
        return len(self.deque) == 0

    def size(self):
        return len(self.deque)

class LinkedListDeque:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_rear(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_front(self):
        if not self.is_empty():
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return value
        else:
            raise IndexError("remove from empty deque")

    def remove_rear(self):
        if not self.is_empty():
            if self.head == self.tail:
                value = self.head.value
                self.head = self.tail = None
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                value = self.tail.value
                self.tail = current
                self.tail.next = None
            return value
        else:
            raise IndexError("remove from empty deque")

    def peek_front(self):
        if not self.is_empty():
            return self.head.value
        else:
            raise IndexError("peek from empty deque")

    def peek_rear(self):
        if not self.is_empty():
            return self.tail.value
        else:
            raise IndexError("peek from empty deque")

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
