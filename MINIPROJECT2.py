# supermarket bill generation system

print("----------welcome to pythonlife's SuperMarket----------")
print("-----------------------hyderabad ----------------------")
name = input("Enter your name: ")
mobilenumber = int(input("enter your mobile number : "))
address = input("enter your address for any delivery: ")

list = '''
mango     Rs 100/kg
water     Rs 20/bottle
sugar     Rs  40/Kg
panner    Rs  100/packet
maggi     Rs  12/packet
millets   Rs  50/Kg
icecream  Rs  45/piece
'''

items = {'mango': '100', 'water': '20', 'sugar': '40', 'panner': '100', 'maggi': '12', 'millets': '50','icecream': '45'}

price = 0
pricelist = []
itemlist = []
final_price = 0
total_price = 0

while True:
    option1 = int(input("Press 1 for the list or 2 to exit: "))
    
    if option1 == 1:
        print(list)
        while True:
            option2 = int(input("Press 1 to buy or 2 to exit: "))
            
            if option2 == 1:
                item = input("Enter the item: ").lower()
                if item in items:
                    itemlist.append(item)
                    quantity_input = input("Enter the quantity: ")
                    
                    if quantity_input.isdigit():
                        quantity = int(quantity_input)
                        price = quantity * int(items[item])
                        pricelist.append((item, quantity, items[item], price))
                        total_price += price
                    else:
                        print("Please enter a number.")
                else:
                    print("Please enter the right item.")
            
            elif option2 == 2:
                if itemlist:
                    print("\nThank you for choosing us.")
                    print("============pythonlife's Super Market ============")
                    print("------------------ Hyderabad ----------------")
                    print(f"Name: {name}")
                    print(f"mobilenumber : {mobilenumber}")
                    print(f"adress : {address}")
                    print("S.No. Items Quantity  Price")
                    
                    for i in range(len(pricelist)):
                        item, quantity, rate, price = pricelist[i]
                        print(f"{i+1} {item} {quantity}  Rs {price}")
                    
                    discount = total_price * 0.05
                    final_price = total_price - discount
                    print(f"Total:    Rs {total_price}")
                    print(f"Final Price:     Rs {final_price:.2f}")
                    print("---------- Thanks for shopping with us! ----------")
                else:
                    print("Thank you for choosing us. See you again!")
                exit()

            else:
                print("Please enter the right option.")

    elif option1 == 2:
        if itemlist:
            print("\nThank you for choosing us. Please find the final bill")
            print("============ pythonlife's Super Market ============")
            print("------------------ Hyderabad ----------------")
            print(f"Name: {name}")
            print("S.No.  Items  Quantity Price")
            
            for i in range(len(pricelist)):
                item, quantity, rate, price = pricelist[i]
                print(f"{i+1} {item}  {quantity}  Rs {price}")
            
            discount = total_price * 0.05
            final_price = total_price - discount
            print(f"\nTotal:       Rs {total_price}")
            print(f"Final Price:    Rs {final_price:.2f}")
            print("---------- Thanks for shopping with us! ----------")
        else:
            print("Thank you for choosing us. See you again!")
        exit()

    else:
        print("Wrong option, Kindly choose the right option.")
