import math
list1 = [1, 3, 4, 16, 32, 8, 64, 4, 128, 2, 256, 32]
list2 = [16, 2, 4, 2, 128, 64, 16, 7, 1, 64, 32, 16, 5, 8]
uoc = {}

numb = int(input("Chon 1 so: "))

for i in range(1, numb+1):
    if numb % i == 0:
        uoc[i] = []

print("Cac cap so co tich bang {} trong list 2 la: ".format(numb))

for i in range(len(list1)):
    for n in uoc:
        if list1[i] == n:
            uoc[n].append(i)

for i in uoc:
    if int(i) < math.floor(math.sqrt(numb)) and uoc[i] != [] and uoc[math.floor(numb/i)] != []:
        print("{} va {} o vi tri so {} va {}".format(i, math.floor(
            numb/i), uoc[i][0]+1, uoc[math.floor(numb/i)][0]+1))
    if int(i) == math.floor(math.sqrt(numb)) and len(uoc[i]) > 1:
        print("{} va {} o vi tri so {} va {}".format(
            i, math.floor(numb/i), uoc[i][0]+1, uoc[i][1]+1))
