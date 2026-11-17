#customers information
customer_name = "drago"
product_name = "laptop"

#product information
price = 250000.00
quantity = 3
delivery_fee = 5000.00

#membership information
is_member = False

#calculate the total
total = price * quantity

#apply 10% discpunt to memebers
if is_member:
    discount = total * 0.10
else: 
    discount =0

# calculate final payment
final_total = total - discount + delivery_fee

#display reciept
print("==== shopping receipt====")
print(f"customer: {customer_name}")
print(f"product:{product_name}")
print(f"price: #{price}")
print(f"quantity:{quantity}")
print(f"is_member:{is_member}")
print(f"total: #{total}")
print(f"discount: #{discount}")
print(f"final payment: #{final_total}")
