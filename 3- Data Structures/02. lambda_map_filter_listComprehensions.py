products = [('laptop', 999), ('pc', 1000), ('mobile', 299)]

#  Map Function

# prices = []

# for product in products:
#     prices.append(product[1])

# print(prices)

prices = list(map(lambda product: product[1], products))
print(prices)

#  Filter
filteredProducts = list(filter(lambda item: item[1] > 900, products))
print(filteredProducts)

#  List Comprehensions
print("====== List Comprehensions =====")

c_price = [product[1] for product in products]
print(c_price)

c_filteredProducts = [product for product in products if product[1] > 900]
print(c_filteredProducts)
