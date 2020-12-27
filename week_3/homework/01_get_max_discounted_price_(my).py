shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]



def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    prices.sort()
    prices.reverse()
    # [1500000, 30000, 2000]
    coupons.sort()
    coupons.reverse()
    # [40, 20]
    sum = 0
    i=0
    while i < len(coupons):
        sum += ((100-coupons[i])/100)*prices[i]
        i+=1
    while i < len(prices):
        sum += prices[i]
        i +=1
    return sum


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.