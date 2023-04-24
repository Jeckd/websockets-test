import websockets

import asyncio
import aioconsole


async def main():
    async with websockets.connect("ws://localhost:8017/ws") as websocket:
        task1 = asyncio.create_task(send(websocket))
        task2 = asyncio.create_task(receive(websocket))
        await asyncio.wait([task1, task2])


async def receive(ws: websockets):
    while True:
        async for message in ws:
            print(message)


async def send(ws: websockets):
    while True:
        await ws.send(await aioconsole.ainput(">>"))


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt as ex:
        print("\nBye!")
