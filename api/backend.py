import websockets
import asyncio
from mpu6050 import mpu6050
import api.motor_manager as motor_manager


async def server(websocket, path):
    async for message in websocket:
        await handle(message, websocket)


async def handle(message, websocket):
    type = message.split(":")[0]
    command = message.split(":")[1]

    if type == "command":
        print(command)
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
    elif type == "get":
        if command == "gyro":
            await websocket.send(mpu6050.get_gyro_data())
        elif command == "signal":
            await websocket.send("Nothing")


def start():
    start_server = websockets.serve(server, "0.0.0.0", 3000)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    start()
