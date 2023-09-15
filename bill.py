def calculate_bill(units):
    if units <= 100:
        bill = 0
    elif units <= 300:
        bill = (units - 100) * 2
    else:
        bill = 200 * 2 + (units - 300) * 5
    return bill

units = int(input("Enter the number of electric units: "))

total_bill = calculate_bill(units)

print(f"Total bill for {units} units: Rs {total_bill}")
