from fastapi import Body,FastAPI

app = FastAPI()

BOOKS = [
    {'title':'Title One','author':'Author One','category':'science'},
    {'title':'Title Two','author':'Author Two','category':'science'},
    {'title':'Title Three','author':'Author Three','category':'maths'},
    {'title':'Title Four','author':'Author Four','category':'social'},
    {'title':'Title Five','author':'Author Five','category':'social'},
    {'title':'Title Six','author':'Author Five','category':'maths'},

]

@app.get('/books')
async def get_books():
    return BOOKS

@app.get('/books/{book_title}')
async def get_books(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
        
@app.get('/books/')
async def get_category_books(category:str):
    books_to_return=[]
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post('/books/create_book')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return new_book

@app.put('/books/update_book')
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i] =update_book

@app.delete('/books/delete_book/{title}')
async def delete_book(title:str):
    for i in range(len(BOOKS)):
            if BOOKS[i].get('title').casefold() == title.casefold():
                BOOKS.pop(i)
                break
    return BOOKS

@app.get('/books/list_author_books/{author}')
async def list_author_books(author:str):
    author_book_list=[]
    for i in range(len(BOOKS)):
        if BOOKS[i].get('author').casefold() == author.casefold():
            author_book_list.append(BOOKS[i])
    return author_book_list