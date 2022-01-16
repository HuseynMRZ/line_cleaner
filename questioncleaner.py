f = open("suallar.txt", encoding = "utf8")

a = set()

#adds all the line into set and prints unique set onto screen
for line in f:
    a.add(line)
for line in a:
    print(line)
