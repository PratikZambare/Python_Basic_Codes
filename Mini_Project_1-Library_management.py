class library :
    def __init__(self , lst , name):
        self.booklist = lst
        self.name = name
        self.lendict = {}

    def display_book(self):
        print(f'we have follwing books is in our library : {self.name}')
        for book in self.booklist :
            print(book)

    def lend_users(self):
        print(f'The book and the user names is {self.lendict}')

    def len_book(self , user ,book):
        if book not in self.lendict:
            self.lendict.update({book : user})
            print('Lender-Book database has been updated, You can take book now')
        else :
            print(f'Book is alredy being used by {self.lendict[book]}')

    def add_book(self , book):
        self.booklist.append(book)
        print("book has been added to the book-list")

    def return_book(self , book):
        self.lendict.pop(book)
if __name__ == '__main__':
    pratik = library(['Python', 'Rich daddy poor daddy','Harry potter', 'C++-Basics',
                      'Algorithms by CLRS'], 'Ooo Yhh')

    while(True) :
        print(f'Welcome to the {pratik.name} library . \nEnter your choice to continue')
        print('1. Display books')
        print('2. Lend a book')
        print('3. Add a book')
        print('4. return a book')
        print('5. lenders list')
        user_choice = (input())

        if user_choice not in ['1','2','3','4','5']:
            print('Please enter a valid input : ')
            continue

        else :
            user_choice = int(user_choice)

        if user_choice == 1:
            pratik.display_book()

        elif user_choice == 2:
            book = input("Enter the name of the book you want a lend : ")
            user = input("Enter your name : ")
            pratik.len_book(user , book)

        elif user_choice == 3:
            book = input("Enter tha name of the book you want to add : ")
            pratik.add_book(book)

        elif user_choice == 4:
            book = input("Enter tha name of the book you want to return : ")
            pratik.return_book(book)

        elif user_choice == 5 :
            pratik.lend_users()

        else:
            print('Not a valid option')

        print('Press q to quit and c to continue')
        user_choice2 = ""
        while(user_choice2!='c'and user_choice2 != 'q') :
            user_choice2 = input()
            if user_choice2 == 'q':
                exit()
            elif user_choice2 == 'c':
                continue