from web3 import Web3

# Replace with your Infura project ID
INFURA_URL = "https://sepolia.infura.io/v3/ecaeed692c7f48509e5387e3404140e4"

# Connect to Infura
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check connection
if web3.is_connected():
    print("✅ Connected to Ethereum!")
else:
    print("❌ Connection failed.")

# Fetch latest block number
latest_block = web3.eth.block_number
print(f"Latest Ethereum Block: {latest_block}")

# Fetch current gas price
gas_price = web3.eth.gas_price
print(f"Current Gas Price: {web3.from_wei(gas_price, 'gwei')} Gwei")
