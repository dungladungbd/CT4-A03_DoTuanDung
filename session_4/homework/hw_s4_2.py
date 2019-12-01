# Ex2:
def buy_candy(money, price, wr_ex_cost,spare_wr):
    if wr_ex_cost <= 1 :
        return "Infinity candies"
    else:
        candies = money // price
        spare_wr += candies % wr_ex_cost
        if spare_wr == 0:
            return candies
        else:
            money = (candies//wr_ex_cost) * price + (spare_wr - candies%wr_ex_cost) * price
            candies += buy_candy(money,price,wr_ex_cost,spare_wr)
            return candies



print(buy_candy(16,2,3,0))