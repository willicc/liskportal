import asyncio
import json
from colorama import Fore, Style
from config import web3, AMOUNT_ETH, CONTRACT_ADDRESS, contract_abi

async def send_transactions(private_key, num_transactions):
    """Send multiple transactions for a single account."""
    amount_wei = web3.to_wei(AMOUNT_ETH, 'ether')
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=json.loads(contract_abi))
    from_address = web3.eth.account.from_key(private_key).address
    nonce = web3.eth.get_transaction_count(from_address)

    for i in range(num_transactions):
        try:
            transaction = contract.functions.deposit().build_transaction({
                'from': from_address,
                'value': amount_wei,
                'gas': 100000,
                'gasPrice': web3.eth.gas_price,
                'nonce': nonce
            })
            signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)
            tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f"{Fore.GREEN}[{from_address[:8]}...{from_address[-4:]}] Transaction {i + 1} sent: {tx_hash.hex()}{Style.RESET_ALL}")
            nonce += 1
            await asyncio.sleep(1)
        except Exception as e:
            print(f"{Fore.RED}[{from_address[:8]}...{from_address[-4:]}] Error in transaction {i + 1} : {str(e)}{Style.RESET_ALL}")
            await asyncio.sleep(5)
