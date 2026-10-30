from fastapi import FastAPI , Depends
from model import Product
from databaseconfig import SessionLocal,engine
import datab_model


app = FastAPI()


datab_model.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "hello"


def init_db():
    db = SessionLocal()

    count = 0

    count = db.query(datab_model.Product).count()

    if count == 0 :
        for val in productss:
            db.add(datab_model.Product(**val.model_dump()))
        db.commit()



def get_db():
     db = SessionLocal()
     try:
         yield db
     finally:
         db.close()


productss = [
    Product(id=1,name="abc",address="sd"),
    Product(id=2,name="abc",address="sd"),
    Product(id=3,name="abc",address="sd"),
    Product(id=4,name="abc",address="sd"),
]

init_db()

@app.get("/product")
def products(db:SessionLocal = Depends(get_db)):
    productsss = db.query(datab_model.Product).all()
    return productsss

@app.post("/product")
def products(product:Product):
     productss.append(product)
     return product

@app.get("/product/{id}")
def any_prod(id:int):
    print(type (id))
    for val in productss:
        if (val.id == id):
            return val.model_dump()

    return "Product not found"

@app.get("/qparams")
def anypost(data):
    return data

@app.delete("/product/{id}")
def delete_product(id: int):
    for index, val in enumerate(productss):
        if val.id == id:
            productss.pop(index)
            return {"message": "Product deleted successfully"}

    return {"message": "Product not found"}

@app.put("/product/{id}")
def update_product(id: int, updated_product: Product):
    for index, val in enumerate(productss):
        if val.id == id:
            productss[index] = updated_product
            return updated_product

    return {"message": "Product not found"}




'''

currently onlu implemented the db wioth the get all functionality and not with the other stuff like the update and delete and other they afre still handle ed with the prioducts  but wiuth the get all is connected with the db which is workking fine and can move forwarrd with that wright now abnd in further time will update other stuff lije the async a, rooute and other iportant prop 


'''

