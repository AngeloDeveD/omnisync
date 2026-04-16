import json
from fastapi import FastAPI
from aiokafka import AIOKafkaProducer
from pydantic import BaseModel

app = FastAPI()

# Модель входящего заказа
class Order(BaseModel):
    order_id: int
    user_id: int
    item_id: str
    quantity: int

# Инициализируем продюсера Kafka
producer = AIOKafkaProducer(bootstrap_servers='kafka:9092')

@app.on_event("startup")
async def startup_event():
    await producer.start()

@app.on_event("shutdown")
async def shutdown_event():
    await producer.stop()

@app.post("/create-order")
async def create_order(order: Order):
    # Превращаем модель в байты для отправки в Kafka
    payload = json.dumps(order.dict()).encode('utf-8')
    
    # Отправляем событие в топик 'orders'
    await producer.send_and_wait("orders", payload)
    
    return {"status": "Order sent to processing", "order_id": order.order_id}