import json
import os

def add_book():
    
    new_book = {
        
        "BookTitle" : input("Enter Book Title: "),
        "AuthorName" : input("Enter Book Author's Name: "),
        "BookId" : input("Enter Book ID: "),
        "Genre" : input("Enter Book Genre: ")
    }
    
    
    if os.path.exists("Data/Library.json"):
        
        with open("Data/Library.json", "r") as file:
            books = json.load(file)
    else:
        books = []


    books.append(new_book)
    
    with open("Data/Library.json", "w") as file:
        json.dump(books, file, indent=4)
        
    print("\n** Book added successfully!\n")


def view_all_books():
    
    if not os.path.exists("Data/Library.json"):
        print("\n** No book data found. File does not exist.\n")
        return
    
    
    with open("Data/Library.json", "r") as file:
        books = json.load(file)
        
    
    if len(books) == 0:
        print("\n** No books found.\n")
        return
    
    
    print("\n----> All Books <----\n")
    
    for index, book in enumerate(books, start = 1):
        print(f"- Book {index}: ")
        print(f"\tBook Title: {book["BookTitle"]}")
        print(f"\tAuthor Name: {book['AuthorName']}")
        print(f"\tBook ID: {book['BookId']}")
        print(f"\tGenre: {book['Genre']}")
        print("---------------------------------")
        
        
        
def delete_a_book():
    
    if not os.path.exists("Data/Library.json"):
        print("\n** No book data found. File does not exist.\n")
        return
    
    
    with open("Data/Library.json", "r") as file:
        books = json.load(file)
        
    
    if len(books) == 0:
        print("\n** No books found.\n")
        return
    
    
    
    while True:
    
        book_id_to_delete = input("Enter the Book ID of book to delete data: ")
        
        found = False
        
        for book in books:
            
            if book["BookId"] == book_id_to_delete:
                
                print("\n- Book Found:\n")
                print(f"\tBook Title: {book["BookTitle"]}")
                print(f"\tAuthor Name: {book['AuthorName']}")
                print(f"\tBook ID: {book['BookId']}")
                print(f"\tGenre: {book['Genre']}")
                
                choice3 = input("Do you want to delete data? (y/n): ").lower()
                
                if choice3 == "y":
                
                    books.remove(book)
                
                    with open("Data/Library.json", "w") as file:
                        json.dump(books, file, indent=4)
                    print("\n** Book data deleted successfully!\n")
                    return
                
                else:
                    print("\nDeletion Cancelled!\n")
                    return
                
                found = True
                break
                    
        if not found:
            print("\n** No book with such credentials found!\n")
        
        
        
def search_specific_book():
    
    if not os.path.exists("Data/Library.json"):
        print("\n** No book data found. File does not exist.\n")
        return
    
    
    with open("Data/Library.json", "r") as file:
        books = json.load(file)
        
    
    if len(books) == 0:
        print("\n** No books found.\n")
        return
    
    while True:
    
        book_id_to_search = input("Enter the Book ID of book to search data: ")
        
        found = False
        
        for book in books:
            
            if book["BookId"] == book_id_to_search:
                print("\n- Book Found:\n")
                print(f"\tBook Title: {book["BookTitle"]}")
                print(f"\tAuthor Name: {book['AuthorName']}")
                print(f"\tBook ID: {book['BookId']}")
                print(f"\tGenre: {book['Genre']}\n")
                
                found = True
                break
                
        if found:
            break
        
        else:
            print("\n** No book with such credentials found!\n")
            
            
            
def update_book_data():
    
    if not os.path.exists("Data/Library.json"):
        print("\n** No book data found. File does not exist.\n")
        return
    
    
    with open("Data/Library.json", "r") as file:
        books = json.load(file)
        
    
    if len(books) == 0:
        print("\n** No books found.\n")
        return
    
    
    while True:
    
        book_id_to_update = input("Enter the Book ID of book to update data: ")
        
        found = False
        
        for book in books: 
            
            if book["BookId"] == book_id_to_update:
                
                print("\n- Book Found:\n")
                print(f"\tBook Title: {book["BookTitle"]}")
                print(f"\tAuthor Name: {book['AuthorName']}")
                print(f"\tBook ID: {book['BookId']}")
                print(f"\tGenre: {book['Genre']}")
                print("------------------------------")
                
                print("\nEnter new data (Leave blank to keep current data):\n")
                
                BookTitle = input("Enter Book Title: ")
                AuthorName = input("Enter Author Name: ")
                Genre = input("Enter Genre: ")
                BookId = input("Enter Book ID: ")
                
                book.update({
                    "BookTitle": BookTitle if BookTitle else book["BookTitle"],
                    "AuthorName": AuthorName if AuthorName else book["AuthorName"],
                    "Genre": Genre if Genre else book["Genre"],
                    "BookId": BookId if BookId else book["BookId"]
                })
            
                print("\n* Book data updated successfully!\n")
                
                print(f"\tBook Title: {book["BookTitle"]}")
                print(f"\tAuthor Name: {book['AuthorName']}")
                print(f"\tBook ID: {book['BookId']}")
                print(f"\tGenre: {book['Genre']}\n")
                
                with open("Data/Library.json", "w") as file:
                    json.dump(books, file, indent=4)
                    
                found = True
                break
                
        if found:
            break
        
        else:
            print("\n** No book with such credentials found!\n")
            
            