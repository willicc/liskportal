import time
from web3 import Web3

# Parameter
max_gwei = 15
num_daily_tx = 75
RPC_URL = "https://rpc.api.lisk.com"
RPC_ETH = "https://eth.llamarpc.com"
CONTRACT_ADDRESS = "0x4200000000000000000000000000000000000006"
GRAPHQL_URL = "https://portal-api.lisk.com/graphql"
AMOUNT_ETH = 0.0000000001  # ETH amount per transaction
DELAY_MINUTES = 3  # Set delay in minutes for each transaction

# Web3 initialization
web3 = Web3(Web3.HTTPProvider(RPC_URL))
check_gass = Web3(Web3.HTTPProvider(RPC_ETH))

# Contract ABI
contract_abi = '''
[
    {
        "constant": false,
        "inputs": [],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
]
'''

# Countdown function
def countdown(delay_seconds):
    try:
        while delay_seconds:
            mins, secs = divmod(delay_seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(f"Waiting for next transaction... {timer}", end="\r")
            time.sleep(1)
            delay_seconds -= 1
        print(" " * 50, end="\r")  # Clear the line after countdown finishes
    except KeyboardInterrupt:
        print("\nCountdown interrupted. Exiting gracefully.")
        raise

# Function to send transactions with delay
def send_transactions_with_delay():
    try:
        contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)
        for i in range(num_daily_tx):
            print(f"Sending transaction {i + 1}...")
            
            # Simulated transaction placeholder (replace with actual transaction logic)
            # tx_hash = contract.functions.deposit().transact({'from': your_address, 'value': Web3.toWei(AMOUNT_ETH, 'ether')})
            # web3.eth.wait_for_transaction_receipt(tx_hash)
            
            print(f"Transaction {i + 1} sent!")
            
            # Delay with countdown
            if i < num_daily_tx - 1:  # No delay after the last transaction
                countdown(DELAY_MINUTES * 60)
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting safely.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
send_transactions_with_delay()

