from typing import Optional
import asyncio
import argparse
import logging
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utcxchangelib.xchange_client import XChangeClient, Side

logging.basicConfig(level=logging.INFO)
_LOGGER = logging.getLogger("team-university_name-bot")
_LOGGER.setLevel(logging.INFO)


class MyXchangeClient(XChangeClient):

    def __init__(self, host: str, username: str, password: str):
        super().__init__(host, username, password)

    async def bot_handle_cancel_response(self, order_id: str, success: bool, error: Optional[str]) -> None:
        pass

    async def bot_handle_order_fill(self, order_id: str, qty: int, price: int):
        print("Order fill:", self.positions)

    async def bot_handle_order_rejected(self, order_id: str, reason: str) -> None:
        pass

    async def bot_handle_trade_msg(self, symbol: str, price: int, qty: int):
        pass

    async def bot_handle_book_update(self, symbol: str) -> None:
        pass

    async def bot_handle_swap_response(self, swap: str, qty: int, success: bool):
        pass

    async def bot_handle_news(self, news_release: dict):
        pass

    async def trade(self):
        pass

    async def start(self, user_interface):
        asyncio.create_task(self.trade())
        if user_interface:
            self.launch_user_interface()
            asyncio.create_task(self.handle_queued_messages())
        await self.connect()


async def main(user_interface: bool):
    # Use actual server values when running live
    SERVER = 'INSERT_SERVER_URL_HERE'
    my_client = MyXchangeClient(SERVER, "YOUR_USERNAME", "YOUR_PASSWORD")
    await my_client.start(user_interface)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run trading bot with optional Phoenixhood UI")
    parser.add_argument("--phoenixhood", required=False, default=False, type=bool, help="Starts Phoenixhood if True")
    args = parser.parse_args()

    user_interface = args.phoenixhood
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(main(user_interface))