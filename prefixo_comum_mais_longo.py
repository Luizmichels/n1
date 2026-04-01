# link do problema - facil
#https://leetcode.com/problems/longest-common-prefix/description/?envType=problem-list-v2&envId=array

class Solucao:
    def encontrarPrefix(self, strs):
        if not (1 <= len(strs) <= 200):
            print("Entrada inválida")
            return ""

        prefixo = strs[0]

        for palavra in strs[1:]:
            while not palavra.startswith(prefixo):
                prefixo = prefixo[:-1]
                if prefixo == "":
                    print("Não há prefixo comum entre as strings de entrada.")
                    return ""

        return prefixo


if __name__ == "__main__":
    entrada = input("Digite as palavras separadas por espaço: ")
    lista = entrada.split()

    solucao = Solucao()
    resultado = solucao.encontrarPrefix(lista)

    print(f"Prefixo comum mais longo: '{resultado}'")