import asyncio
import time

from app.iot.message import MessageType

TIME_TO_SLEEP = 0.5


# of course this code looks dumb,
# but imagine some real implementations of each method here
class HueLightDevice:
    async def connect(self) -> None:
        print("Connecting Hue Light.")
        await asyncio.to_thread(time.sleep, TIME_TO_SLEEP)
        print("Hue Light connected.")

    async def disconnect(self) -> None:
        print("Disconnecting Hue Light.")
        await asyncio.to_thread(time.sleep, TIME_TO_SLEEP)
        print("Hue Light disconnected.")

    async def send_message(
            self,
            message_type: MessageType,
            data: str = ""
    ) -> None:
        print(
            f"Hue Light handling message of "
            f"type {message_type.name} with data [{data}]."
        )
        await asyncio.to_thread(time.sleep, TIME_TO_SLEEP)
        print("Hue Light received message.")


class SmartSpeakerDevice:
    async def connect(self) -> None:
        print("Connecting to Smart Speaker.")
        await asyncio.to_thread(time.sleep, TIME_TO_SLEEP)
        print("Smart Speaker connected.")

    async def disconnect(self) -> None:
        print("Disconnecting Smart Speaker.")
        await asyncio.to_thread(time.sleep, TIME_TO_SLEEP)
        print("Smart Speaker disconnected.")

    async def send_message(
            self,
            message_type: MessageType,
            data: str = ""
    ) -> None:
        print(
            f"Smart Speaker handling message of "
            f"type {message_type.name} with data [{data}]."
        )
        await asyncio.to_thread(time.sleep, TIME_TO_SLEEP)
        print("Smart Speaker received message.")


class SmartToiletDevice:
    async def connect(self) -> None:
        print("Connecting to Smart Toilet.")
        await asyncio.to_thread(time.sleep, TIME_TO_SLEEP)
        print("Smart Toilet connected.")

    async def disconnect(self) -> None:
        print("Disconnecting Smart Toilet.")
        await asyncio.to_thread(time.sleep, TIME_TO_SLEEP)
        print("Smart Toilet disconnected.")

    async def send_message(
            self,
            message_type: MessageType,
            data: str = ""
    ) -> None:
        print(
            f"Smart Toilet handling message "
            f"of type {message_type.name} with data [{data}]."
        )
        await asyncio.to_thread(time.sleep, TIME_TO_SLEEP)
        print("Smart Toilet received message.")
