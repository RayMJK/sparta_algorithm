shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


# O(N) + O(M) = O(N+M)
def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    menus_set = set(menus)  # O(N)
    for order in orders:  # m
        if order not in menus_set: # O(1)
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)