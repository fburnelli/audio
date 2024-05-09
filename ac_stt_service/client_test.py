import websocket

# Define the WebSocket server address
websocket_server_address = "ws://localhost:8040"

# Connect to the WebSocket server
ws = websocket.create_connection(websocket_server_address)

# Send data
data_to_send = "Hello, WebSocket!"
ws.send(data_to_send)

# Close the connection
ws.close()

