# link do problema - facil
# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    mapa = {}

    for i, num in enumerate(nums):
        complemento = target - num

        if complemento in mapa:
            return [mapa[complemento], i]

        mapa[num] = i

print('Enunciado: Dado um array de inteiros, retorne os índices de dois números que somam o valor alvo.\n')

print('Array [2, 7, 11, 15] | Target = 9')
print('Resultado:', twoSum([2, 7, 11, 15], 9))

print('\nArray [3, 2, 4] | Target = 6')
print('Resultado:', twoSum([3, 2, 4], 6))

print('\nArray [3, 3] | Target = 6')
print('Resultado:', twoSum([3, 3], 6))