import datetime
import os
os.getcwd()

class LMS:
    """
    This class is used to keep records of books library.
    It has total four modules: 'Display Books', 'Lend Books', 'Add Books', 'Return Books'
    'list_of_books' should be txt file. 'library_name' should be string.
    """

    def __init__(self, list_of_books, library_name):
        self.list_of_books = "list_of_books.txt"  # we must create text file name== "list_of_books.txt"  first
        self.library_name = library_name
        self.books_dict = {}
        id = 1  # here id start from 101
        with open(self.list_of_books) as b:
            content = b.readlines()
        for line in content:
            self.books_dict.update({str(id):{'books_title':line.replace("\n",""),'lender_name':'','lend_date':'', 'status':'Available'}})
            id += 1    

    def display_books(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~List of Books in library ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Books ID","\t", "Title")
        print("               ")
        for key, value in self.books_dict.items():
            print(key,"\t\t", value.get("books_title"), "- [", value.get("status"),"]")
                                                                    #   keys values-status
    def Issue_books(self):
        books_id = input("Enter Books ID : ")    #we issue book based on id
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['status'] == 'Available':
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} on {self.books_dict[books_id]['lend_date']}")
               # return self.Issue_books() can create problem
            elif self.books_dict[books_id]['status'] == 'Available':
                your_name = input("Enter Your Name : ")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['lend_date'] = current_date
                self.books_dict[books_id]['status']= 'Already Issued'
                print("Book Issued Successfully !!!\n")
        else:
            print("Book ID Not Found !!!")
            return self.Issue_books()

    def add_books(self):
        new_books = input("Enter Books Title : ")
        if new_books == "":
            return self.add_books()
        elif len(new_books) > 20:
            print("Books title length is too long, please enter title within 20 character!")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as b:
                b.writelines(f"{new_books}\n")
            self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':'','lend_date':'', 'status':'Available'}})
            print(f"******************* congratulation ! The books '{new_books}' has been added successfully****************** ")

    def return_books(self):
        books_id = input("Enter Books ID : ")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['status'] == 'Available':
                print("This book is already available in library. Please check book id. !!! ")
                return self.return_books()
            elif not self.books_dict[books_id]['status'] == 'Available':
                self.books_dict[books_id]['lender_name'] = ''
                self.books_dict[books_id]['lend_date'] = ''
                self.books_dict[books_id]['status']= 'Available'
                print("Successfully Updated !!!\n")
                print("Thanks for returning this book! Hope you enjoy by reading it. Have a great day ahead!")
        else:
            print("Book ID Not Found !!!")

if __name__ == "__main__":
    try:
        mylms = LMS("list_of_books.txt","manager*")
        press_key_list = {"D": "Display a Books", "I": "Issue a Books", "A": "Adding Books to library", "R": "Return Books to library", "Q": "Quit the library"}    
        
        key_press = False
        while not (key_press == "q"):
            print(f"\n *************** Welcome to Willam W.Cook Legal Library ,Ann Arbor,Michigan **************\n")
            for key, value in press_key_list.items():
                print("Press", key, "To", value)
            key_press = input("Press Key : ").lower()   #making alphabet in lower case when user input is in uppercase
            if key_press == "i":
                print("\n~~~~~~~~~~~ ISSUE a BOOK ~~~~~~~~~~~~~~~\n")
                mylms.Issue_books()
                
            elif key_press == "a":
                print("\n******************** Adding a Books *****************\n")
                mylms.add_books()

            elif key_press == "d":
                print("\n----------------------------->>>> Display a books <<<<-------------------------------\n")
                mylms.display_books()
            
            elif key_press == "r":
                print("\n***********************======>> RETURN BOOK <<==========***************************\n")
                mylms.return_books()
            elif key_press == "q":
                 print("\n   ~~~~~~~~~~  Thanks for choosing ! Willam W.Cook Legal Library  ~~~~~~~~~~~~~~")
                 break
            else:
                continue
    except Exception as e:
        print("Something went wrong........", e)