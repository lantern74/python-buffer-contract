from web3 import Web3

# Replace with your Infura/Alchemy URL
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Replace with your wallet address and private key
wallet_address = '0xYourWalletAddress'
private_key = 'YourPrivateKey'

# Replace with the Buffer contract address
buffer_contract_address = '0xYourBufferContractAddress'

# Replace with the ABI for the Buffer smart contract (you need the full ABI JSON structure here)
buffer_abi = [
    # Add the actual ABI of the Buffer smart contract
]

# Create contract instance
buffer_contract = w3.eth.contract(address=buffer_contract_address, abi=buffer_abi)

# Function to open a trade
def open_trade(direction, amount):
    # direction can be 0 for "down" or 1 for "up"
    nonce = w3.eth.get_transaction_count(wallet_address)
    
    # Prepare the transaction
    txn = buffer_contract.functions.openTrade(direction, amount).buildTransaction({
        'chainId': 1,  # Mainnet (use 4 for Rinkeby, etc.)
        'gas': 2000000,
        'gasPrice': w3.toWei('50', 'gwei'),
        'nonce': nonce,
    })

    # Sign the transaction
    signed_txn = w3.eth.account.signTransaction(txn, private_key)

    # Send the transaction
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(f'Transaction sent with hash: {txn_hash.hex()}')

# Example usage:
# Open an "up" trade with an amount of 1 (adjust this based on contract specifications)
open_trade(1, 1)  # 1 for "up", amount: 1 unit
