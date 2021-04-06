phonebook = {}
for _ in range(int(input())):
    key = input()
    val = int(input())
    phonebook[key] = val
while True:
    query = input()
    if query != None:
        if query in phonebook:
            print("{}={}".format(query, phonebook[query]))
        else:
            print("Not found")
    else:
        break
