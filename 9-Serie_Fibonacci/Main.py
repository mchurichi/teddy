inp = open("data.in")
out = open("data.out", "w")

# parsea todas los numeros
lines = [int(n) for n in inp.readlines()]

# genera la serie fibonacci hasta el mayor numero
fibonacci = []
for n in xrange(max(lines)):
    if n <=1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[n-1] + fibonacci[n-2])

# obtiene el numero de la serie en la posicion dada
for n in lines:
    out.write(str(fibonacci[n-1]) + "\n" )

inp.close()
out.close()
exit(0)
