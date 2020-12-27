shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "떡볶이", "만두"]


def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    for i in orders:
        if i not in menus:
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)