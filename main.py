from products import Product
from store import Store

# bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
# mac = Product("MacBook Air M2", price=1450, quantity=100)
#
# best_buy = Store([bose, mac])
#
# pixel = Product("Google Pixel 7", price=500, quantity=250)
# best_buy.add_product(pixel)

# print(best_buy.products[2].quantity)
# best_buy.remove_product(pixel)
# print(best_buy.get_total_quantity())
# print(best_buy.get_all_products())

# res = best_buy.order([(bose, 5), (mac, 30), (pixel, 10)])
# if res is not None:
#     print(res)

def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(product_list[0], 1), (product_list[1], 2)]))



if __name__ == '__main__':
    main()