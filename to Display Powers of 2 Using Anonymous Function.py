terms = 10
result = list(map(lambda x:2 ** x , range(terms)))

print("the total terms are: , terms")
for i in range (terms):
    print("2 raised to power ", i,"is", result[i])