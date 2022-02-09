"""
Escrevendo em Arquivos

Sempre abrir os arquivos para escrever neles. Usando bloco with:
Ao abrir o arquivo para leitura, não podemos escrever nele.
O inverso se aplica também
Usar os caracteres com o open()
========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================

# Ao usar o 'w' a gente apaga as informações do arquivo antes de começar.

with open('exemplo texto', 'w') as file:
    file.write('\nIsso foi feito no Python')

# ao usar o 'a' a gente adiciona texto ao fim do arquivo

with open('exemplo texto', 'a') as file:
    file.write('\n Agora estamos appending um texto')

# ao usar o 'x' a gente cria um arquivo novo no mesmo diretório, retorna erro caso o arquivo já exista.

with open('exemplo2', 'x') as file:
    file.write('esse é o novo arquivo')

# A DIFERENÇA ENTRE 'W' E 'X' É: o 'w' deleta o que estiver no arquivo, caso ele exista já.
# o 'x' retorna exception se o arquivo já existir. o 'x' é mais interessante para abrir novos arquivos.
"""

# Exemplo de lista de mercado

with open('lista.txt', 'w') as lista:
    while True:
        item = input("Insira um item à lista de mercado ou digite 'Sair' para terminar a lista").lower()
        if item != 'sair':
            lista.write(item + '\n')
        else:
            break

with open('lista.txt', 'r') as file:
    lista = file.read()

print(lista)
