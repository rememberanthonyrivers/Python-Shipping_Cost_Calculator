international_shipping = True 

total = 150     #this line represents the total cost of the order 
shipping_cost = 0   #this line creates a counter variable to work with 

if international_shipping:
    shipping_cost += 15 
    print("International base cost applied")

if total <= 50:
    shipping_cost += 20
elif total <= 100:
    shipping_cost += 15 
else: 
    shipping_cost += 5 

print(f"Shipping cost: {shipping_cost}")