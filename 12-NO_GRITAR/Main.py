inp = open("data.in")
out = open("data.out", "w")

# numero de lineas de la carta
n = int(inp.readline())

for l in xrange(n):
    line = inp.readline().upper()
    words = line.split()
    for word in words:
        if (word.startswith("P") and word.endswith("R")) or (word.startswith("H") and word.find("O") != -1 ):
            out.write("#" * len(word))
        else:
            out.write(word)
        if word != words[-1]:
            out.write(" ")
            
    out.write("\n")

inp.close()
out.close()

exit(0)
