def searchInsert(nums, target):
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)

print('Enunciado: Dado um array ordenado de inteiros distintos e um valor alvo, retorne o índice se o valor alvo for encontrado. Caso contrário, retorne o índice onde ele estaria se fosse inserido na ordem correta.\n')
print('Array a ser utilizado [1,3,5,6]')
print(f'Primeiro alvo 5: ', searchInsert([1,3,5,6], 5))
print(f'Segundo alvo 2:  ', searchInsert([1,3,5,6], 2))
print(f'Terceiro alvo 3: ', searchInsert([1,3,5,6], 7))

# link do problema - facil
# https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=array&