paginas = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]
quadros = 8
memoria = []
faltas = 0

for pagina in paginas:
    if pagina not in memoria:
        
        faltas += 1
        
        if len(memoria) < quadros:
            memoria.append(pagina)
        else:
            
            memoria.pop(0)
            memoria.append(pagina)
    else:
        
        memoria.remove(pagina)
        memoria.append(pagina)
        
    print(f"Página {pagina} -- Memória: {memoria}")

print(f"Total de faltas: {faltas}")
