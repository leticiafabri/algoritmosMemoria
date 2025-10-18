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
            
            #tira a pagina que está em primeiro (foi menos usada recentemente)
            memoria.pop(0)
            memoria.append(pagina)
    else:
        
        #se ela está na memória, tira e adiciona novamente no final (pois foi recem usada)
        memoria.remove(pagina)
        memoria.append(pagina)
    print(f"Página {pagina} -- Memória: {memoria}")

print(f"Total de faltas: {faltas}")
