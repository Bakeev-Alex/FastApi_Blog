from enum import Enum, IntEnum

from fastapi import FastAPI


app = FastAPI()


class ModelName(str, Enum):
    """
    Класс для выбора параметра
    """

    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def root():
    return {"message": "Hello word"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    """
    Получение значение из параметров url

    :param item_id: id
    :param q: Просто число для проверки
    :return: dict = значение ключей
    """
    return {"item_id": item_id, "q": q}


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    """
    Пример для выбора значения из Enum класса.
    Если в typing указать ModelName, то в swagger поле <model_name> будет с выбором
     параметра из этого класса.
    Parameters:
        model_name: ModelName = Имя модели
    """
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep learning alexnet"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "Deep Learning lenet"}
    return {"model_name": model_name, "message": f"Deep Learning {model_name}"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    """
    Передача get параметров в url
    """
    return fake_items_db[skip: skip + limit]
