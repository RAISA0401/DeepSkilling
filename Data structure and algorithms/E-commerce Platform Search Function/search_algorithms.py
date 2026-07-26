def linear_search(products, target_id):
    for product in products:
        if product.product_id == target_id:
            return product
    return None


def binary_search(products, target_id):
    low = 0
    high = len(products) - 1

    while low <= high:
        mid = (low + high) // 2

        if products[mid].product_id == target_id:
            return products[mid]
        elif products[mid].product_id < target_id:
            low = mid + 1
        else:
            high = mid - 1

    return None