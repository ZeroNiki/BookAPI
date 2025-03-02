from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from fastapi import APIRouter, Depends, HTTPException
from src.database import get_db
from src.operations.models import Book, BookCreate, BookUpdate

router = APIRouter(prefix="/books", tags=["Books API"])


@router.get("/")
async def get_all_books(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Book))
    return result.scalars().all()


@router.post("/")
async def add_book(book: BookCreate, db: AsyncSession = Depends(get_db)):
    new_book = Book(title=book.title, author=book.author, year=book.year)
    db.add(new_book)
    await db.commit()
    return {"Message": "Book added!", "id": new_book.id}


@router.get("/{book_id}")
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    query = select(Book).where(Book.id == book_id)
    book = await db.execute(query)
    return book.scalar_one_or_none()


@router.put("/{book_id}")
async def update_book(
    book_id: int, book_data: BookUpdate, db: AsyncSession = Depends(get_db)
):
    query = select(Book).where(Book.id == book_id)
    result = await db.execute(query)
    book = result.scalar_one_or_none()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book.title = book_data.title
    book.author = book_data.author
    book.year = book_data.year

    await db.commit()
    await db.refresh(book)

    return {"Message": "Book update successfully", "New book data": book}


@router.delete("/{book_id}")
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    query = select(Book).where(Book.id == book_id)
    result = await db.execute(query)
    book = result.scalar_one_or_none()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    await db.delete(book)
    await db.commit()

    return {"Message": "Book delete successfully"}
