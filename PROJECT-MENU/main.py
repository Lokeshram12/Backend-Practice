from fastapi import FastAPI,Query,HTTPException
from models import MenuItem,MenuResponse
from data import menu_items

app = FastAPI(
    title="Chai Menu API",
    description="Read only menu API"
)

@app.get("/hello")

def root():
    return {"message":"Welcome to MENU API"}

@app.get("/menu",response_model=MenuResponse)

def get_menu(category:str|None=Query(None,description="Filter by chai,snack or combo")):
    if category:

        filtered_items = [item for item in menu_items if item["category"]==category.lower()]
       
        if not filtered_items:

            raise HTTPException(status_code=404,detail=f"No item found for this category:{category}")

        return MenuResponse(count=len(filtered_items),items=filtered_items)
    
    return MenuResponse(count=len(menu_items),items=menu_items)


@app.get("/menu/{item_id}",response_model=MenuResponse)
def get_item(item_id:int):
    filtered_item=[item for item in menu_items if item["id"]==item_id]
    if not filtered_item:
        raise HTTPException(status_code=404,detail=f"Item not found")
    return MenuResponse(count=len(filtered_item),items=filtered_item)