# WS client example

import asyncio
import websockets
import json


async def hello():
    uri = "wss://api.testnet.fmex.com/v2/ws"
    async with websockets.connect(uri) as websocket:
        greeting = await websocket.recv()
        print(f"< {greeting}")

        await websocket.send(
            json.dumps(
                {"cmd": "ping", "args": [1540557696867], "id": "sample.client.id"}
            )
        )
        greeting = await websocket.recv()
        print(f"< {greeting}")

        await websocket.send(json.dumps({"cmd": "sub", "args": ["ticker.btcusd_p"]}))
        greeting = await websocket.recv()
        print(f"< {greeting}")

        for i in range(5):
            greeting = await websocket.recv()
            print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
