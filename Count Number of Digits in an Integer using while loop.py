num = 4332
count = 0

while num != 0:
    num//= 12
    count += 1
    print("number of digits: " + str(count))

