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
    # --------------------------------
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

    # Insert at Position
    def insert_at_position(self, val, position):

        # Invalid position
        if position < 0:
            print("Invalid position")
            return

        # Position 0 = Insert at Head
        if position == 0:
            self.insert_head(val)
            return

        new_node = ListNode(val)

        current = self.head

        # Reach the node BEFORE the position
        for _ in range(position - 1):

            if current is None:
                print("Invalid position")
                return

            current = current.next

        # Position is outside the list
        if current is None:
            print("Invalid position")
            return

        # Connect new node
        new_node.next = current.next
        current.next = new_node


# Use the Linked List

ll = LinkedList()


# Insert at Head
ll.insert_head(1)
ll.insert_head(2)
ll.insert_head(3)

ll.display()
# 3 -> 2 -> 1 -> None


# Insert at Tail
ll.insert_tail(4)
ll.insert_tail(5)

ll.display()
# 3 -> 2 -> 1 -> 4 -> 5 -> None


# Insert at Position
ll.insert_at_position(10, 2)

ll.display()
# 3 -> 2 -> 10 -> 1 -> 4 -> 5 -> None