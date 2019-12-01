
# Ex 1:


def quick_sort(lst):
    if len(lst) == 1 or len(lst) == 0:
        return lst
    else:
        a = 0
        b = len(lst)
        i = -1
        for _ in range(len(lst)-1):
            pivot = lst[a]
            b += i
            if (lst[b] < pivot and a < b) or (lst[b] > pivot and a > b):
                lst[a], lst[b] = lst[b], lst[a]
                a, b = b, a
                i = i * -1
        left = lst[:a]
        mid = [lst[a]]
        right = lst[(a+1):]
        q_left = quick_sort(left)
        q_right = quick_sort(right)
        lst = q_left + mid + q_right
        return lst


test_lst = [34, 4, 6, 53, 45, 7, 5, 3, 10]
print(quick_sort(test_lst))

# Ex 2:


def first_upper1(strr):
    for i in range(len(strr)):
        if strr[i].islower() == False:
            return strr[i]


def first_upper2(strr):
    if len(strr) == 0:
        return "No capital letter"
    else:
        if strr[0].isupper():
            return strr[0]
        else:
            return first_upper2(strr[1:])


print(first_upper1("asdfceDafasdF"))
print(first_upper2("asdfceDafasdF"))

# Ex 3:


def sub_str(strr):
    if len(strr) == 0:
        return 0
    else:
        sub_count = 0
        for i in strr:
            if strr[0] == i:
                sub_count += 1
        return sub_count + sub_str(strr[1:])


print(sub_str("abcab"))
