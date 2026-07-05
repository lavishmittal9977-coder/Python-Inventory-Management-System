product=("Laptop","Mobile","Tv","Refridgerator")
quantity=(10,15,20,8)
price=(50000,20000,25000,30000)
product_cart=[]
quantity_cart=[]
price_cart=[]
cart_total=[]
while True:
    print("*******INVENTORY MANAGEMENT*******")
    print("press 1 to show Products")
    print("press 2 to buy product")
    print("press 3 to show cart")
    print("press 4 to exit")
    print("-"*40)
    
    ch=int(input("Enter your choice:"))
    match ch:
        case 1:
            print(f"{'product':<20}{'price':<15}{'quantity':<10}")
            for i in range(len(product)):
                print(f"{product[i]:<20}{price[i]:<15}{quantity[i]:<10}")
        case 2:
            pname=input("Enter the name of product:").title()
            qnty=int(input("Enter the quantity:"))
            if pname in product:
               index=product.index(pname)
               if  qnty>0 and qnty<=quantity[index] :
                   temp=list(quantity)
                   temp[index]-=qnty
                   quantity=tuple(temp)
                   total=qnty*price[index]
                                  
                   if product[index] in product_cart:
                        cart_index=product_cart.index(product[index])
                        quantity_cart[cart_index]+=qnty
                        cart_total[cart_index]=quantity_cart[cart_index]*price_cart[cart_index]
                   else:
                        product_cart.append(product[index])
                        quantity_cart.append(qnty)
                        price_cart.append(price[index])
                        cart_total.append(total)
                        print("product Added  to cart Successfully!")
               else:
                   print("Insufficient Stock")
            else:
                print("Product not found")
        case 3:
            print("******YOUR  SHOPPING CART******")
            print(f"{'Product':<20}{'Price':<15}{'Quantity':<10}{'Total':<10}")
            for i in  range(len(product_cart)):
                print(f"{product_cart[i]:<20}{price_cart[i]:<15}{quantity_cart[i]:<10}{cart_total[i]:<10}")
            print("Grand total",sum(cart_total))
        case 4:
            print("Thank you for shopping with us!")
            break
        case _:
            print("Invalid choice")
