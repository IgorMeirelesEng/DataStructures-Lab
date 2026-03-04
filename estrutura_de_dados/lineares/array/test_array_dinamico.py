"""
Testes — ArrayDinamico
"""

import traceback
from array_dinamico import ArrayDinamico

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

def teste_crescimento() -> None:
    secao("Crescimento automático (× 2)")
    arr = ArrayDinamico()
    print(f"  Inicial: {arr}")

    for v in range(1, 10):
        print(f"  inserir_fim({v}):")
        arr.inserir_fim(v)
        print(f"    {arr}")

    assert arr.tamanho == 9
    assert arr.capacidade == 16   
    ok("Capacidade final: 16 após 9 inserções")


def teste_encolhimento() -> None:
    secao("Encolhimento automático (÷ 2)")
    arr = ArrayDinamico()

    for v in range(1, 9):
        arr.inserir_fim(v)   # capacidade sobe até 16!!
    print(f"  Cheio com 8 elementos: {arr}")

    while arr.tamanho > 0:
        val = arr.remover_fim()
        print(f"  remover_fim() → {val}:  {arr}")

    ok("Encolhimento acompanhou as remoções")


def teste_insercao() -> None:
    secao("Inserção")
    arr = ArrayDinamico()

    for v in [10, 20, 30, 40]:
        arr.inserir_fim(v)
    print(f"  Após inserir 10,20,30,40 no fim:\n    {arr}")

    print(f"  inserir_em(1, 99):")
    arr.inserir_em(1, 99)
    print(f"    {arr}")

    print(f"  inserir_em(0, 5)  (início):")
    arr.inserir_em(0, 5)
    print(f"    {arr}")

    assert len(arr) == 6
    ok("Tamanho esperado: 6")
    assert arr[0] == 5 and arr[2] == 99
    ok("Posições corretas após inserções")


def teste_remocao() -> None:
    secao("Remoção")
    arr = ArrayDinamico()

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
    arr = ArrayDinamico()

    for v in [100, 200, 300]:
        arr.inserir_fim(v)
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
    arr = ArrayDinamico()

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
    arr = ArrayDinamico()

    for v in [1, 3, 5, 7, 9, 11, 13]:
        arr.inserir_fim(v)
    print(f"  {arr}")

    casos = [(7, 3), (1, 0), (13, 6), (6, -1)]
    for valor, esperado in casos:
        idx = arr.busca_binaria(valor)
        print(f"  Buscar {valor:>2} → índice {idx:>2} (esperado: {esperado})")
        assert idx == esperado

    ok("Busca binária OK")


def teste_vazio() -> None:
    secao("Limites — array vazio")
    arr = ArrayDinamico()

    print(f"  Recém-criado: {arr}  →  vazio={arr.esta_vazio()}")
    assert arr.esta_vazio()
    ok("Recém-criado está vazio")

    print(f"  Tentando remover de array vazio...")
    try:
        arr.remover_fim()
        falhou("Deveria lançar IndexError")
    except IndexError as e:
        ok(f"IndexError capturado: {e}")

if __name__ == "__main__":
    print("*" * 50)
    print("ARRAY DINÂMICO (Python) — Testes".center(50))
    print("*" * 50)

    testes = [
        teste_crescimento,
        teste_encolhimento,
        teste_insercao,
        teste_remocao,
        teste_acesso,
        teste_busca_linear,
        teste_busca_binaria,
        teste_vazio,
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