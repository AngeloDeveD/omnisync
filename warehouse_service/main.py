import asyncio
import json
from aiokafka import AIOKafkaConsumer

async def consume():
    # Настраиваем консьюмера
    consumer = AIOKafkaConsumer(
        'orders',
        bootstrap_servers='kafka:9092',
        group_id="warehouse-group"
    )
    
    await consumer.start()
    print("Warehouse Service started. Waiting for orders...")
    
    try:
        async for msg in consumer:
            order_data = json.loads(msg.value.decode('utf-8'))
            order_id = order_data.get("order_id")
            item_id = order_data.get("item_id")
            
            # Имитация бизнес-логики (резервирование)
            print(f" [OK] Processing order {order_id}: reserving {order_data['quantity']} of {item_id}")
            
            # Тут в будущем будет запрос к PostgreSQL через SQLAlchemy/Tortoise
            await asyncio.sleep(1) 
            print(f" [DONE] Stock updated for order {order_id}")
            
    finally:
        await consumer.stop()

if __name__ == "__main__":
    asyncio.run(consume())