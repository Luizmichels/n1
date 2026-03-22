import subprocess
import sys

def exibir_menu():
    print("\n" + "="*45)
    print("        MENU DE EXERCÍCIOS DE BUSCA IA")
    print("="*45)
    print("[1] - Posição de Inserção de Pesquisa (Array) - André")
    print("[2] - Parênteses válidos (Pilha) - André")
    print("[3] - Jenela Deslizante Máxima (Lista) - André")
    print("[4] - Soma Dois Números (Array) - Luiz")
    print("[5] - Mesclar Duas Listas (Lista) - Luiz")
    print("[0] - Sair do programa")
    print("="*45)

def main():
    exercicios = {
        "1": "array_posicao_insercao_pesquisa.py",
        "2": "parenteses_validos.py",
        "3": "jenela_deslizante_maxima.py",
        "4": "soma_dois_numeros.py",
        "5": "mesclar_duas_listas.py"
    }

    while True:
        exibir_menu()
        escolha = input("Escolha o número do exercício que deseja executar (0-7): ")

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
            print("\nOpção inválida! Por favor, digite um número entre 0 e 7.")

if __name__ == "__main__":
    main()