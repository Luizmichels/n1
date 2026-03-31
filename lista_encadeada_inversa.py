class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, left, right):
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    current = prev.next

    for _ in range(right - left):
        temp = current.next
        current.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("||")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

print("Lista original:")
print_list(head)

novo = reverseBetween(head, 1, 5)

print("Lista totalmente invertida:")
print_list(novo)

# link do problema - médio
# https://leetcode.com/problems/reverse-linked-list-ii/description/