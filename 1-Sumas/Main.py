import sys

inp = open("data.in")
out = open("data.out", "w")

for line in inp:
    data = line.split()
    out.write(str(int(data[0]) + int(data[1])) + "\n")

inp.close()
out.close()
sys.exit(0)
