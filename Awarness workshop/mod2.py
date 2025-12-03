# anjalii

def count_customers(data):
    male = 0
    female = 0
    for record in data:
        gender = record["CustomerGender"]
        if gender == "Male":
            male += 1
        elif gender == "Female":
            female += 1
    return male, female



