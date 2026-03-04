import traceback
from array_estatico import ArrayEstatico

def secao(titulo: str) -> None:
    print("\n")
    print(f"{"*"*50}")
    print(f"{titulo.center(50)}")
    print(f"{"*"*50}")


def ok(msg: str) -> None:
    print(f"  ✓ {msg}")


def falhou(msg: str) -> None:
    print(f"  ✗ {msg}")
    raise AssertionError(msg)

def teste_insercao() -> None:
    secao("Inserção")
    arr = ArrayEstatico(10)

    arr.inserir_fim(10)
    arr.inserir_fim(20)
    arr.inserir_fim(30)
    arr.inserir_fim(40)
    print(f"  Após inserir 10,20,30,40 no fim:\n    {arr}")

    arr.inserir_em(1, 99)
    print(f"  Após inserir 99 na posição 1:\n    {arr}")

    arr.inserir_em(0, 5)
    print(f"  Após inserir 5 na posição 0 (início):\n    {arr}")

    assert len(arr) == 6
    ok("Tamanho esperado: 6")

    # sintaxe de lista (protocolo __getitem__ criado!!)
    assert arr[0] == 5
    assert arr[2] == 99
    ok("Acesso via arr[i] funciona")


def teste_remocao() -> None:
    secao("Remoção")
    arr = ArrayEstatico(10)

    for v in range(10, 60, 10):
        arr.inserir_fim(v)          
    print(f"  Estado inicial:\n    {arr}")

    val = arr.remover_fim()
    print(f"  remover_fim() → {val}:\n    {arr}")
    assert val == 50

    val = arr.remover_em(1)
    print(f"  remover_em(1) → {val}:\n    {arr}")
    assert val == 20

    assert len(arr) == 3
    ok("Tamanho esperado: 3")


def teste_acesso() -> None:
    secao("Acesso por índice — O(1)")
    arr = ArrayEstatico(5)
    arr.inserir_fim(100)
    arr.inserir_fim(200)
    arr.inserir_fim(300)
    print(f"  Array: {arr}")

    for i in range(3):
        print(f"  arr[{i}] → {arr[i]}")

    print(f"  Tentando arr[99] em array de tamanho {len(arr)}...")
    try:
        _ = arr[99]
        falhou("Deveria lançar IndexError")
    except IndexError as e:
        ok(f"IndexError capturado: {e}")

    print(f"  Antes: arr[1] = {arr[1]}  →  atribuindo 999...")
    arr[1] = 999
    print(f"  Depois: arr[1] = {arr[1]}")
    assert arr[1] == 999
    ok("Atribuição via arr[i] = v funciona")


def teste_busca_linear() -> None:
    secao("Busca Linear — O(n)")
    arr = ArrayEstatico(10)

    for v in [5, 3, 8, 1, 9, 2, 7]:
        arr.inserir_fim(v)
    print(f"  {arr}")

    idx = arr.busca_linear(9)
    print(f"  Buscar 9  → índice {idx} (esperado: 4)")
    assert idx == 4

    idx = arr.busca_linear(99)
    print(f"  Buscar 99 → índice {idx} (esperado: -1)")
    assert idx == -1

    ok("Busca linear OK")


def teste_busca_binaria() -> None:
    secao("Busca Binária — O(log n)  [array ordenado]")
    arr = ArrayEstatico(10)

    for v in [1, 3, 5, 7, 9, 11, 13]:
        arr.inserir_fim(v)
    print(f"  {arr}")

    casos = [(7, 3), (1, 0), (13, 6), (6, -1)]
    for valor, esperado in casos:
        idx = arr.busca_binaria(valor)
        print(f"  Buscar {valor:>2} → índice {idx:>2} (esperado: {esperado})")
        assert idx == esperado

    ok("Busca binária OK")


def teste_limites() -> None:
    secao("Limites (cheio / vazio)")
    arr = ArrayEstatico(3)

    print(f"  Recém-criado: {arr}  →  vazio={arr.esta_vazio()}")
    assert arr.esta_vazio()
    ok("Recém-criado está vazio")

    for v in [1, 2, 3]:
        arr.inserir_fim(v)
        print(f"  inserir_fim({v}) → {arr}  cheio={arr.esta_cheio()}")
    assert arr.esta_cheio()
    ok("Array com 3 elementos está cheio")

    print(f"  Tentando inserir 4 no array cheio...")
    try:
        arr.inserir_fim(4)
        falhou("Deveria lançar OverflowError")
    except OverflowError as e:
        ok(f"OverflowError capturado: {e}")

    for _ in range(3):
        val = arr.remover_fim()
        print(f"  remover_fim() → {val}  |  {arr}  vazio={arr.esta_vazio()}")
    assert arr.esta_vazio()
    ok("Após remover tudo, está vazio novamente")

    print(f"  Tentando remover de array vazio...")
    try:
        arr.remover_fim()
        falhou("Deveria lançar IndexError")
    except IndexError as e:
        ok(f"IndexError capturado: {e}")


# ── main ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("═" * 46)
    print("  ARRAY ESTÁTICO (Python) — Testes           ")
    print("═" * 46)

    testes = [
        teste_insercao,
        teste_remocao,
        teste_acesso,
        teste_busca_linear,
        teste_busca_binaria,
        teste_limites,
    ]

    erros = 0
    for teste in testes:
        try:
            teste()
        except Exception:
            erros += 1
            traceback.print_exc()

    print()
    if erros == 0:
        print("✅  Todos os testes passaram!")
    else:
        print(f"❌  {erros} teste(s) falharam.")
    print()