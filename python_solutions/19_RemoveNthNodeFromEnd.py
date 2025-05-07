#give the head of a linked list, remove the nth node from end and return head
#immediately, I'm thinking we can use two pointers, one faster and one slower, one will reach the end and count
#the number of elements in the list, one is also needed to keep track of the next element after the nth node
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head
        while first is not None:
            length += 1
            first = first.next
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next

def test_solution():
    solution = Solution()

    head1 = create_linked_list([1,2,3,4,5])
    n1 = 2
    result1 = solution.removeNthFromEnd(head1, n1)
    print(f"Test 1: {linked_list_to_list(result1)}")

    head2 = create_linked_list([1])
    n2 = 1
    result2 = solution.removeNthFromEnd(head2, n2)
    print(f"Test 2: {linked_list_to_list(result2)}")

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def create_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

if __name__ == "__main__":
    test_solution()