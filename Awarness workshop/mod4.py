# anjalii 
def read_sales_file(filename):
    sales_records = []
    try:
        with open(filename, "r") as file:
            header = file.readline()   # <-- Skip header row

            for line in file:
                parts = line.strip().split(",")

                # SKIP empty lines
                if len(parts) < 7:
                    continue

                sales_records.append({
                    "SaleID": int(parts[0]),
                    "Date": parts[1],
                    "CustomerName": parts[2],
                    "CustomerGender": parts[3],
                    "ProductCategory": parts[4],
                    "UnitsSold": int(parts[5]),
                    "UnitPrice": float(parts[6])
                })
        return sales_records

    except FileNotFoundError:
        print("File not found.")
        return []


