import asyncio
import websockets
import json
import time
async def send_message():
    async with websockets.connect("ws://localhost:8040") as websocket:
        # Prepare the message you want to send
        message = {"type": "start"}
        # Convert the message to JSON format
        message_json = json.dumps(message)
        # Send the message to the server
        await websocket.send(message_json)
        time.sleep(1)
        await websocket.send(json.dumps({"type": "end"}))
# Run the send_message coroutine
asyncio.run(send_message())

