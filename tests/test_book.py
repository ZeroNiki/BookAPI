from httpx import AsyncClient


async def test_add_book(client: AsyncClient):
    response = await client.post(
        "/books/",
        json={"title": "Test Book", "author": "John Doe", "year": 2020},
    )
    assert response.status_code == 200

    json_response = response.json()
    assert response.json()["Message"] == "Book added!"
    assert "id" in json_response


async def test_get_all_books(client: AsyncClient):
    response = await client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


async def test_get_book(client: AsyncClient):
    response = await client.post(
        "/books/",
        json={"title": "Test Book 2", "author": "Test author", "year": 1999},
    )

    book_id = response.json().get("id")
    assert book_id is not None

    response = await client.get(f"/books/{book_id}")

    assert response.status_code == 200

    assert response.json()["title"] == "Test Book 2"
    assert response.json()["author"] == "Test author"
    assert response.json()["year"] == 1999


async def test_update_book(client: AsyncClient):
    response = await client.post(
        "/books/",
        json={"title": "Old book", "author": "Old author", "year": 2222},
    )
    book_id = response.json().get("id")
    assert book_id is not None

    response = await client.put(
        f"/books/{book_id}",
        json={"title": "New book", "author": "New author", "year": 2007},
    )

    assert response.status_code == 200
    assert response.json()["New book data"]["title"] == "New book"
    assert response.json()["New book data"]["author"] == "New author"
    assert response.json()["New book data"]["year"] == 2007


async def test_delete_book(client: AsyncClient):
    response = await client.post(
        "/books/",
        json={"title": "To be deleted", "author": "Someone", "year": 8888},
    )
    book_id = response.json().get("id")
    assert book_id is not None

    response = await client.delete(f"/books/{book_id}")

    assert response.status_code == 200
    assert response.json()["Message"] == "Book delete successfully"
