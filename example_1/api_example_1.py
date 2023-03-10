import uvicorn
from fastapi import FastAPI

app = FastAPI()

inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "dospinos"
    },
    2: {
        "name": "Milk",
        "price": 4.99,
        "brand": "coronado"
    }
}


@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
