import math
list1 = [1, 3, 4, 16, 32, 8, 64, 4, 128, 2, 256, 32]
list2 = [16, 2, 4, 2, 128, 64, 16, 7, 1, 64, 32, 16, 5, 8]


def tim_uoc_so(n, lst):
    a = 0
    n = math.floor(n)
    x = math.floor(math.sqrt(n))
    for i in range(1, x+1):
        if n % i == 0:
            a += 1
            lst['a{}'.format(a)] = [i, math.floor(n/i)]


def select_list(lst):
    for value in avail_ans.values():
        index1 = -1
        index2 = -1
        for i in range(len(lst)):
            if lst[i] == value[0] and index1 == -1:
                index1 = i
            elif lst[i] == value[1] and index2 == -1:
                index2 = i
        if index1 != -1 and index2 != -1:
            print("{} va {} o vi tri so {} va {}".format(
                value[0], value[1], index1+1, index2+1))


numb = int(input("So can tim uoc so la: "))
avail_ans = {}
tim_uoc_so(numb, avail_ans)
print("Cac cap so co tich bang 256 trong list 1 la: ")
select_list(list1)
print()
print("Cac cap so co tich bang 256 trong list 2 la: ")
select_list(list2)