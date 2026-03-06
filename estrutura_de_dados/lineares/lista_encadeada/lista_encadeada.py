class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo: "No | None" = None

    def __repr__(self):
        return f"No({self.valor})"
    
class ListaEncadeada:
    def __init__(self) -> None:
        self._cabeca: No | None = None
        self._tamanho = 0

    def inserir_inicio(self, valor) -> None:
        # Insere no início da lista
        # Complexidade: O(1)

        novo = No(valor)
        novo.proximo = self._cabeca
        self._cabeca = novo
        self._tamanho += 1

    def inserir_fim(self, valor) -> None:
        # Insere no fim da Lista
        # Complexidade: O(n)
        # Percorre até o último nó para encadear o novo nó
        novo = No(valor)
        if self._cabeca is None:
            self._cabeca = novo
        else:
            atual = self._cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo
        self._tamanho += 1

    def inserir_em(self, indice: int, valor) -> None:
            # Insere o valor em uma posição especíífica da lista
            # Complexidade: O(n)
            # Caminha até o nó anterior ao índice e reencadeia os ponteiros.
            self._validar_indice_insercao(indice)
                
            if indice == 0:
                self.inserir_inicio(valor)
                return
                
            novo = No(valor)
            anterior = self._caminhar_ate(indice - 1)
            novo.proximo = anterior.proximo
            anterior.proximo = novo
            self._tamanho += 1

    def remover_inicio(self):
        # Remove e retorna o primeiro elemento da lista
        # Complexidade: O(1)

        if self.esta_vazia():
            raise IndexError("Lista vazia.")
        valor = self._cabeca.valor
        self._cabeca = self._cabeca.proximo
        self._tamanho -= 1
        return valor
        
    def remover_fim(self):
        # Remove e retorna o último elemento da lista
        # Complexidade: O(n)
        # Percorre até o penúltimo nó para reencadear o ponteiro do último nó para None.
        if self.esta_vazia():
            raise IndexError("Lista vazia.")
        
        if self._cabeca.proximo is None:
            return self.remover_inicio()
        
        anterior = self._cabeca
        while anterior.proximo.proximo is not None:
            anterior = anterior.proximo
        
        valor = anterior.proximo.valor
        anterior.proximo = None
        self._tamanho -= 1
        return valor

    def remover_em(self, indice: int):
        # Remove e retorna o elemento em uma posição específica da lista
        # Complexidade: O(n)
        # Caminha até o nó anterior ao índice e reencadeia os ponteiros para excluir o nó do meio.
        self._validar_indice_acesso(indice)
        
        if indice == 0:
            return self.remover_inicio()
        
        anterior = self._caminhar_ate(indice - 1)
        valor = anterior.proximo.valor
        anterior.proximo = anterior.proximo.proximo
        self._tamanho -= 1
        return valor
    
    def remover_valor(self, valor) -> bool:
        # Remove a primeira ocorrência do valor na lista
        # Complexidade: O(n)
        # Percorre a lista para encontrar o valor e reencadeia os ponteiros para excluir o nó.
        #  Retorna True se o valor foi encontrado e removido, ou False caso contrário.
        if self.esta_vazia():
            return False
        
        if self._cabeca.valor == valor:
            self.remover_inicio()
            return True
        
        anterior = self._cabeca
        while anterior.proximo is not None:
            if anterior.proximo.valor == valor:
                anterior.proximo = anterior.proximo.proximo
                self._tamanho -= 1
                return True
            anterior = anterior.proximo
        
        return False