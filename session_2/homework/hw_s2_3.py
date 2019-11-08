import math
list1 = [1, 3, 4, 16, 32, 8, 64, 4, 128, 2, 256, 32]
list2 = [16, 2, 4, 2, 128, 64, 16, 7, 1, 64, 32, 16, 5, 8]
used = []
numb = int(input("So can tim uoc so la: "))
print("Cac cap so co tich bang {} trong list 1 la: ".format(numb))
for i in range(len(list2)-1):
    for n in range(i+1, len(list2)):
        if list2[n] * list2[i] == numb:
            if list2[n] not in used and list2[i] not in used:
                used.append(list2[n])
                used.append(list2[i])
                print("{} va {} o vi tri so {} va {}".format(
                    list2[i], list2[n], i+1, n+1))
