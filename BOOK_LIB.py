print('**~~~~BAngladesh Library~~~~**')
print('')

global Booklist
booklist = []

def Show_book():
    print('Avalable Books:')
    for book in booklist:
        print(book)

def Borrow_book(book):
    if book in booklist:
        print(f'{book} is avalable. Thank you for purchasing ')
        booklist.remove(book)
    else:
        print('Sorry! That book is not avalabe!') 

def Return_book(book):
    if book not in booklist:
        print(f'Thank you for returning the {book}')
        booklist.append(book)
    else:
        print('That book is already Returned!')

def Add_book(book):
    booklist.append(book)
    print('Thank you for your donation')
    print(f'Your {book} is added to the library')

Show_book()
Add_book('Rokto Kobori')
Add_book('Shanchaita')
Add_book('Ami Dalim bolchi')
Add_book('Siraj-ud-Daulah')
Add_book('Tajkerat-ul-Awlia')
Add_book('Dosshi Kojon')
Add_book('Life of Pi')
Add_book('Ikigai')
Add_book('The Kite Runner')
Add_book('Feluda Samagra 1')
Add_book('Feluda Samagra 2')
Show_book()
Borrow_book('Shanchaita')
Show_book()
Return_book('Shanchaita')
Show_book()


