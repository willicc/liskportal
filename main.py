import asyncio
from banner import display_banner
from config import web3
from check_in import check_in
from transactions import send_transactions
from colorama import Fore, Style
# Load private keys
with open("pvkeys.txt", "r") as file:
    private_keys = [line.strip() for line in file if line.strip()]
display_banner()

async def main():
    while True:
        for private_key in private_keys:
            from_address = web3.eth.account.from_key(private_key).address
            short_address = f"{from_address[:8]}...{from_address[-4:]}"
            print(f"{Fore.CYAN}[{short_address}] Processing Check in: {Style.RESET_ALL}")

            await check_in(from_address)
            print(f"{Fore.CYAN}[{short_address}] Processing Daily Transactions: {short_address}{Style.RESET_ALL}")
            await send_transactions(private_key, 75)

        print(f"{Fore.YELLOW}All accounts processed. Sleeping for 24 hours...{Style.RESET_ALL}")
        await asyncio.sleep(24 * 60 * 60)

asyncio.run(main())
