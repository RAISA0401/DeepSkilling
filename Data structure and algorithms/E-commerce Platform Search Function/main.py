from product import Product
from search_algorithms import linear_search, binary_search

products = [
    Product(105, "Laptop", "Electronics"),
    Product(102, "Shoes", "Fashion"),
    Product(108, "Watch", "Accessories"),
    Product(101, "Phone", "Electronics"),
    Product(110, "Bag", "Fashion")
]

sorted_products = sorted(products, key=lambda x: x.product_id)

target = 108

print("Linear Search")
result = linear_search(products, target)

if result:
    print(result)
else:
    print("Product not found")

print("\nBinary Search")
result = binary_search(sorted_products, target)

if result:
    print(result)
else:
    print("Product not found")