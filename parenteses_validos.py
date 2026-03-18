def isValid(s: str):
    pilha = []
    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in pares:  # é fechamento
            if not pilha or pilha[-1] != pares[char]:
                return False
            pilha.pop()
        else:  # é abertura
            pilha.append(char)

    return len(pilha) == 0


print("Enunciado: Dada uma string scontendo apenas os caracteres '(', ')', '{', '}', '['e ']', determine se a string de entrada é válida.\n")
print('Uma sequência de entrada é válida se:')
print('  - Os colchetes abertos devem ser fechados pelo mesmo tipo de colchetes.')
print('  - Os colchetes abertos devem ser fechados na ordem correta.')
print('  - Cada parêntese fechado tem um parêntese aberto correspondente do mesmo tipo.\n')

print("1º ():       ", isValid('()'))
print("2º (()[]{}): ", isValid('(()[]{})'))
print("3º (]:       ", isValid('(]'))
print("4º ([]):     ", isValid('([])'))
print("5º ([)]:     ", isValid('([)]'))

# link do problema
# https://leetcode.com/problems/valid-parentheses/description/?envType=problem-list-v2&envId=stack&