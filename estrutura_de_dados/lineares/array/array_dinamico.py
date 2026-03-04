from typing import Optional

class ArrayDinamico:
    _CAPACIDADE_INICIAL: int = 4

    def __init__(self) -> None:
        self._capacidade: int = self._CAPACIDADE_INICIAL
        self._dados: list = [None] * self._capacidade # Pré-alocação do array
        self._tamanho: int = 0

    def inserir_fim(self, valor) -> None:
        # Insere o valor no final do array.
        # Complexidade: O(1) amortizada, pois o array é redimensionado quando necessário.
        if self._tamanho == self._capacidade:
            self._redimensionar(2 * self._capacidade) # Dobra a capacidade quando o array estiver cheio.
        
        self._dados[self._tamanho] = valor
        self._tamanho += 1

    def inserir_em(self, indice: int, valor) -> None:
        # Insere o valor em um índice específico do array.
        # Para isso, os elementos a partir do índice precisam ser deslocados para a direita (Shift).
        # Complexidade O(n)

        self._validar_indice_insercao(indice)

        if self._tamanho == self._capacidade:
            self._redimensionar(2 * self._capacidade) # Dobra a capacidade quando o array estiver cheio.

        for i in range(self._tamanho, indice, - 1):
            self._dados[i] = self._dados[i - 1]

        self._dados[indice] = valor
        self._tamanho += 1

    def remover_fim(self):
        # Remove e retorna o último elemento.
        # Complexidade: O(1) amortizada, pois o array é redimensionado quando necessário.
        # Enconlhe o array se ficar muito vazio (tamanho <= capacidade / 4)
        if self.esta_vazio():
            raise IndexError("Array vazio.")
        
        self._tamanho -= 1
        valor = self._dados[self._tamanho]
        self._dados[self._tamanho] = None # Limpa sentinela para evitar referências desnecessárias.
        if self._tamanho <= self._capacidade // 4 and self._capacidade > self._CAPACIDADE_INICIAL:
            self._redimensionar(max(self._capacidade // 2, self._CAPACIDADE_INICIAL)) # Encolhe a capacidade para metade quando o array estiver muito vazio.

        return valor
    
    def remover_em(self, indice: int):
        # Remove o valor em um índice específico do array.
        # Para isso, os elementos a partir do índice precisam ser deslocados para a esquerda (Shift).
        # Complexidade O(n)
        
        if self.esta_vazio():
            raise IndexError("Array vazio.")
        
        self._validar_indice_acesso(indice)

        valor = self._dados[indice]

        for i in range(indice, self._tamanho -1):
            self._dados[i] = self._dados[i + 1]

        self._tamanho -= 1
        self._dados[self._tamanho] = None # Limpa sentinela para evitar referências desnecessárias.

        if self._tamanho <= self._capacidade // 4 and self._capacidade > self._CAPACIDADE_INICIAL:
            self._redimensionar(max(self._capacidade // 2, self._CAPACIDADE_INICIAL)) # Encolhe a capacidade para metade quando o array estiver muito vazio.

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
        # Busca linear por um valor.
        # Complexidade O(n).
        # Retorna o índice do valor encontrado ou -1 se não encontrado. 
        for i in range(self._tamanho):
            if self._dados[i] == valor:
                return i
        return -1
    
    def busca_binaria(self, valor) -> int:
        # Busca binária por um valor.
        # Complexidade O(log n).
        # Requer que o array esteja ordenado.
        # Retorna o índice do valor encontrado ou -1 se não encontrado. 
        esquerda, direita = 0, self._tamanho - 1
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            if self._dados[meio] == valor:
                return meio
            elif self._dados[meio] < valor:
                esquerda = meio + 1
            else:
                direita = meio - 1
        return -1
    
    def _redimensionar(self, nova_capacidade: int) -> None:
        # Aloca um novo buffer e copia os dados.
        # Equivalente ao realloc() em C.

        print(f"Redimensionando: {self._capacidade} -> {nova_capacidade}")
        novo_buffer = [None] * nova_capacidade
        for i in range(self._tamanho):
            novo_buffer[i] = self._dados[i]

        self._dados = novo_buffer
        self._capacidade = nova_capacidade

    def esta_vazio(self) -> bool:
        return self._tamanho == 0
    
    def esta_cheio(self) -> bool:
        return self._tamanho == self._capacidade
    
    @property
    def tamanho(self) -> int:
        return self._tamanho
    
    @property
    def capacidade(self) -> int:
        return self._capacidade
    
    def __len__(self) -> int:
        return self._tamanho
    
    def __getitem__(self, indice: int):
        return self.obter(indice)
    
    def __setitem__(self, indice: int, valor) -> None:
        self.definir(indice, valor)

    def __repr__(self) -> str:
        elementos = self._dados[:self._tamanho]
        return (
            f"ArrayDinamico(capacidade={self._capacidade}, tamanho={self._tamanho}, "
            f"elementos={elementos})"
        )
    
    def _validar_indice_acesso(self, indice: int) -> None:
        if not (0 <= indice < self._tamanho):
            raise IndexError(
                f"Índice {indice} fora dos limites do array (0 a {self._tamanho - 1})."
                )
        
    def _validar_indice_insercao(self, indice: int) -> None:
        if not (0 <= indice <= self._tamanho):
            raise IndexError(
                f"Índice de inserção {indice} fora dos limites do array (0 a {self._tamanho})."
                )