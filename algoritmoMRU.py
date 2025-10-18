paginas = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
quadros = 8
memoria = []
faltas = 0

for pagina in paginas:
    if pagina not in memoria:
        faltas += 1
        if len(memoria) < quadros:
            memoria.append(pagina)
        else:
            
            #tira o ultimo item da lista (a que acabou de ser usada)
            memoria.pop(-1)
            memoria.append(pagina)
    else:
        memoria.remove(pagina)
        memoria.append(pagina)
    print(f"Página {pagina} -- Memória: {memoria}")

print(f"Total de faltas de página: {faltas}")
