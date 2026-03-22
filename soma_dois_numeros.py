def addTwoNumbers(l1, l2):
    l1.reverse()
    l2.reverse()
    l1, l2 = int(''.join(map(str,l1))), int(''.join(map(str,l2)))
    soma = l1+l2
    lista_soma = [int(numero) for numero in str(soma)]
    return lista_soma

l1 = [2,4,3]
l2 = [5,6,4]

print("Enunciado: Informe duas listas que não devem ser vazias e nem conter valores negativos. Os números digitados são armazenados em ordem inversa, e cada uma das lista devem ser passar a ser composta por essa ordem inversa mas agora sendo somente um unico inteiro. Faça a soma dos dois números e retorne ele como sendo uma lista encadeada.")
print(f"Primeira lista: {l1}")
print(f"Segunda lista: {l2}")
print(addTwoNumbers(l1,l2))

# link do problema - médio 
# https://leetcode.com/problems/add-two-numbers/description/?topicSlugs=array