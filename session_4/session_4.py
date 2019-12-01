'''def greatest_division(a,b):
    if a == b:
        return a
    elif a>b:
        a = a-b
        return greatest_division(a,b)
    else:
        b = b - a
        return greatest_division(a,b)
print(greatest_division(8,6))
'''
import math
# NOTE : MERGE SORT


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    else:

        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]
        m_left = merge_sort(left)
        m_right = merge_sort(right)
        loop = True
        i = 0
        j = 0
        new_lst = []
        while loop:
            if m_left[i] > m_right[j]:
                new_lst.append(m_right[j])
                j += 1
                if j == len(m_right):
                    loop = False
                    new_lst += m_left[i:]
            else:
                new_lst.append(m_left[i])
                i += 1
                if i == len(m_left):
                    loop = False
                    new_lst += m_right[j:]
        return new_lst


h = [3, 7, 4, 2, 34324, 44, 433, 3434, 5]
print(merge_sort(h))


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


print(quick_sort(h))
