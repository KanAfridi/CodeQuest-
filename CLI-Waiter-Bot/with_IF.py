
menu = {
    'tea': 3.5,
    'green tea': 2.3,
    'bread': 1.5,
    'milk': 3.0,
    'coffee': 1.4,
    'pizza': 10.0,
    'pasta': 12.0,
    'fried egg': 1.5,
    'steak': 20.0
}

greeting = input("Waiter: Hello sir!\n").lower()
valid_greetings = ['hello', 'hi']

if greeting in valid_greetings:
    customer_reply = input("Waiter: How are you, sir?\n").lower()
    
    if customer_reply in ['good', 'fine', 'good thanks', "i'm good thanks"]:
        print("Waiter: Glad to hear that! 🥰💕\n")
    else:
        print("Waiter: I'm sorry to hear that. 😔")
         
    while True:
        print("☕🍵🍔🍔")
        print("Waiter: So, what would you like to order?")
        for name, price in menu.items():
            print(name.upper())
        
        order = input().lower()
        if order in menu:
            price = menu[order]
            print(f"The price of {order} is ${price}.")
            customer_satisfaction = input("Waiter: Would you like to proceed with this order? Yes or No\n").lower()
            
            if customer_satisfaction in ['yes', 'yeah', 'okay', 'ok']:
                print("Waiter: How many would you like?")
                quantity = int(input())
                total_cost = price * quantity
                print(f"Waiter: Your total for {quantity} {order}(s) is ${total_cost:.2f}.")

                order_more = input("Waiter: Would you like to order anything else? Yes or No\n").lower()
                
                if order_more in ['yes', 'yeah']:
                    additional_order = input("Waiter: What else would you like to order?\n").lower()
                    
                    if additional_order in menu:
                        additional_quantity = int(input("Waiter: How many?\n"))
                        additional_price = menu[additional_order]
                        additional_total = additional_price * additional_quantity
                        
                        total_cost += additional_total
                        print(f"Waiter: Your order is {quantity} {order}(s) and {additional_quantity} {additional_order}(s).")
                        print(f"Waiter: Your total bill is ${total_cost:.2f}. Please wait while I prepare your order.")
                        break 
                    else:
                        print("Waiter: Sorry, that item is not available on our menu.")
                        continue
                else:
                    print("Waiter: Thank you for your order! Please wait while I prepare it.")
                    break  # Exit the loop
            else:
                print("Waiter: Would you like to order something else instead?")
                continue_response = input("Waiter: Yes or No\n").lower()
                if continue_response not in ['yes', 'yeah']:
                    print("Alright sir, let me know if you need anything else. Have a nice day!")
                    break  
        else:
            print("Waiter: Sorry, that item is not on our menu.")
else:
    print("Waiter: Sorry, I didn't get that. Please say 'Hello' or 'Hi' to proceed.")

