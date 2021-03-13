### listas.py

## Estudando listas em Python

moto = ['Rodas','Motor','Relação','Freios']     # lista inicial

moto.append('Embreagem')    # adicona elemento ao final da lista

moto.insert(2, 'Transmissão')   # insere o elemento 'Transmissão' na posição 2,
                                # sem substituir o elemento atual dessa posição.
                                # O elementos subsequentes serão deslocados para a direita

moto.remove('Motor')    # remove o elemento, deslocando para a esquerda os elementos seguintes
# Alternativa: del moto[1]  -> remove o elemento da posição 1
# Alternativa 2: moto.pop(1) -> remove o elemento da posição 1
# Observação: o método pop geralmente é utilizado para remover o último elemento da lista.

moto.pop()  # remove o último elemento

# ---------------
print(moto)


# ----------
valores = [8,2,4,10,1,3,6]
valores.sort()      # organiza em ordem crescente
valores.sort(reverse=True)      # organiza em ordem decrescente

print(valores)
print(f'A lista valores tem {len(valores)} elementos.')


# Uma maneira elegante de declarar uma lista é pelo construtor list(), 
# uma vez que list é objeto da classe de mesmo nome.
# Exemplo: lista = list()   # cria uma lista vazia

# Atribuição de listas em Python:
# a = [2, 4, 5, 9]
# b = a     # as listas b, a são interligadas. Qualquer alteração em uma das listas altera a outra
# b = a[:]  # o conteúdo de a é copiado para b, sem estabeler uma relação entre elas.