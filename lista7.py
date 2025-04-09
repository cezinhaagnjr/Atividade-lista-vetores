tupla = ("Alice", "Carlos", "César", "Clara")

print(tupla)

lista_temp = list(tupla)

lista_temp[2] = "João"
tupla = tuple(lista_temp)
print(tupla)