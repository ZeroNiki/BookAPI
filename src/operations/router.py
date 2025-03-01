from fastapi import APIRouter

router = APIRouter(prefix="/books", tags=["Books API"])


@router.get("/", response_model=list[dict])
async def get_all_books():
    pass


@router.get("/{book_id}", response_model=dict)
async def get_book(book_id: int):
    pass


@router.post("/", response_model=dict)
async def add_book():
    pass


@router.put("/{book_id}")
async def update_book(book_id: int):
    pass


@router.delete("/{book_id}")
async def delete_book(book_id: int):
    pass
