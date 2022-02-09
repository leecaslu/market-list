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
