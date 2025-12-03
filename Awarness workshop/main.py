from mod1 import check_sales
from mod2 import count_customers
from mod3 import calculate_total_sales, calculate_average_sale, most_popular_category
from mod4 import read_sales_file
def main():
    data = read_sales_file("sales_data.csv")

    print("\n--- SALES ANALYSIS REPORT ---\n")

    # Customer count
    male, female = count_customers(data)
    print("Male Customers:", male)
    print("Female Customers:", female)

    # Total and average sales
    total_sales = calculate_total_sales(data)
    avg_sale = calculate_average_sale(data)
    print("Total Sales Amount: $", round(total_sales, 2))
    print("Average Sale Amount: $", round(avg_sale, 2))

    # Popular category
    popular = most_popular_category(data)
    print("Most Popular Product Category:", popular)

    # High/Low sale check for each record
    print("\nSale Category per Transaction:")
    for rec in data:
        amount = rec["UnitsSold"] * rec["UnitPrice"]
        print(rec["SaleID"], "-", check_sales(amount))

if __name__ == "__main__":
    main()
