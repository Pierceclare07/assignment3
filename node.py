# Implement your Node class here
class Node:
    """
    Singly-linked list node for Stack/Queue.
    Stores `value` and pointer to `next` node (default None).
    """
    __slots__ = ("value", "next")

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value!r})"

pass