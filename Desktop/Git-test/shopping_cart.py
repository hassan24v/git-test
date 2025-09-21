#تمرین سبد خرید
basket = {
    "apple" : {"price" : 2, "no" : 3},
    "banana" : {"price" : 1, "no" : 5},
    "cherry" : {"price" : 3, "no" : 2}
}

#محاسبه مجموع فاکتور
total_bill = 0
for item in basket.values():
    total_bill += item["price"] * item["no"]

print(f"Total bill : {total_bill}")