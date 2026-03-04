from typing import Optional

class ArrayEstatico:

    def __init__(self, capacidade: int = 100) -> None:
        if capacidade <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")
        self._capacidade: int = capacidade
        self._dados: list = [None] * capacidade # Pré-alocação do array
        self._tamanho: int = 0

    def inserir_fim(self, valor) -> None:
        # Insere o valor no final no array.
        # Complexidade: O(1) no melhor caso, O(n) no pior caso (quando o array precisa ser redimensionado).
        if self.esta_cheio():
            raise OverflowError("O array está cheio. Não é possível inserir novos elementos.")
        self._dados[self._tamanho] = valor
        self._tamanho += 1

    def inserir_em(self, indice: int, valor) -> None:
        # Insere o valor em um índice específico do array.
        # Para isso, os elementos a partir do índice precisam ser deslocados para a direita (Shift).
        # Complexidade O(n) no pior caso, quando o índice é 0 (inserção no início do array), e O(1) no melhor caso, quando o índice é igual ao tamanho atual do array (inserção no final).
        if self.esta_cheio():
            raise OverflowError("O array está cheio. Não é possível inserir novos elementos.")
        self._validar_indice_insercao(indice)
        # Desloca os elementos da direita para esquerda para abrir espaço para o novo valor.
        for i in range(self._tamanho, indice, -1):
            self._dados[i] = self._dados[i - 1]
        
        self._dados[indice] = valor
        self._tamanho += 1

    def remover_fim(self):
        if self.esta_vazio():
            raise IndexError("Array vazio.")
        self._tamanho -= 1
        valor = self._dados[self._tamanho]
        self._dados[self._tamanho] = None # Limpa sentinela para evitar referências desnecessárias.
        return valor
    
    def remover_em(self, indice: int):
        # Remove o valor em um índice específico do array.
        # Para isso, os elementos a partir do índice precisam ser deslocados para a esquerda (Shift).
        # Complexidade O(n) no pior caso, quando o índice é 0 (remoção no início do array), e O(1) no melhor caso, quando o índice é igual ao tamanho atual do array - 1 (remoção no final).
        if self.esta_vazio():
            raise IndexError("Array vazio.")
        self._validar_indice_acesso(indice)

        valor = self._dados[indice]

        for i in range(indice, self._tamanho -1):
            self._dados[i] = self._dados[i + 1]

        self._tamanho -= 1
        self._dados[self._tamanho] = None # Limpa sentinela para evitar referências desnecessárias.
        return valor
    
    def obter(self, indice: int):
        # Acesso por índice.
        # Complexidade O(1).
        self._validar_indice_acesso(indice)
        return self._dados[indice]
    
    def definir(self, indice: int, valor) -> None:
        # Modificação por índice.
        # Complexidade O(1).
        self._validar_indice_acesso(indice)
        self._dados[indice] = valor

    def busca_linear(self, valor) -> int:
        # Busca linear por valor.
        # Complexidade O(n).
        # Percorre o array até encontrar o valor.
        # Não exige ordenação.
        # Retorna o índice ou -1 se o valor não for encontrado.
        for i in range(self._tamanho):
            if self._dados[i] == valor:
                return i
        return -1
    
    def busca_binaria(self, valor) -> int:
        # Busca binária por valor.
        # Complexidade O(log n).
        # Requer que o array esteja ordenado.
        # A cada iteração o espaço de busca é reduzido pela metade.
        # Retorna o índice ou -1 se o valor não for encontrado.
        esq, dir_ = 0, self._tamanho -1

        while esq <= dir_:
            meio = esq + (dir_ - esq) // 2

            if self._dados[meio] == valor:
                return meio
            elif self._dados[meio] < valor:
                esq = meio + 1
            else:
                dir_ = meio - 1
        
        return -1
    
    def esta_cheio(self) -> bool:
        return self._tamanho == self._capacidade
    
    def esta_vazio(self) -> bool:
        return self._tamanho == 0
    
    @property
    def tamanho(self) -> int:
        return self._tamanho
    
    @property
    def capacidade(self) -> int:
        return self._capacidade
    
    def __len__(self) -> int:
        return self._tamanho
    
    def __setitem__(self, indice: int, valor) -> None:
        self.definir(indice, valor)

    def __getitem__(self, indice: int):
        return self.obter(indice)
    
    def __repr__(self) -> str:
        elementos = self._dados[:self._tamanho]
        return (
            f"ArrayEstatico(capacidade={self._capacidade}, tamanho={self._tamanho}, "
            f"dados={elementos}"
        )

    def _validar_indice_acesso(self, indice: int) -> None:
        if not (0 <= indice < self._tamanho):
            raise IndexError(
                f"Índice {indice} fora dos limites [0, {self._tamanho - 1}]."
            )
        
    def _validar_indice_insercao(self, indice: int) -> None:
        if not (0 <= indice <= self._tamanho):
            raise IndexError(
                f"Índice de inserção {indice} fora dos limites [0, {self._tamanho}]"
            )

