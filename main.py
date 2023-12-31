
def caixa(notas):
    listNotas = notas.keys().sort(reverse=True)
    while(True):
        valor = int(input("Qual valor do saque?\nmin: R$10\nmax R$:600\n"))
        if valor < 10:
            print("O valor deve ser maior ou igual a 10")
        elif valor > 600:
            print("O valor deve ser menor ou igual a 600")
        else:
            break

    for nota in listNotas:
        while valor>=nota:
            valor -= nota
            notas[nota] += 1
        
    for nota in listNotas:
        if notas[nota] > 0:
            print(str(notas[nota]) + " notas de R$" + str(nota))

notas = {100:0, 50:0, 10:0, 5:0, 1:0}
caixa(notas)