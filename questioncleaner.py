f = open("suallar.txt", encoding = "utf8")

a = set()

for line in f:
    a.add(line)
for line in a:
    print(line)
