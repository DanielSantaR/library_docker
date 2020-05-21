from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.encoders import jsonable_encoder
from app.models.book import Book, BookCreate, BookUpdate

router = APIRouter()

storage = []


@router.get('/')
def get_all_books():
    return storage


@router.get('/name/{name}')
def get_dog_by_name(*, name: str):

    found_books_by_name = []
    for i in range(len(storage)):
        if(storage[i]['name'] == name):
            book = storage[i]
            found_books_by_name.append(book)

    if not(found_books_by_name):
        message = f'No book found named {name}'
        return message

    return {'message': f'Found books named {name}', 'data': found_books_by_name}


@router.get('/id/{id}')
def get_book_by_id(*, id: int):

    found_books_by_id = []
    for i in range(len(storage)):
        if(storage[i]['id'] == id):
            book = storage[i]
            found_books_by_id.append(book)

    if not(found_books_by_id):
        message = f'No book found with id {id}'
        return message

    return {'message': f'Found book with id {id}', 'data': found_books_by_id}


@router.put('/{book_id}')
def update_book(*, book_id: int, book_in: BookUpdate):

    position_detected = False
    book_in = book_in.dict()

    for i in range(len(storage)):
        if storage[i]["id"] == book_id:
            position_detected = True
        if position_detected:
            if position_detected:
                storage.pop(i)
                storage.append(book_in)
                message = "Update completed"
                return message

    message = "Book not available"
    return message


@router.post('/')
def insert_book(
    *,
        book_in: BookCreate):

    id_exists = False
    book_in = book_in.dict()
    if len(storage) == 0:
        storage.append(book_in)
        message = "Insert successfully"
        return message
    else:
        for i in range(len(storage)):
            if storage[i]["id"] == book_in["id"]:
                id_exists = True

        if id_exists:
            message = "The book id already exists"
            return message
        else:
            storage.append(book_in)
            message = "Insert successfully"
            return message


@router.delete('/{book_id}')
def delete_book(*, book_id: int):

    position_detected = False

    for i in range(len(storage)):
        if storage[i]["id"] == book_id:
            position_detected = True
        if position_detected:
            if position_detected:
                storage.pop(i)
                message = "Delete completed"
                return message

    message = "Book not available"
    return message


@router.get('/generate_smoke_test/')
def generate_test():
    test1 = {
        "id": 11111,
        "name": "smoke book 1",
        "literary_genre": "smbk 1",
        "author": "team 1",
        "year": "2020",
        "price": 10000
    }

    test2 = {
        "id": 11112,
        "name": "smoke book 2",
        "literary_genre": "smbk 2",
        "author": "team 2",
        "year": "2020",
        "price": 10000
    }

    test3 = {
        "id": 11113,
        "name": "smoke book 3",
        "literary_genre": "smbk 3",
        "author": "team 3",
        "year": "2020",
        "price": 10000
    }
    test4 = {
        "id": 11114,
        "name": "smoke book 1",
        "literary_genre": "a_smbk 1",
        "author": "Juan",
        "year": "2001",
        "price": 15000
    }

    test5 = {
        "id": 11115,
        "name": "smoke book 2",
        "literary_genre": "b_smbk 2",
        "author": "Lucas",
        "year": "1990",
        "price": 100000
    }

    test6 = {
        "id": 11116,
        "name": "smoke book 3",
        "literary_genre": "c_smbk 3",
        "author": "Luis",
        "year": "2019",
        "price": 1000
    }

    storage.append(test1)
    storage.append(test2)
    storage.append(test3)
    storage.append(test4)
    storage.append(test5)
    storage.append(test6)

    message = "Smoke test generated"
    return message
