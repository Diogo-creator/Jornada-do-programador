# Description: Sistema de despesas
import json
import os

if os.path.exists("despesas.json"):
    with open("despesas.json", "r") as arquivo:
        try:
            despesas = json.load(arquivo)
        except json.JSONDecodeError:
            despesas = []  # Se o JSON estiver vazio ou corrompido, inicia como lista vazia
else:
    despesas = []  # Se o arquivo não existir, inicia como lista vazia

# Função para adicionar uma despesa


def adicionar_despesa():
    item = input("Digite a descrição da despesa: ")
    # Ex: Mercado, Transporte, Lazer
    categoria = input("Digite a categoria da despesa: ")
    while True:
        try:
            valor = float(input("Digite o valor da despesa: R$ "))
            break
        except ValueError:
            print("Valor inválido! Digite um número válido.")

    data = input("Digite a data da despesa (AAAA-MM-DD): ")
    pago = input("A despesa foi paga? (s/n): ").strip().lower() == "s"

    despesas.append({
        "item": item,
        "categoria": categoria,
        "valor": valor,
        "data": data,
        "pago": pago
    })

    with open("despesas.json", "w") as arquivo:
        json.dump(despesas, arquivo, indent=4)

    print(f"Despesa '{item}' adicionada com sucesso!")

# mostra a lista de despesas


def listar_despesas():
    if not despesas:
        print("Nenhuma despesa registrada.")
        return

    print("\n🔹 Lista de Despesas:")
    for i, despesa in enumerate(despesas, 1):
        status = "✅ Paga" if despesa["pago"] else "❌ Não Paga"
        print(
            f"{i}. {despesa['item']} | {despesa['categoria']} | R$ {despesa['valor']:.2f} | {despesa['data']} | {status}")
    print()

# mostra as despesas pagas


def despesas_pagas():
    for despesa in despesas:
        if despesa["item"] == True:
            print(
                f"A despesa {despesa['descricao']} foi paga no valor de {despesa['valor']}")
        else:
            print(
                f"A despesa {despesa['descricao']} não foi paga no valor de {despesa['valor']}")
    print("Fim da lista")

# mostra a maior despesa


def despesa_maior():
    if not despesas:
        print("Nenhuma despesa registrada.")
        return

    maior_despesa = max(despesas, key=lambda x: x["valor"])
    print(
        f"A maior despesa foi '{maior_despesa['item']}', no valor de R$ {maior_despesa['valor']:.2f}")
    return maior_despesa


def despesa_menor():
    if not despesas:
        print("Nenhuma despesa registrada.")
        return

    menor_despesa = min(despesas, key=lambda x: x["valor"])
    print(
        f"Menor despesa: '{menor_despesa['item']}', R$ {menor_despesa['valor']:.2f}")
    return menor_despesa


def carregar_categorias():
    if os.path.exists("categorias.json"):
        try:
            with open("categorias.json", "r") as arquivo:
                return json.load(arquivo)
        except json.JSONDecodeError:
            return []
    return []

# Função para adicionar uma categoria


def adicionar_categoria():
    categorias = carregar_categorias()
    if not despesas:
        print("Nenhuma despesa registrada.")
        return

    # Exibir despesas para o usuário escolher qual editar
    print("\n🔹 Lista de Despesas:")
    for i, despesa in enumerate(despesas, 1):
        print(f"{i}. {despesa['item']} - R$ {despesa['valor']:.2f}")

    categoria = input("Digite a categoria: ")
    obs = input("Digite uma observação sobre essa categoria: ")
    despesa['categoria'] = categoria
    despesa['obs'] = obs
    with open("despesas.json", "w") as arquivo:
        json.dump(despesas, arquivo, indent=4)

    print(
        f"\nCategoria '{categoria}' adicionada à despesa '{despesas['item']}' com sucesso!")

    with open("categorias.json", "w") as arquivo:
        json.dump(categorias, arquivo, indent=4)

    print("Categoria adicionada com sucesso!")

# Buscar item atraves categorias


def busca_atraves_categorias():
    if not despesas:
        print("Nenhuma despesa registrada.")
        return

    carregar_categorias()  # Carrega as categorias

    escolha = input("Digite a categoria que deseja buscar: ").strip()

    despesas_filtradas = [
        despesa for despesa in despesas if despesa.get("categoria") == escolha]

    if not despesas_filtradas:
        print(f"Nenhuma despesa encontrada na categoria '{escolha}'.")
        return

    print(f"\n🔹 Despesas da categoria '{escolha}':")
    for i, despesa in enumerate(despesas, 1):
        status = "✅ Paga" if despesa["pago"] else "❌ Não Paga"
        print(
            f"{i}. {despesa['item']} | {despesa['categoria']} | R$ {despesa['valor']:.2f} | {despesa['data']} | {status}")
    print()


# Mostra o menu

print("Bem vindo ao sistema de despesas!")
while True:
    print("1 - Adicionar despesa")
    print("2 - Listar despesas")
    print("3 - Listar despesas pagas")
    print("4 - Mostrar maior despesa")
    print("5 - Mostrar menor despesa")
    print("6 - Carregar categoria")
    print("7 - Adicionar categoria")
    print("8 - Buscar despesa através de categoria")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionar_despesa()
    elif opcao == "2":
        listar_despesas()
    elif opcao == "3":
        despesas_pagas()
    elif opcao == "4":
        despesa_maior()
    elif opcao == "5":
        despesa_menor()
    elif opcao == "6":
        carregar_categorias()
    elif opcao == "7":
        adicionar_categoria()
    elif opcao == "8":
        busca_atraves_categorias()
    elif opcao == "0":
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
