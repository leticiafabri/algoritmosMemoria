

paginas = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
quadros = 8
memoria = []
faltas = 0

for pagina in paginas:
    if pagina not in memoria:
        
        #se nao está na memoria, é uma falta de página
        faltas += 1
        
        #se tem espaço na memória, adiciona
        if len(memoria) < quadros:
            memoria.append(pagina)
            
        #se estiver cheia a memoria, tira a primeira (indice 0) e adiciona outra   
        else:
            memoria.pop(0)
            memoria.append(pagina)
    print(f"Página {pagina} -- Memória: {memoria}")

print(f"Total de faltas de página: {faltas}")
