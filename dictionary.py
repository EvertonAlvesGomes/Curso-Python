### dictionary.py

## Estudo sobre dicionários em Python

# Tuplas: ( )
# Listas: [ ]
# Dicionários: { }

# Os índices de dicionários podem ser personalizados.

# Declarando um dicionário:
# Objeto: dict()
# Chaves: dados = {     ...      } 

# Dicionários não precisam da função append() para adicionar elementos.
# Simplesmente faça dados['<param>'] = <valor>

# Excluindo dados de um dicionário: del dados['<param>']

# Elementos de dicionários são referenciados por colchetes. 
# Lembre-se que dicionários são declarados por chaves.

# Fatiamento não é válido para dicionários. Utilize o método copy().

# Exemplo:
filme = {
    'titulo':'Star Wars',
    'ano':'1977',
    'diretor':'George Lucas'
}

print(filme.values())   # valores: 'Star Wars', '1977', 'George Lucas'
print(filme.keys())     # chaves: 'titulo', 'ano', 'diretor'
print(filme.items())    # itens: chaves e valores

print('\n')
for k,v in filme.items():
    print(f'{k}: {v}')