def count_substr(input_str):
    if len(input_str) == 0:
        return 0
    else:
        valid_substring = count_substr(
            input_str[1:]) + count_substr(input_str[:1]) - count_substr(input_str[1:-1])
        if input_str[0] == input_str[-1]:
            valid_substring += 1
        return valid_substring


def can_keo_can_ke(money, price, ex_wrap):
    if ex_wrap <= 1:
        return 'Vo so keo'
    else:
        candies = money // price
        sp_wraps = candies
        candies += doi_keo_doi_ke(ex_wrap, sp_wraps)
        return candies


def doi_keo_doi_ke(ex_wrap, sp_wraps):
    if sp_wraps < ex_wrap:
        return 0
    else:
        ex_candies = sp_wraps // ex_wrap
        sp_wraps = ex_candies + sp_wraps % ex_wrap
        ex_candies += doi_keo_doi_ke(ex_wrap, sp_wraps)
        return ex_candies


print(can_keo_can_ke(20, 3, 5))

# Solution:
def count_candy(candy, wrap):
    if (candy<wrap):
        return 0
    new_candy = candy //wrap
    return new_candy + count_candy(new_candy + candy % wrap, wrap)

def count_max_candy(money,price,wrap):
    candy = money // price
    return candy + count_candy(candy, wrap)

print(count_max_candy(16,2,3))