# Menu and pricing dictionary
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

# Greeting and order process
def greet_customer():
    greeting = input("Waiter: Hello sir!\n").strip().lower()
    if greeting in ['hello', 'hi']:
        return True
    else:
        print("Waiter: Please say 'Hello' or 'Hi' to proceed.")
        return False

def ask_how_are_you():
    response = input("Waiter: How are you, sir?\n").lower()
    if response in ['good', 'fine', 'good thanks', "i'm good thanks"]:
        print("Waiter: Glad to hear that! 🥰💕\n")
    else:
        print("Waiter: I'm sorry to hear that.")
        
    
def confirm_order():
    response = input("Waiter: Would you like to proceed with this order? Yes or No\n").strip().lower()
    return response in ['yes', 'yeah', 'okay', 'ok']

def order_more():
  response = input("Waiter: Would you like to order anything else? Yes or No\n").strip().lower()
  return response in ['Yes', 'Yeah', 'Ok']
  

def ask_to_continue():
    response = input("Waiter: Would you like to order something else instead? Yes or No\n").strip().lower()
    return response in ['yes', 'yeah']


def get_quantity():
    while True:
        try:
            quantity = int(input("Waiter: How many would you like?\n"))
            return quantity
        except ValueError:
            print("Waiter: Please enter a valid quantity.")


def process_additional_order():
    while True:
        additional_order = input("Waiter: What else would you like to order?\n").strip().lower()
        if additional_order in menu:
            price = menu[additional_order]
            quantity = get_quantity()
            additional_cost = price * quantity
            print(f"Waiter: Your additional order for {quantity} {additional_order}(s) is ${additional_cost:.2f}.")
            return additional_cost
        else:
            print("Waiter: Sorry, that item is not available on our menu.")

            
def get_order():
    while True:
        print(f'This is our menu 😍\n', '--'*20)
        for name, price in menu.items():
        
            print(name.upper())
        order = input("Waiter: What would you like to order?\n").strip().lower()
        
        if order in menu:
            price = menu[order]
            print(f"Waiter: The price of {order} is ${price:.2f}.")
            
            if confirm_order():
                quantity = get_quantity()
                total_cost = price * quantity
                print(f"Waiter: Your total for {quantity} {order}(s) is ${total_cost:.2f}.")
                
                if order_more():
                    additional_cost = process_additional_order()
                    total_cost += additional_cost
                print(f"Waiter: Your final bill is ${total_cost:.2f}. Please wait while I prepare your order.")
                break
            else:
                if not ask_to_continue():
                    print("Waiter: Alright, have a nice day!")
                    break
        else:
            print("Waiter: Sorry, that item is not on our menu.")
          
     
# Main program
if greet_customer():
    ask_how_are_you()
    get_order()