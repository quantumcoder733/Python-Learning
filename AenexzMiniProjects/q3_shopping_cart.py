def create_cart(owner, discount=0):
    return {"owner": owner, "items": [], "discount": discount}


def add_to_cart(cart, name, price, qty=1):
    cart["items"].append({"name": name, "price": price, "qty": qty})


def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError as e:
        print(f"Error caught while updating tuple: {e}")


def calculate_total(cart):
    subtotal = sum(item["price"] * item["qty"] for item in cart["items"])
    discount_amount = subtotal * (cart["discount"] / 100)
    return subtotal - discount_amount


def display_cart(cart):
    print(f"--- Shopping Cart: {cart['owner']} ---")
    if not cart["items"]:
        print("Cart is empty.")
        return

    for item in cart["items"]:
        total_item = item["price"] * item["qty"]
        print(f"- {item['name']} x{item['qty']} @ ${item['price']:.2f} each = ${total_item:.2f}")

    subtotal = sum(item["price"] * item["qty"] for item in cart["items"])
    final_total = calculate_total(cart)
    
    print(f"Subtotal: ${subtotal:.2f}")
    if cart["discount"] > 0:
        print(f"Discount: {cart['discount']}%")
    print(f"Final Total: ${final_total:.2f}\n")


if __name__ == "__main__":
    alice_cart = create_cart("Alice", discount=10)
    add_to_cart(alice_cart, "Laptop", 999.99, qty=1)
    add_to_cart(alice_cart, "Mouse", 25.50, qty=2)

    bob_cart = create_cart("Bob")
    add_to_cart(bob_cart, "Headphones", 80.00, qty=1)

    display_cart(alice_cart)
    display_cart(bob_cart)

    sample_price = (100.0, "USD")
    print("Demonstrating tuple immutability:")
    update_price(sample_price, 120.0)