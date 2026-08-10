class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    # Display / Traverse
    def display(self):
        current = self.head

        while current:
            print(current.val, end=" -> ")
            current = current.next

        print("None")

    # Insert at Head
    def insert_head(self, val):
        new_node = ListNode(val)

        new_node.next = self.head
        self.head = new_node

    # Insert at Tail
    def insert_tail(self, val):
        new_node = ListNode(val)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node


# Use the Linked List

ll = LinkedList()


# Insert at head
ll.insert_head(1)
ll.insert_head(2)
ll.insert_head(3)

ll.display()
# 3 → 2 → 1 → None


# Insert at tail
ll.insert_tail(4)
ll.insert_tail(5)

ll.display()
# 3 -> 2 -> 1 -> 4 -> 5 -> None