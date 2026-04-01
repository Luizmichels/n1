# link do problema - facil/medio
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head

    rapido = dummy
    lento = dummy

    for _ in range(n + 1):
        rapido = rapido.next

    while rapido:
        rapido = rapido.next
        lento = lento.next

    # remove o nó
    lento.next = lento.next.next

    return dummy.next


# Função para imprimir a lista
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


head = ListNode(1,
        ListNode(2,
        ListNode(3,
        ListNode(4,
        ListNode(5)))))

print("Enunciado: Dada uma lista encadeada, remova o n-ésimo nó a partir do final.\n")

print("Lista original:")
printList(head)

# Removendo o 2º do final
head = removeNthFromEnd(head, 2)

print("Lista após remover o 2º elemento a partir do final:")
printList(head)