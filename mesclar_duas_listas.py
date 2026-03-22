def mergeTwoLists(list1, list2):
    lista_completa = list1
    lista_completa.extend(list2)
    lista_completa.sort()
    return lista_completa



list1 = [1,2,4]
list2 = [3,1,4]

print("Enunciado: Informar duas listas, mesclar as duas lista e deve ser retornado uma lista única que esteja ordenada.")
print(f"Primeira lista: {list1}")
print(f"Segunda lista: {list2}")

print(mergeTwoLists(list1, list2))
