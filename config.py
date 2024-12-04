from web3 import Web3

RPC_URL = "https://rpc.api.lisk.com"
CONTRACT_ADDRESS = "0x4200000000000000000000000000000000000006"
GRAPHQL_URL = "https://portal-api.lisk.com/graphql"
AMOUNT_ETH = 0.0000000001  # ETH amount per transaction
web3 = Web3(Web3.HTTPProvider(RPC_URL))

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
