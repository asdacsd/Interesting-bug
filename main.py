import time
from concurrent.futures import ThreadPoolExecutor
from typing import Optional
from fastapi import FastAPI, Query, Form, requests, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
executor = ThreadPoolExecutor()
origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


my_query = Query('NONE')


def test_func(item: Item, age: int = None):
    return {'item_id': item, 'age': age}


@app.get('/')
def index(q: str = my_query, my_item: dict = Depends(test_func)):
    return {'q': q, 'item': my_item}


class Test(BaseModel):
    user: str
    region: str


@app.post("/api/test")
async def root(Test: Test = None):
    time.sleep(1)
    return [
               {
                   'date': '2016-05-03',
                   'name': Test.user,
                   'address': 'No. 189, Grove St, Los Angeles',
                   'region': Test.region
               }
           ] * 40


@app.get("/hello/{name}")
async def say_hello(name: int):
    return {"message": f"Hello {name}"}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

1
@app.get("/users/{id}/{ddd}")
async def read_user(id: str):
    return {"user_id": f'{id}hhhhhaole'}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    url = f'./{file_path}.txt'
    with open(url, "wb") as f:
        f.write(b"Hello World")
    return {"file_path": file_path}


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.post("/items/")
async def create_item(item: Item):
    print(item)
    print(item.Config.allow_mutation)
    print(type(item))
    return item


@app.get("/items/")
async def create_item(item: Item):
    return item


@app.get("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    print(dir(item))
    result = dict(item)
    result["item_id"] = item_id
    if q:
        result.update({"q": q})
    return result


@app.get('/test/{item_id}')
async def test(item_id: int):
    return {'item_id': item_id}


if __name__ == '__main__':
    import uvicorn

    # print(cpu_count())
    print('启动成功')
    uvicorn.run(app="main:app",
                host="0.0.0.0",
                port=8000,
                workers=1,  # cpu_count()
                debug=True  # True
                )

