
menu = {
    'pizza': 10.0,
    'tea': 3.5,
    'bread': 1.5,
    'milk': 3.0,
    'coffee': 1.4
}

greeting = input("Waiter: Hello sir!\n").lower()
valid_greetings = ['hello', 'hi']

if greeting in valid_greetings:
    customer_reply = input("Waiter: How are you, sir?\n").lower()
    
    if customer_reply in ['good', 'fine', 'good thanks', "i'm good thanks"]:
        print("Waiter: Glad to hear that!")
    else:
        print("Waiter: I'm sorry to hear that. 😔")
         
    while True:
        print("Waiter: So, what would you like to order?")
        
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
                        break  # Exit the loop after confirming the additional order
                    else:
                        print("Waiter: Sorry, that item is not available on our menu.")
                        continue
                else:
                    print("Waiter: Thank you for your order! Please wait while I prepare it.")
                    break  # Exit the loop after confirming no additional items
            else:
                print("Waiter: Would you like to order something else instead?")
                continue_response = input("Waiter: Yes or No\n").lower()
                if continue_response not in ['yes', 'yeah']:
                    print("Alright sir, let me know if you need anything else. Have a nice day!")
                    break  # Exit the loop if the customer doesn't want anything else
        else:
            print("Waiter: Sorry, that item is not on our menu.")
else:
    print("Waiter: Sorry, I didn't get that. Please say 'Hello' or 'Hi' to proceed.")







'''
menu = {
    'pizza': 10.0,
    'tea': 3.5,
    'bread': 1.5,
    'milk': 3.0,
    'coffee': 1.4
}


greet = input('Waiter: Hello sir!\n').lower()

ans = ['Hello', 'hi']
answer = [word.lower() for word in ans]

if greet in answer:
    customer_reply = input('Waiter: How are you sir?\n')
    
    if customer_reply.lower() in ['good', 'fine', 'good thanks', "i'm good thanks"]:
        print('Waiter: Glad to hear that')
    else:
        print('Waiter: I\'m sorry to hear that. 😔') 
         
    while True:
        print('Waiter: So What would you like to order?')

        order = input().lower()
        if order in menu:
            price = menu[order]
            #price_ask = input('Waiter: should i bring your order\n') 
            print(f"The price of {order} is ${price}.")
            customer_satisfiction = input('Waiter: Would you like to proceed with this order? Yes or No\n')            
            
            if customer_satisfiction.lower() in ['yes', 'yeah', 'okay', 'ok']:
                print("waiter: how much?")
                quantity = input()
                total = price * int(quantity)
                print(f"Waiter: okay sir Your total bill is ${total}.")
                order_extra = input("Anything else you want to order Yes or No?\n")
                
                if order_extra == 'yes' and order_extra in menu:
                    second_order = input("what do you want to order more?\n")
                    second_order_quantity = input("how much?")
                    second_order_total = second_order_quantity[menu] * second_order
                    Total_cost = second_order_quantity * second_order[menu]
                    
                    total_cost = second_order_total + total
                    print(f"Waiter: okay sir {price} of {quantity} {order} and {second_order_quantity} of {second_order} {second_order_total} Your total bill is ${total_cost}.")
                    
                    print('Waiter: please wait')
                    break
            else:
                print('Waiter: would you like to order something else instead?')
                continue_response = input('Waiter:... yes or no\n').lower()
                if continue_response not in ['yes', 'yeah']:
                    print("Alright sir, let me know if you need anything else. Have a nice day!")
        else:
            ask_again = input('Waiter: it is not in our menu sorry sir')     
else:
    print('Waiter: Sorry, I didn\'t get that. Please say "Hello" or "Hi" to proceed. \nPlease be respectful.')
    '''