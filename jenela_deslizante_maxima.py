def maxSlidingWindow(nums, k):
    saida = []
    
    for i in range(len(nums) - k + 1):
        janela = nums[i:i+k]
        saida.append(max(janela))
    return saida

print("Enunciado: É dado um array de inteiros  nums, e há uma janela deslizante de tamanho k que se move da extremidade esquerda do array para a extremidade direita. Você só consegue ver os knúmeros dentro da janela. A cada iteração, a janela deslizante se move uma posição para a direita. Retorne a janela deslizante máxima .\n")
print("1º lista [1,3,-1,-3,5,3,6,7], janela 3 : ", maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print("2º lista [1,8,9,2,4,6,10,3,7], janela 2: ", maxSlidingWindow([1,8,9,2,4,6,10,3,7], 2))
print("3º lista [1], janela 1                 : ", maxSlidingWindow([1], 1))

# link do problema - facil
# https://leetcode.com/problems/sliding-window-maximum/description/?envType=problem-list-v2&envId=queue&