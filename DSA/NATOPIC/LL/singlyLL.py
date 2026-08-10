print("Hello, World!")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(1)
node2 = ListNode(2) 
node3 = ListNode(3)
node1.next = node2
node2.next = node3

head = node1
# print(head)
# print(head.val)
# print(head.next.val)
# print(head.next.next.val)
current = head

# while current.next: # Gives 1 and 2 but not 3...current.next is None for the last node(here 30)

while current: # Gives 1, 2 and 3
    print(current.val)
    current = current.next