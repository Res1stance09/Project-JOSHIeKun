def calculate_products(items):
    subtotal = 0
    for item in items:
        subtotal += item['price'] * item['quantity']
    
    if subtotal > 100:
        discount = subtotal * .10
        subtotal -= discount
    
    tax = subtotal * 0.08
    final_total = subtotal + tax
    
    return round(final_total,2)

def cart_items():
    
    cart1 = [
        {"name": "Book", "price": 3.99, "quantity": 3},
        {"name": "Pencil", "price": 2.99, "quantity": 2} 
    ]
    
    cart2 = [
        {"name": "Blower", "price": 9.99, "quantity": 2},
        {"name": "Alcohol", "price": 8.99, "quantity": 3}
    ]
    
    print("Calculate the product without Tax")
    print(f"{calculate_products(cart1)}")
    
    print("Calculate the product With Tax")
    print(f"{calculate_products()}")


if __name__ == "__main__":
    cart_items()