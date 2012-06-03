inp = open("data.in")
out = open("data.out", "w")

n = int(inp.readline())
output = ""

for use_case in xrange(n):
    line = inp.readline()
    desde, hasta = [int(i) for i in line.split()]
    c = 0
    for num in xrange(desde, hasta+1):
        c += str(num).count("1")
    out.write(str(c) + "\n")

inp.close()
out.close()
exit(0)
