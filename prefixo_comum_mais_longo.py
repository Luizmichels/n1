# link do problema - facil
#https://leetcode.com/problems/longest-common-prefix/description/?envType=problem-list-v2&envId=array

def encontrarPrefix(self, strs):
    if not (1 <= len(strs) <= 200):
        print("Entrada inválida")
        return ""

    prefixo = ""

    if prefixo == "":
        print("Não há prefixo comum entre as strings de entrada.")
        return ""