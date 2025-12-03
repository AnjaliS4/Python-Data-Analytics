#anjali 
def calculate_total_sales(data):
    total = 0
    for record in data:
        total += record["UnitsSold"] * record["UnitPrice"]
    return total

def calculate_average_sale(data):
    total = calculate_total_sales(data)
    return total / len(data)

def most_popular_category(data):
    category_count = {}
    for record in data:
        cat = record["ProductCategory"]
        category_count[cat] = category_count.get(cat, 0) + 1
    return max(category_count, key=category_count.get)



