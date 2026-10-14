"""Parte 3: recomendação de usuários pelo índice de Jaccard."""

import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


USUARIOS_INICIAIS = {
    "Ana": {"rock", "jazz", "cinema", "games"},
    "Bia": {"jazz", "cinema", "séries", "viagens"},
    "Caio": {"games", "tecnologia", "cinema"},
}


def normalizar_interesses(texto):
    """Separa, limpa, padroniza e elimina interesses repetidos."""
    return {item.strip().lower() for item in texto.split(",") if item.strip()}


def calcular_jaccard(interesses_a, interesses_b):
    """Calcula |A ∩ B| / |A ∪ B|; por convenção, ∅ com ∅ vale 0."""
    comuns = interesses_a & interesses_b
    todos = interesses_a | interesses_b
    indice = len(comuns) / len(todos) if todos else 0.0
    return comuns, todos, indice


def recomendar(nome, usuarios):
    """Compara um usuário com todos os outros e preserva empates."""
    if nome not in usuarios:
        raise ValueError("usuário não encontrado")
    comparacoes = []
    for outro_nome, interesses in usuarios.items():
        if outro_nome != nome:
            comuns, todos, indice = calcular_jaccard(usuarios[nome], interesses)
            comparacoes.append({
                "nome": outro_nome,
                "comuns": comuns,
                "uniao": todos,
                "indice": indice,
            })
    if not comparacoes:
        return [], []
    maior = max(item["indice"] for item in comparacoes)
    melhores = [item["nome"] for item in comparacoes if item["indice"] == maior]
    return comparacoes, melhores


def mostrar_usuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    for nome, interesses in usuarios.items():
        lista = ", ".join(sorted(interesses)) if interesses else "nenhum"
        print(f"- {nome}: {lista}")


def executar_parte3():
    usuarios = {nome: set(interesses) for nome, interesses in USUARIOS_INICIAIS.items()}
    while True:
        print("\nPARTE 3 — RECOMENDAÇÃO POR INTERESSES")
        print("1 - Cadastrar usuário\n2 - Listar usuários\n3 - Recomendar\n0 - Voltar")
        opcao = input("Escolha: ").strip()
        if opcao == "0":
            return
        if opcao == "1":
            nome = input("Nome: ").strip()
            if not nome:
                print("O nome não pode ficar vazio.")
                continue
            if nome in usuarios:
                print("Já existe um usuário com esse nome.")
                continue
            usuarios[nome] = normalizar_interesses(input("Interesses separados por vírgula: "))
            print("Usuário cadastrado.")
        elif opcao == "2":
            mostrar_usuarios(usuarios)
        elif opcao == "3":
            nome = input("Nome exato do usuário: ").strip()
            try:
                comparacoes, melhores = recomendar(nome, usuarios)
                if not comparacoes:
                    print("Cadastre outra pessoa para realizar comparações.")
                    continue
                for item in comparacoes:
                    comuns = ", ".join(sorted(item["comuns"])) or "nenhum"
                    print(
                        f"{nome} × {item['nome']}: comuns={{{comuns}}}; "
                        f"|interseção|={len(item['comuns'])}; |união|={len(item['uniao'])}; "
                        f"J={item['indice']:.2f} ({item['indice']:.1%})"
                    )
                print("Maior afinidade:", ", ".join(melhores))
                if len(melhores) > 1:
                    print("Houve empate; todos os nomes acima são recomendações.")
            except ValueError as erro:
                print(f"Erro: {erro}.")
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    executar_parte3()
