import websockets
import asyncio
import api.motor_manager as motor_manager


async def server(websocket, path):
    asyncio.ensure_future(status_update(websocket))
    async for message in websocket:
        await handle(message, websocket)


async def status_update(websocket):
    i = 0
    while True:
        i += 1
        await asyncio.sleep(3)
        await websocket.send(await get_signal_strength())


async def get_signal_strength():
    proc = await asyncio.create_subprocess_shell(
        "/sbin/iwconfig wlan0",
        stdout=asyncio.subprocess.PIPE)

    stdout, _ = await proc.communicate()

    for line in stdout.decode().split("\n"):
        if 'Link Quality' in line:
            return line.lstrip(' ')
    return None


async def handle(message, websocket):
    type = message.split(":")[0]
    command = message.split(":")[1]

    if type == "command":
        if command.startswith("stop_"):
            motor_manager.stop()
        else:
            if command == "forward":
                motor_manager.forward()
            elif command == "backward":
                motor_manager.backward()
            elif command == "left":
                motor_manager.left()
            elif command == "right":
                motor_manager.right()


def start():
    start_server = websockets.serve(server, "0.0.0.0", 3000)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    start()
