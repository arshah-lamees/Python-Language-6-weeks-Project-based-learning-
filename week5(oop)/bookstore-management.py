from datetime import datetime

class Book:
    def __init__(self, title, author, isbn, price, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.quantity = quantity
    
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity: {self.quantity}\n")

class Inventory:
    def __init__(self):
        self.books = {}
    
    def add_book(self, book):
        if book.isbn in self.books:
            print("Book already exists! Updating quantity instead.")
            self.books[book.isbn].quantity += book.quantity
        else:
            self.books[book.isbn] = book
            print(f"Book '{book.title}' added successfully!")
    
    def remove_book(self, isbn, quantity=1):
        if isbn in self.books:
            if self.books[isbn].quantity >= quantity:
                self.books[isbn].quantity -= quantity
                print(f"Removed {quantity} copies of '{self.books[isbn].title}'")
                if self.books[isbn].quantity == 0:
                    del self.books[isbn]
                return True
            else:
                print("Not enough stock to remove!")
        else:
            print("Book not found in inventory!")
        return False
    
    def check_stock(self, isbn):
        return self.books.get(isbn, None)
    
    def display_inventory(self):
        print("\nCurrent Inventory:")
        for book in self.books.values():
            book.display()

class Sales:
    def __init__(self):
        self.transactions = []
    
    def record_sale(self, book, quantity, total_price):
        self.transactions.append({
            'timestamp': datetime.now(),
            'book': book,
            'quantity': quantity,
            'total': total_price
        })
    
    def display_sales(self):
        print("\nSales History:")
        for transaction in self.transactions:
            print(f"{transaction['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Book: {transaction['book'].title}")
            print(f"ISBN: {transaction['book'].isbn}")
            print(f"Quantity: {transaction['quantity']}")
            print(f"Total: ${transaction['total']:.2f}\n")

def main():
    inventory = Inventory()
    sales = Sales()
    
    while True:
        print("\nBookstore Management System")
        print("1. Add new book")
        print("2. Sell book")
        print("3. Check stock")
        print("4. View sales history")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            try:
                title = input("Enter book title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
                
                new_book = Book(title, author, isbn, price, quantity)
                inventory.add_book(new_book)
            except ValueError:
                print("Invalid input! Please enter valid numbers for price and quantity.")
        
        elif choice == '2':
            isbn = input("Enter ISBN of book to sell: ")
            book = inventory.check_stock(isbn)
            if book!="":
                try:
                    quantity = int(input("Enter quantity to sell: "))
                    if quantity <= 0:
                        print("Invalid quantity!")
                    elif book.quantity >= quantity:
                        total = quantity * book.price
                        inventory.remove_book(isbn, quantity)
                        sales.record_sale(book, quantity, total)
                        print(f"Sale recorded! Total: ${total:.2f}")
                    else:
                        print("Not enough stock!")
                except ValueError:
                    print("Invalid quantity input!")
            else:
                print("Book not found in inventory!")
        
        elif choice == '3':
            isbn = input("Enter ISBN to check: ")
            book = inventory.check_stock(isbn)
            if book!="":
                book.display()
            else:
                print("Book not found in inventory!")
        
        elif choice == '4':
            sales.display_sales()
        
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

main()
