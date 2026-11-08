from fastapi import APIRouter, HTTPException
from app.database import db
from app.models import Order
from bson import ObjectId

router = APIRouter()

@router.get("/")
async def get_orders():
    orders = []
    async for order in db.orders.find().sort("created_at", -1):
        order["_id"] = str(order["_id"])
        orders.append(order)
    return orders

@router.post("/")
async def create_order(order: Order):
    order_dict = order.dict(by_alias=True)
    result = await db.orders.insert_one(order_dict)
    return {"id": str(result.inserted_id), "message": "Order created successfully"}

@router.get("/{order_id}")
async def get_order(order_id: str):
    if not ObjectId.is_valid(order_id):
        raise HTTPException(status_code=400, detail="Invalid order ID")
    order = await db.orders.find_one({"_id": ObjectId(order_id)})
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order["_id"] = str(order["_id"])
    return order
