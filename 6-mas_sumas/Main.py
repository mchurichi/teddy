import sys

inp = open("data.in")
out = open("data.out", "w")


for line in inp:
    data = line.split()
    if len(data) != 1:
        out.write(str(int(data[0]) + int(data[1]) + int(data[2])) + "\n")

inp.close()
out.close()
sys.exit(0)
