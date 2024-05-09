import asyncio
import json
import websockets
import http
import os
import time
import datetime
import uuid
import wave
import array

logger = print
listen_host = '127.0.0.1'
stt_port = 8040
log_sent = bool(os.environ.get('LOG_SENT'))
log_received = bool(os.environ.get('LOG_RECEIVED'))

conversation_id = str(uuid.uuid4())
print("Random UUID (version 4):", conversation_id)
concatenated_audio = array.array('h')

class SttSession:
    def __init__(self, ws):
        self.ws = ws
        self.ended = False

    async def send(self, message):
        print(f"send {message}")
        msg = json.dumps(message)
        if self.ws.open:
            if log_sent:
                logger('sending:', msg)
            await self.ws.send(msg)

    async def send_hypothesis(self, hypo_obj):
        print("send_hypothesis")
        await self.send({
            'type': 'hypothesis',
            'alternatives': [{'text': hypo_obj['text'].lower()}]
        })

    async def send_recognition(self, rec_obj):
        print("send_recognition")
        await self.send({
            'type': 'recognition',
            'alternatives': [{'text': rec_obj['text'].lower(), 'confidence': 0.8355}]
        })

    async def on_message(self, message, is_binary=False):
        print("on_message")
        if not is_binary and message.startswith('{'):
            ac_api_msg = json.loads(message)
            msg_type = ac_api_msg.get('type')
            if msg_type == 'start':
                await self.send({'type': 'started'})
                await asyncio.sleep(0.05)
            elif msg_type == 'stop':
                await self.send({'type': 'end', 'reason': 'stopped by client'})
            elif msg_type == 'end':
                self.ended = True
                await self.send({'type': 'end', 'reason': 'ended by client'})
                await asyncio.sleep(0.05)
                await self.ws.close()
                return
        elif is_binary:
            print("got a chunk",len(message))
            # save stream

        
        # here the simulated call ....   
        #await (self.send_hypothesis(obj) if obj['type'] == 'hypothesis' else self.send_recognition(obj))
        
async def stt_handler(ws, _):
    session = SttSession(ws)
    async for message in ws:
        print("stt_handler: for message in ws:")         

        if isinstance(message, bytes):
            ts = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")[:-3] 
            filename = 'stream_' + ts + '.wav'
            print(f"stream length:{len(message)}")
            audio_data = array.array('h', message)
            concatenated_audio.extend(audio_data)

            is_binary = True
        else:
            print("not binary message")
            msg_str = message
            is_binary = False
        if log_received:
            print("log_received")
            if is_binary:
                print('received: ---binary data--- length:', len(msg_str))
            else:
                print('received:', msg_str)
        if is_binary or not msg_str.startswith('{'):
            print("continue....")
            continue
        msg_json = json.loads(msg_str)
        print(msg_json)
        if msg_json.get('type') == 'start':
            try:
                print("not clear wehn BEFORE on_message")
                await session.on_message(msg_str)
                print("not clear wehn AFTER on_message")
            except Exception as e:
                logger('Error:', e)

async def stt_server():
    async with websockets.serve(stt_handler, listen_host, stt_port):
        logger(f"STT Server is listening on {stt_port} ({listen_host}).")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    print("START")
    try:
        asyncio.run(stt_server())
    except:
        with wave.open(f'conv_id_{conversation_id}.wav', 'w') as file:
            file.setnchannels(1)  # Mono
            file.setsampwidth(2)  # 2 bytes for linear16 encoding
            file.setframerate(16000)  # 16kHz sample rate
            file.setcomptype('NONE', 'not compressed')  # No compression
            file.writeframes(concatenated_audio)
        
    print("END")
