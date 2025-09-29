# Predefined products
products = [
    {"id": 1, "name": "Laptop", "price": 45000},
    {"id": 2, "name": "Smartphone", "price": 15000},
    {"id": 3, "name": "Headphones", "price": 2000},
    {"id": 4, "name": "Keyboard", "price": 1200},
    {"id": 5, "name": "Mouse", "price": 800},
    {"id": 6, "name": "Charger", "price": 500},
    {"id": 7, "name": "USB Cable", "price": 300},
    {"id": 8, "name": "Backpack", "price": 2500},
]

# The cart — initially empty
cart = []

MAX_CART_ITEMS = 8

def view_products(products_list):
    print("\nAvailable Products:")
    print("{:<5} {:<20} {:<10}".format("ID", "Name", "Price (₹)"))
    for p in products_list:
        print("{:<5} {:<20} {:<10}".format(p["id"], p["name"], p["price"]))
    print()

def find_product(products_list, product_id):
    """Helper: return the product dict with given id, or None if not found."""
    for p in products_list:
        if p["id"] == product_id:
            return p
    return None

def find_in_cart(cart_list, product_id):
    """Helper: return the cart item dict if present (by id), else None."""
    for item in cart_list:
        if item["id"] == product_id:
            return item
    return None

def add_to_cart(products_list, cart_list, product_id, quantity):
    if len(cart_list) >= MAX_CART_ITEMS:
        print("Cart is full. You cannot add more than {} items.".format(MAX_CART_ITEMS))
        return

    product = find_product(products_list, product_id)
    if not product:
        print(" Product with ID {} does not exist.".format(product_id))
        return

    if quantity <= 0:
        print(" Quantity must be at least 1.")
        return

    cart_item = find_in_cart(cart_list, product_id)
    if cart_item:
        # If already in cart, just increase quantity
        cart_item["quantity"] += quantity
        print("Increased quantity of '{}' by {}.".format(product["name"], quantity))
    else:
        # New addition
        cart_list.append({
            "id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })
        print("Added '{}' (qty {}) to cart.".format(product["name"], quantity))

def view_cart(cart_list):
    if not cart_list:
        print("\n🛒 Your cart is empty.\n")
        return

    print("\nYour Cart:")
    print("{:<5} {:<20} {:<10} {:<10} {:<10}".format("ID", "Name", "Price (₹)", "Quantity", "Total (₹)"))
    grand_total = 0
    for item in cart_list:
        total = item["price"] * item["quantity"]
        grand_total += total
        print("{:<5} {:<20} {:<10} {:<10} {:<10}".format(
            item["id"], item["name"], item["price"], item["quantity"], total))
    print("Grand Total: ₹{}".format(grand_total))
    print()

def update_cart(cart_list, product_id, new_quantity):
    cart_item = find_in_cart(cart_list, product_id)
    if not cart_item:
        print(" Product with ID {} is not in the cart.".format(product_id))
        return
    if new_quantity <= 0:
        print(" Quantity must be at least 1. To remove, use Remove option.")
        return

    cart_item["quantity"] = new_quantity
    print("Updated quantity of '{}' to {}.".format(cart_item["name"], new_quantity))

def remove_from_cart(cart_list, product_id):
    cart_item = find_in_cart(cart_list, product_id)
    if not cart_item:
        print("Product with ID {} is not in the cart.".format(product_id))
        return

    cart_list.remove(cart_item)
    print(" Removed '{}' from the cart.".format(cart_item["name"]))

def checkout(cart_list):
    if not cart_list:
        print("\n Cart is empty. Nothing to checkout.\n")
        return

    print("\n===== Final Bill =====")
    view_cart(cart_list)
    print("Thank you for shopping with us!\n")

    # Empty the cart
    cart_list.clear()

def menu():
    while True:
        print("===== Shopping Cart =====")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Update Cart")
        print("5. Remove from Cart")
        print("6. Checkout")
        print("7. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_products(products)
        elif choice == "2":
            try:
                pid = int(input("Enter product ID to add: "))
                qty = int(input("Enter quantity: "))
                add_to_cart(products, cart, pid, qty)
            except ValueError:
                print("Invalid input. Please enter integer values.")
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            try:
                pid = int(input("Enter product ID to update: "))
                qty = int(input("Enter new quantity: "))
                update_cart(cart, pid, qty)
            except ValueError:
                print("Invalid input. Please enter integer values.")
        elif choice == "5":
            try:
                pid = int(input("Enter product ID to remove: "))
                remove_from_cart(cart, pid)
            except ValueError:
                print("Invalid input. Please enter integer values.")
        elif choice == "6":
            checkout(cart)
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print(" Invalid choice. Please choose between 1 and 7.")

if __name__ == "__main__":
    menu()
