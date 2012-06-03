inp = open("data.in")
out = open("data.out", "w")

for line in inp:
    n, u, d = [int(i) for i in line.split()]
    pos = n
    m = 0
    
    # Ignora los solucionados
    if n == 0:
        continue
        
    while pos > 0:
        # Subida (u) / 1 minuto
        pos -= u
        m += 1
        # LLego?
        if pos <= 0:
            break
        # Descanso 1 min / Baja d posiciones
        m += 1
        pos += d
        
    out.write(str(m) + "\n")

exit(0)
