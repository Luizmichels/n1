# link do problema - facil
# https://leetcode.com/problems/reverse-linked-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    anterior = None
    atual = head

    while atual:
        proximo = atual.next
        atual.next = anterior
        anterior = atual
        atual = proximo

    return anterior


# Função auxiliar para imprimir a lista
def printList(head):
    atual = head
    while atual:
        print(atual.val, end=" -> ")
        atual = atual.next
    print("None")


# Criando lista: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Enunciado: Dada uma lista encadeada, inverta a ordem dos elementos.\n")

print("Lista original:")
printList(head)

# Invertendo
head = reverseList(head)

print("\nLista invertida:")
printList(head)