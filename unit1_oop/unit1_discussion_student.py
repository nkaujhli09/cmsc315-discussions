"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class BakeryCustomer:
    # Class variable shared by all bakery customers
    bakery_name = "The Sweet Spot"

    def __init__(self, customer_id, name):
        # Two instance variables
        self.customer_id = customer_id
        self.name = name

    def get_summary(self):
        """Displays information about the customer."""
        return f"ID: {self.customer_id} | Name: {self.name} | Shop: {self.bakery_name}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class PremiumCustomer(BakeryCustomer):
    # New class variable
    discount_rate = 0.15

    def __init__(self, customer_id, name, items_ordered, order_details):
        # Call the parent constructor
        super().__init__(customer_id, name)
        # Two new instance variables (items_ordered is a list, order_details is a dict)
        self.items_ordered = items_ordered
        self.order_details = order_details

    def calculate_savings(self, subtotal):
        """New method unique to PremiumCustomer."""
        savings = subtotal * self.discount_rate
        return f"{self.name} saves ${savings:.2f} on this order!"

    def get_summary(self):
        """Overrides the parent class method."""
        parent_info = super().get_summary()
        status = self.order_details.get("status", "Unknown")
        return f"{parent_info} | VIP Discount: {self.discount_rate * 100}% | Order Status: {status}"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Bakery Namespace Demonstration ===")
    
    # Create two premium customer objects
    cust1 = PremiumCustomer("VIP001", "Alice", ["Croissant", "Eclair"], {"status": "Pending"})
    cust2 = PremiumCustomer("VIP002", "Bob", ["Sourdough"], {"status": "Completed"})
    
    # Access a class variable through the class itself and through an object
    print(f"Class variable via Class: {PremiumCustomer.discount_rate}")
    print(f"Class variable via Object: {cust1.discount_rate}")
    
    # Add a new attribute to only one object after it is created
    cust1.favorite_pastry = "Almond Croissant"
    print(f"\nAdded 'favorite_pastry' attribute exclusively to {cust1.name}.")
    
    # Display each object's namespace using __dict__
    print(f"\n{cust1.name}'s Namespace (__dict__):")
    print(cust1.__dict__)
    
    print(f"\n{cust2.name}'s Namespace (__dict__):")
    print(cust2.__dict__)
    
    # Display information about the class namespace
    print("\nPremiumCustomer Class Namespace (Keys only):")
    print([key for key in PremiumCustomer.__dict__.keys() if not key.startswith('__')])


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Bakery Copying Demonstration ===")
    
    # Create an original customer with nested mutable data (basket items and status dictionary)
    original_order = PremiumCustomer("VIP003", "Charlie", ["Cupcake", "Tart"], {"status": "Processing"})
    
    # Create a shallow copy and a deep copy
    shallow_order = copy(original_order)
    deep_order = deepcopy(original_order)
    
    # Modify the original object's nested mutable data and top-level primitives
    original_order.name = "Charles"                           # Primitive string
    original_order.items_ordered.append("Macaron")            # Nested list
    original_order.order_details["status"] = "Dispatched"     # Nested dict
    
    # Display the results to show the difference
    print("After modifying Charlie's original order:")
    print(f"Original: {original_order.get_summary()} | Basket: {original_order.items_ordered}")
    print(f"Shallow : {shallow_order.get_summary()} | Basket: {shallow_order.items_ordered}")
    print(f"Deep    : {deep_order.get_summary()} | Basket: {deep_order.items_ordered}")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.
def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n[Testing Parent Object]")
    # Create at least one object from the parent class
    regular_customer = BakeryCustomer("REG101", "John Doe")
    # Demonstrate calling its summary method
    print(regular_customer.get_summary())

    print("\n[Testing Child Object]")
    # Create at least one object from the child class
    premium_customer = PremiumCustomer("VIP777", "Jane Smith", ["Baguette", "Muffin"], {"status": "Baking"})
    # Demonstrate inheritance and polymorphism by calling the overridden summary method
    print(premium_customer.get_summary())
    # Call the child's specialized method
    print(premium_customer.calculate_savings(45.00))

    # Call your namespace demonstration function
    demonstrate_namespaces()
    
    # Call your copy demonstration function
    demonstrate_copying()


if __name__ == "__main__":
    main()
