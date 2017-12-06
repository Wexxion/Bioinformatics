data = []

for line in open("in.txt"):
    data.append(line.strip())

res = data[0]

for i in range(1, len(data)):
    res += data[i][len(data[0]) - 1]

print(res)

