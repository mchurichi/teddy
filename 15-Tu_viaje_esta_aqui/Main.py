inp = open("data.in")
out = open("data.out", "w")

n = int(inp.readline())

def suma (palabra):
    s = 1
    for c in palabra.strip():
        s *= ord(c)-64
    return s

for use_case in xrange(n):
    cometa = inp.readline()
    grupo = inp.readline()
    
    if suma(cometa) % 47 == suma(grupo) % 47:
        out.write("GO\n")
    else:
        out.write("STAY\n")

inp.close()
out.close()

exit(0)
