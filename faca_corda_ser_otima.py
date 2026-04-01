#Link do problema - facil
# https://leetcode.com/problems/make-the-string-great/description/?envType=problem-list-v2&envId=stack

def verificar(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return i
        elif s[i] != s[i + 1]:
            return "Não tem combinação"


if __name__ == "__main__":
    entrada = input("Digite uma string: ")

    resultado = verificar(entrada)

    print(f"Resultado: {resultado}")   
        