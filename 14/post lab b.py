class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")

    def apply_discount(self, discount_percent):
        discount_amount = self.price * discount_percent / 100
        self.price -= discount_amount


# (a) Create two objects for different books and display their details
book1 = Book("1984", "George Orwell", 15.99)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 12.99)

print("Book 1 details:")
book1.display_details()
print("\nBook 2 details:")
book2.display_details()

# (b) Apply a 10% discount to one of the books and display the updated price
print("\nApplying 10% discount to Book 1...")
book1.apply_discount(10)

print("Updated Book 1 details:")
book1.display_details()


