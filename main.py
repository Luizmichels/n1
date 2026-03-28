import subprocess
import sys

def exibir_menu():
    print("\n" + "="*45)
    print("        MENU DOS DESAFIOS DE CODE INTERVIEW")
    print("="*45)
    print("[1] - Posição de Inserção de Pesquisa (Array) - André")
    print("[2] - Parênteses válidos (Pilha) - André")
    print("[3] - Jenela Deslizante Máxima (Lista) - André")
    print("[4] - Soma Dois Números (Array) - Luiz")
    print("[5] - Mesclar Duas Listas (Lista) - Luiz")
    print("[6] - Prefixo comum mais longo (Array) - Maria Eduarda")
    print("[7] - Faça a corda ser ótima (Pilha) - Maria Eduarda")
    print("[8] - Recipiente com mais água (Array) - Gustavo")
    print("[9] - Lista encadeada inversa (Lista) - Gustavo")
    print("[10] - Simplificar o caminho (Pilha) - Gustavo")
    print("[11] - Two Sum (Array) - Rebeca")
    print("[12] - Reverse Linked List (Lista) - Rebeca")
    print("[0] - Sair do programa")
    print("="*45)

def main():
    exercicios = {
        "1": "array_posicao_insercao_pesquisa.py",
        "2": "parenteses_validos.py",
        "3": "jenela_deslizante_maxima.py",
        "4": "soma_dois_numeros.py",
        "5": "mesclar_duas_listas.py",
        "6": "prefixo_comum_mais_longo.py",
        "7": "faca_corda_ser_otima.py",
        "8": "recipiente_com_mais_agua.py",
        "9": "lista_encadeada_inversa.py",
        "10": "simplificar_o_caminho.py",
        "11": "array_two_sum.py",
        "12": "reverse_linked_list.py"
    }

    while True:
        exibir_menu()
        escolha = input("Escolha o número do exercício que deseja executar (0-12): ")

        if escolha == "0":
            print("Saindo do programa. Até logo!")
            break
        
        elif escolha in exercicios:
            arquivo = exercicios[escolha]
            print(f"\n" + "-"*45)
            print(f"Executando: {arquivo}")
            print("-" *45 + "\n")
            
            try:
                subprocess.run([sys.executable, arquivo], check=True)
            except FileNotFoundError:
                print(f"Erro: O arquivo '{arquivo}' não foi encontrado no diretório atual.")
            except subprocess.CalledProcessError as e:
                print(f"Erro: O script '{arquivo}' parou de funcionar inesperadamente. (Código: {e.returncode})")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")
                
            print("\n" + "-"*45)
            print("Fim da execução do script.")
            input("Pressione Enter para voltar ao menu...")
            
        else:
            print("\nOpção inválida! Por favor, digite um número entre 0 e 12.")

if __name__ == "__main__":
    main()