from file_organizer import organizar_pasta


def main():
    print("Organizador de Arquivos")
    print("=" * 30)

    caminho = input("Digite o caminho da pasta que deseja organizar: ")

    try:
        movidos = organizar_pasta(caminho)

        if not movidos:
            print("Nenhum arquivo foi movido.")
            return

        print(f"\n{len(movidos)} arquivo(s) organizado(s):\n")

        for arquivo in movidos:
            print(f"{arquivo['arquivo']} → {arquivo['categoria']}")

    except FileNotFoundError as erro:
        print(f"Erro: {erro}")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")


if __name__ == "__main__":
    main()