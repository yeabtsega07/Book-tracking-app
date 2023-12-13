import mysql.connector
from model.book import Book

class BookRepository:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            user='root', 
            password='12345678',
            host='mysql',
            database='book'
            )
    
    def get_all(self):
        cursor = self.cnx.cursor()
        query = ("SELECT id, title, status FROM books")
        cursor.execute(query)
        return [{"id": book[0], "title": book[1], "status": book[2]} for book in cursor.fetchall()]

    def get(self, book_id):
        cursor = self.cnx.cursor()
        query = ("SELECT id, title, status FROM books WHERE id = %s")
        cursor.execute(query, (book_id,))
        book = cursor.fetchone()
        return {"id": book[0], "title": book[1], "status": book[2]} if book else None

    def create(self, book: Book):
        cursor = self.cnx.cursor()
        query = ("INSERT INTO books (title, status) VALUES (%s, %s)")
        cursor.execute(query, (book.title, book.status))
        self.cnx.commit()
        return {"id": cursor.lastrowid, "title": book.title, "status": book.status}

    
    def update(self, book_id: str, status: str):
        cursor = self.cnx.cursor()
        query = ("UPDATE books SET status = %s WHERE id = %s")
        cursor.execute(query, (status, book_id))
        self.cnx.commit()
        return {"message": "Book updated successfully"} if cursor.rowcount else None

    def delete(self, book_id):
        cursor = self.cnx.cursor()
        query = ("DELETE FROM books WHERE id = %s")
        cursor.execute(query, (book_id,))
        self.cnx.commit()
        return {"message": "Book deleted successfully"} if cursor.rowcount else None